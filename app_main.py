import sys
import os
import socket

# Choose a Qt platform plugin before importing PyQt6.
# If DISPLAY is unset or unreachable (remote/X11 not available), use offscreen.
display = os.environ.get('DISPLAY', '')
use_offscreen = False
if not display:
    use_offscreen = True
else:
    # DISPLAY can be like "host:display.screen" or ":0" for local unix socket.
    try:
        host_part = display.split(':', 1)[0]
        if host_part and host_part != 'localhost':
            disp_num = int(display.split(':', 1)[1].split('.', 1)[0])
            port = 6000 + disp_num
            # try TCP connect with short timeout
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            try:
                s.connect((host_part, port))
            except Exception:
                use_offscreen = True
            finally:
                s.close()
    except Exception:
        # if parsing/connection fails, fall back to offscreen
        use_offscreen = True

if use_offscreen:
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'

from PyQt6.QtWidgets import QApplication

def get_resource_path(relative_path):
    """ Xử lý đường dẫn động cho cả môi trường phát triển và sau khi đóng gói """
    try:
        base_path = sys._MEIPASS # Thư mục tạm của PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

from ui.main_window import CFDAeroApp

def main():
    app = QApplication(sys.argv)
    
    # Nạp giao diện QSS rành mạch
    style_path = get_resource_path("ui/resources/style.qss")
    if os.path.exists(style_path):
        with open(style_path, "r") as f:
            app.setStyleSheet(f.read())
    else:
        print(f"Cảnh báo: Không tìm thấy file style.qss tại {style_path}")

    # Đường dẫn thư viện lõi C đã xử lý động
    lib_path = get_resource_path("core/libwingcore.so")
    
    window = CFDAeroApp(lib_path)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()