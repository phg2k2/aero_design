#include "weightCore.h"
#include "missionProfile.h"
#include "constants.h"
#include <math.h>
#include <stddef.h>


double calc_power_required(double weight, double velocity, double l_d_ratio) {
    const double g = get_gravity(); 
    return (weight * g * velocity) / l_d_ratio; 
}

double calc_battery_weight(double p_required, double flight_time, double sed, double eta_total) {
    double p_battery = p_required / eta_total; 
    return (p_battery * flight_time) / sed; 
}

WeightResults iterate_gross_weight(MissionProfile profile, double initial_guess, double* history_buffer) {
    WeightResults res;
    res.convergence_history = history_buffer; // Gán địa chỉ mảng để tránh Segfault
    
    double w_old, w_new = initial_guess;
    double eta_total = profile.eta_propulsive * profile.eta_electrical * profile.eta_motor;
    res.iterations_count = 0;

    // CỐ ĐỊNH trọng lượng dựa trên Baseline thiết kế (ví dụ 0.7kg) 
    res.structural_weight_kg = profile.struct_ratio * initial_guess; 
    res.propulsion_weight_kg = profile.prop_ratio * initial_guess;

    do {
        w_old = w_new;
        
        // Lưu lịch sử hội tụ vào bộ đệm
        if (history_buffer != NULL && res.iterations_count < 1000) {
            history_buffer[res.iterations_count] = w_old;
        }
        res.iterations_count++;

        // Tính công suất và trọng lượng pin biến thiên [cite: 787-788]
        double p_req = (w_old * get_gravity() * profile.v_cruise_mps) / profile.lift_to_drag_ratio;
        double p_battery = p_req / eta_total;
        res.battery_weight_kg = (p_battery * profile.flight_time_hrs) / profile.energy_density_wh_per_kg;

        // Trọng lượng tổng mới = (Cấu trúc + Động cơ + Tải trọng) CỐ ĐỊNH + Pin BIẾN THIÊN
        w_new = res.structural_weight_kg + res.propulsion_weight_kg + 
                res.battery_weight_kg + profile.payload_weight_kg;

    } while (fabs(w_new - w_old) > 1e-10 && res.iterations_count < 1000);

    res.total_weight_kg = w_new;
    return res;
}