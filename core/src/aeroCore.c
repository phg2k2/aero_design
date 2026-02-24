#include "aeroCore.h"
#include "constants.h"
#include <math.h>

double calc_lift_slope(double a2d, double AR, double e) {
    return a2d / (1 + (a2d / (get_pi() * AR * e)));
}

double cal_induced_drag_coeff(double Cl, double AR, double e) {
    return (Cl * Cl) / (get_pi() * AR * e);
}

double calc_total_drag(double Cd0, double k, double Cl) {
    return Cd0 + k * Cl * Cl;
}

double calc_lift_drag_ratio(double Cl, double Cd) {
    if (Cd == 0) {
        return 0.0; // Avoid division by zero
    }
    return Cl / Cd;
}