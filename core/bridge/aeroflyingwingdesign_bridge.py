import ctypes
import os

D = ctypes.c_double
I = ctypes.c_int
P = ctypes.POINTER(D)

class AeroDesignBridge:
    def __init__(self, lib_path):
        """Khởi tạo và nạp thư viện lõi C (.so)"""
        if not os.path.exists(lib_path):
            raise FileNotFoundError(f"Không tìm thấy thư viện tại: {lib_path}")
        
        self.lib = ctypes.CDLL(os.path.abspath(lib_path))
        self._register_api()

    def _register_api(self):
        """Đăng ký Prototype cho toàn bộ hàm trong lõi C"""
        api_config = {
            # Hằng số môi trường
            "get_air_density": (D, []),
            "get_mu_air": (D, []),
            "get_pi": (D, []),
            
            # Các hàm tính toán thiết kế cánh bay
            "calculate_mean_aerodynamic_chord": (D, [D, D]),
            "calculate_distance_to_mac": (D, [D, D, D]),
            "calculate_sweep_at_mac": (D, [D, D, D]),
            "calculate_aerodynamic_center_from_root_leading_edge": (D, [D, D]),
            "calculate_center_of_gravity_from_root_leading_edge": (D, [D, D, D]),
            "calculate_total_area": (D, [D, D, D]),
            "calculate_aspect_ratio": (D, [D, D]),
        }

        for func_name, (res, args) in api_config.items():
            try:
                func = getattr(self.lib, func_name)
                func.restype = res
                func.argtypes = args
            except AttributeError:
                print(f"⚠️ Cảnh báo: Hàm '{func_name}' chưa được định nghĩa trong lõi C.")
    
    def flyingwingdesign_calculations(self, A, B, Y, S, SM):
        mac = self.lib.calculate_mean_aerodynamic_chord(A, B)
        distance_to_mac = self.lib.calculate_distance_to_mac(Y, A, B)
        sweep_at_mac = self.lib.calculate_sweep_at_mac(S,A,B)
        ac_from_le = self.lib.calculate_aerodynamic_center_from_root_leading_edge(sweep_at_mac, mac)
        cg_from_le = self.lib.calculate_center_of_gravity_from_root_leading_edge(ac_from_le, SM, mac)
        total_area = self.lib.calculate_total_area(A, B, Y)
        aspect_ratio = self.lib.calculate_aspect_ratio(Y, total_area)

        return {
            "mean_aerodynamic_chord": mac,
            "distance_to_mac": distance_to_mac,
            "sweep_at_mac": sweep_at_mac,
            "ac_from_le": ac_from_le,
            "cg_from_le": cg_from_le,
            "total_area": total_area,
            "aspect_ratio": aspect_ratio
        }