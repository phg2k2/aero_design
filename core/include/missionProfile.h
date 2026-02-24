#ifndef MISSION_PROFILE_H
#define MISSION_PROFILE_H

typedef struct {
    double v_cruise_mps;
    double flight_time_hrs;
    double payload_weight_kg;

    double energy_density_wh_per_kg;

    double eta_propulsive;
    double eta_electrical;
    double eta_motor;

    double struct_ratio;
    double prop_ratio;

    double lift_to_drag_ratio;

} MissionProfile;

#endif // MISSION_PROFILE_H