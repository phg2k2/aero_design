#ifndef WING_CONFIG_H
#define WING_CONFIG_H

typedef struct {
    double span;
    double root_chord;
    double tip_chord;
    double sweep_angle; // in degrees
    double angle_of_attack; // in degrees
    double target_static_margin; // as a fraction of chord
} WingConfig;

#endif // WING_CONFIG_H