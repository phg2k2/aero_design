#ifndef FLYING_WING_CG_H
#define FLYING_WING_CG_H

double calculate_mean_aerodynamic_chord(double root_chord, double tip_chord);

double calculate_distance_to_mac(double half_span, double root_chord, double tip_chord);

double calculate_sweep_at_mac(double sweep_distance, double root_chord, double tip_chord);

double calculate_aerodynamic_center_from_root_leading_edge(double sweep_at_mac_val, double mac);

double calculate_center_of_gravity_from_root_leading_edge(double ac_from_root_le_val, double static_margin, double mac);

double calculate_total_area(double root_chord, double tip_chord, double half_span);

double calculate_aspect_ratio(double half_span, double total_area_val);

#endif // FLYING_WING_CG_H