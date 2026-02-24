import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Thiết lập Figure cho đồ họa kỹ thuật
        self.fig = Figure(figsize=(8, 6), tight_layout=True)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        layout.addWidget(self.canvas)

    def draw_uav_wing(self, a, b, s, y, mac_val, cg_val):
        """
        Vẽ sơ đồ hình học cánh Flying Wing.
        a: Root Chord, b: Tip Chord, s: Sweep, y: Half Span
        mac_val: Chiều dài MAC, cg_val: Vị trí CG tính từ mũi cánh (Root LE)
        """
        self.ax.clear()
        
        # 1. Định nghĩa các tọa độ đỉnh cánh (Nửa cánh trái và phải)
        # Tọa độ: (X, Y) - X là trục dọc thân, Y là sải cánh
        root_le = [0, 0]
        root_te = [a, 0]
        tip_le_right = [s, y]
        tip_te_right = [s + b, y]
        tip_le_left = [s, -y]
        tip_te_left = [s + b, -y]

        # 2. Vẽ biên dạng cánh (Outline)
        # Vẽ mép trước (Leading Edge)
        self.ax.plot([tip_le_left[1], root_le[1], tip_le_right[1]], 
                     [tip_le_left[0], root_le[0], tip_le_right[0]], 'k-', lw=2)
        # Vẽ mép sau (Trailing Edge)
        self.ax.plot([tip_te_left[1], root_te[1], tip_te_right[1]], 
                     [tip_te_left[0], root_te[0], tip_te_right[0]], 'k-', lw=2)
        # Vẽ mút cánh (Wing Tips)
        self.ax.plot([tip_le_right[1], tip_te_right[1]], [tip_le_right[0], tip_te_right[0]], 'k-', lw=2)
        self.ax.plot([tip_le_left[1], tip_te_left[1]], [tip_le_left[0], tip_te_left[0]], 'k-', lw=2)

        # 3. Vẽ ký hiệu Trọng tâm (CG)
        # Sử dụng ký hiệu hình tròn chia 4 (đặc trưng trong tờ trình kỹ thuật)
        self.ax.plot(0, cg_val, marker='o', markersize=12, color='red', label=f'CG: {cg_val:.2f} mm')
        self.ax.axhline(y=cg_val, color='red', linestyle='--', alpha=0.3)

        # 4. Vẽ đường MAC (Mean Aerodynamic Chord)
        # Giả sử MAC nằm ở vị trí hình học trung bình (đơn giản hóa để hiển thị)
        y_mac = y / 2 
        self.ax.plot([y_mac, y_mac], [s/2, s/2 + mac_val], 'b--', lw=1.5, label=f'MAC: {mac_val:.2f} mm')

        # 5. Định dạng đồ thị chuyên nghiệp
        self.ax.set_title("Sơ đồ hình học và Trọng tâm UAV", fontweight='bold')
        self.ax.set_xlabel("Sải cánh (mm)")
        self.ax.set_ylabel("Chiều dài thân (mm)")
        
        # Đảo ngược trục Y để mũi máy bay hướng lên trên (giống XFLR5)
        self.ax.invert_yaxis() 
        self.ax.axis('equal') # Giữ đúng tỉ lệ hình học
        self.ax.grid(True, linestyle=':', alpha=0.6)
        self.ax.legend(loc='lower right')
        
        self.canvas.draw()