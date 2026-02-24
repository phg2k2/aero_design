#ifndef CONSTANTS_H
#define CONSTANTS_H

#define CONSTANTS_LIST \
    X(PI, 3.14159265358979323846, get_pi)            \
    X(AIR_DENSITY, 1.225, get_air_density)   \
    X(MU_AIR, 1.81e-5, get_mu_air)       \
    X(SEA_LEVEL_PRESSURE, 101325.0, get_sea_level_pressure) \
    X(SEA_LEVEL_TEMPERATURE, 288.15, get_sea_level_temperature) \
    X(GRAVITY, 9.81, get_gravity)            \
    X(DEFAULT_EFF_ELECTRICITY, 0.98, get_eff_electricity) \
    X(DEFAULT_EFF_MOTOR, 0.9, get_eff_motor) \
    X(DEFAULT_EFF_PROP, 0.95, get_eff_prop) \
    X(WSTR_W, 0.6614, get_wstr_w) \
    X(WP_W, 0.1028, get_wp_w)   \
    X(BALSAWOOD_E, 11.4e9, get_balsawood_e) \
    X(BALSAWOOD_DENSITY, 400.0, get_balsawood_density)\
    X(BALSAWOOD_POISSON, 0.3, get_balsawood_poisson)    \
    X(OSWALD_EFFICIENCY, 0.8, get_oswald_efficiency) \
    X(PARASITIC_DRAG_COEFF, 0.03, get_parasitic_drag_coeff) \
    X(SED, 34.8857, get_sed) \
    X(VON_KARMAN_CONST, 0.41, get_von_karman_const)


#define X(val, num, func) double func(void);
CONSTANTS_LIST
#undef X

#endif // CONSTANTS_H