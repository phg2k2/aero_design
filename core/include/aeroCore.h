#ifndef AERO_CORE_H
#define AERO_CORE_H

double calc_lift_slope(double a2d, double AR, double e);
double cal_induced_drag_coeff(double Cl, double AR, double e);
double calc_total_drag(double Cd0, double k, double Cl);
double calc_lift_drag_ratio(double Cl, double Cd);

#endif // AERO_CORE_H