#include "flyingWingCG.h"

double calculate_mean_aerodynamic_chord(double root_chord, double tip_chord){
    double A = root_chord;
    double B = tip_chord;
    return (2.0/3.0)*((A*A+A*B+B*B)/(A+B));
}

double calculate_distance_to_mac(double half_span, double root_chord, double tip_chord){
    double A = root_chord;
    double B = tip_chord;
    double Y = half_span;
    return (Y/3.0)*((A+2*B)/(A+B));
}

double calculate_sweep_at_mac(double sweep_distance, double root_chord, double tip_chord){
    double A = root_chord;
    double B = tip_chord;
    double S = sweep_distance;
    return (S*(A+2*B))/(3.0*(A+B));
}

double calculate_aerodynamic_center_from_root_leading_edge(double sweep_at_mac_val, double mac){
    return sweep_at_mac_val+0.25*mac;
}

double calculate_center_of_gravity_from_root_leading_edge(double ac_from_root_le_val, double static_margin, double mac){
    return ac_from_root_le_val-(static_margin*mac);
}

double calculate_total_area(double root_chord, double tip_chord, double half_span){
    return (root_chord+tip_chord)*half_span;
}

double calculate_aspect_ratio(double half_span, double total_area_val){
    return (4*half_span*half_span)/total_area_val;
}