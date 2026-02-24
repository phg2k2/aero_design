from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QGridLayout, QMessageBox
from ui.layouts.main_layouts import MainGridLayout
from ui.widgets.input_panel import InputPanel
from ui.widgets.output_table import OutputTable
from ui.widgets.plot_canvas import PlotCanvas
from core.bridge.aeroflyingwingdesign_bridge import AeroDesignBridge

class CFDAeroApp(QMainWindow):
    def __init__(self, lib_path):
        super().__init__()
        self.bridge = AeroDesignBridge(lib_path)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("UAV Design App - Aerospace Engineering")
        self.resize(1300, 850)

        # Hệ thống Tab chính
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        #Tab 1
        self.tab_aero = QWidget()
        self.setup_flyingwingdesign_tab()
        self.tabs.addTab(self.tab_aero, "Flying Wing Design")


    def setup_flyingwingdesign_tab(self):
        layout = MainGridLayout(self.tab_aero)
        
        # Cấu hình tham số Aero
        aero_params = [
            ("A", "Wing Root Chord", "300.0", "-"),
            ("B", "Wing Tip Chord", "150.0", "-"),
            ("Y", "Wing Half Span", "600.0", "-"),
            ("S", "Wing Sweep Distance", "200.0", "-"),
            ("SM", "Static Margin", "0.1", "-")
        ]
        
        self.aero_input = InputPanel(title="Input", params=aero_params)
        self.aero_output = OutputTable(title="Output")
        self.aero_plot = PlotCanvas()

        layout.assemble(self.aero_input, self.aero_output, self.aero_plot)

        self.aero_input.submitted.connect(self.run_aero_analysis)

    def run_aero_analysis(self, data):
        try:
            # Gọi tính toán từ lõi C thông qua Bridge
            res = self.bridge.flyingwingdesign_calculations(
                float(data['A']), float(data['B']), float(data['Y']), float(data['S']), float(data['SM'])
            )
            
            # Hiển thị kết quả rành mạch cho tờ trình
            display = {
                "Mean Aerodynamic Chord": f"{res['mean_aerodynamic_chord']:.2f}",
                "Distance to MAC": f"{res['distance_to_mac']:.2f}",
                "Sweep at MAC": f"{res['sweep_at_mac']:.2f}",
                "Aerodynamic Center from LE": f"{res['ac_from_le']:.2f}",
                "Center of Gravity from LE": f"{res['cg_from_le']:.2f}",
                "Total Area": f"{res['total_area']:.2f}",
                "Aspect Ratio": f"{res['aspect_ratio']:.2f}"
            }
            self.aero_output.update_results(display)
            
            # Vẽ đồ thị trực quan thang Log
            self.aero_plot.draw_uav_wing(
                a=float(data['A']), b=float(data['B']), s=float(data['S']), y=float(data['Y']), mac_val=res['mean_aerodynamic_chord'], cg_val=res['cg_from_le']
            )

        except Exception as e:
            QMessageBox.critical(self, "Lỗi Thực thi", f"Kiểm tra lõi C: {str(e)}")
