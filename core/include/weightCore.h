#ifndef WEIGHT_CORE_H
#define WEIGHT_CORE_H

#include "missionProfile.h"

typedef struct {
    double total_weight_kg;
    double battery_weight_kg;
    double structural_weight_kg;
    double propulsion_weight_kg;
    int iterations_count;
    double* convergence_history;
} WeightResults;

double calc_power_required(double weight, double velocity, double l_d_ratio);
double calc_battery_weight(double p_required, double flight_time, double sed, double eta_total);
WeightResults iterate_gross_weight(MissionProfile profile, double initial_guess, double* history_buffer);

#endif