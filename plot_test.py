import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Thiết lập Figure chuyên nghiệp cho kỹ thuật hàng không 
        self.fig = Figure(figsize=(8, 6), tight_layout=True)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        layout.addWidget(self.canvas)

    def draw_uav_wing(self, a, b, s, y, mac_val, cg_val):
        """
        Cập nhật sơ đồ hình học cánh UAV: MAC luôn nằm trong biên dạng.
        a: Root Chord, b: Tip Chord, s: Sweep, y: Half Span
        """
        self.ax.clear()
        
        # --- 1. Tính toán tọa độ MAC theo logic plot_test để khớp biên dạng  ---
        # d: Vị trí sải cánh đặt MAC 
        d_mac = (y / 3) * ((a + 2 * b) / (a + b))
        # c: Độ lùi Leading Edge tại vị trí d_mac 
        c_mac = (s * (a + 2 * b)) / (3 * (a + b))
        # Chiều dài MAC tính toán để vẽ 
        mac_len = (2/3) * (a**2 + a*b + b**2) / (a + b)

        # --- 2. Vẽ biên dạng cánh đối xứng (Cánh phải và trái)  ---
        # Mép trước (Leading Edge): Tip Left -> Root -> Tip Right
        self.ax.plot([-y, 0, y], [s, 0, s], 'b-', lw=2, label='Wing Profile')
        # Mép sau (Trailing Edge): Tip Left -> Root -> Tip Right
        self.ax.plot([-y, 0, y], [s + b, a, s + b], 'b-', lw=2)
        # Hai đầu mút cánh (Wing Tips)
        self.ax.plot([y, y], [s, s + b], 'b-', lw=2)
        self.ax.plot([-y, -y], [s, s + b], 'b-', lw=2)

        # --- 3. Vẽ MAC và Trọng tâm (CG)  ---
        # Vẽ MAC tại vị trí d_mac, đảm bảo nằm gọn bên trong biên dạng 
        self.ax.plot([d_mac, d_mac], [c_mac, c_mac + mac_len], 'r--', lw=2, label=f'MAC: {mac_len:.1f} mm')
        
        # Đánh dấu trọng tâm CG bằng dấu X màu đỏ tại trục trung tâm (Y=0) 
        self.ax.plot(0, cg_val, 'rX', markersize=10, label=f'CG: {cg_val:.2f} mm')
        
        # Đường kẻ ngang phụ trợ để quan sát vị trí CG so với MAC 
        self.ax.axhline(y=cg_val, color='red', linestyle=':', alpha=0.4)

        # --- 4. Định dạng đồ thị theo tiêu chuẩn báo cáo kỹ thuật  ---
        self.ax.set_title("UAV Wing Geometry & Stability Analysis", fontweight='bold')
        self.ax.set_xlabel("Sải cánh - Spanwise (mm)")
        self.ax.set_ylabel("Chiều dài thân - Chordwise (mm)")
        
        self.ax.invert_yaxis() # Mũi máy bay hướng lên trên 
        self.ax.axis('equal')  # Giữ đúng tỉ lệ hình học không bị bóp méo 
        self.ax.grid(True, linestyle=':', alpha=0.6)
        self.ax.legend(loc='lower right')
        
        self.canvas.draw()