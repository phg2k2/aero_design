#include <stdio.h>
#include "flyingWingCG.h"
#include "time.h"

int main() {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    double A = 300.0;
    double B = 150.0;
    double Y = 600.0;
    double S = 200.0;
    double sm = 0.1;

    // Tính toán
    double mac    = calculate_mean_aerodynamic_chord(A, B);
    double dtm    = calculate_distance_to_mac(Y, A, B);
    double sam    = calculate_sweep_at_mac(S, A, B);
    double acfrle = calculate_aerodynamic_center_from_root_leading_edge(sam, mac);
    double cgfrle = calculate_center_of_gravity_from_root_leading_edge(acfrle, sm, mac);
    double total_S = calculate_total_area(A, B, Y);
    double ar     = calculate_aspect_ratio(Y, total_S);

    end = clock();

    cpu_time_used = ((double)(end-start))/CLOCKS_PER_SEC;

    // In báo cáo chuyên nghiệp
    printf("\n=====================================================================\n");
    printf("                  FLYING WING DESIGN ANALYSIS RESULT               \n");
    printf("=====================================================================\n");
    
    // %-45s: Căn trái nhãn trong 45 khoảng trống
    // %10.2f: Căn phải giá trị trong 10 khoảng trống, lấy 2 số thập phân
    printf("%-45s | %20.4f\n", "Mean Aerodynamic Chord (MAC)", mac);
    printf("%-45s | %20.4f\n", "Distance from centerline to MAC (d)", dtm);
    printf("%-45s | %20.4f\n", "Sweep distance at MAC LE (C)", sam);
    printf("%-45s | %20.4f\n", "Aerodynamic Center from Root LE (AC)", acfrle);
    printf("%-45s | %20.4f\n", "Target Center of Gravity (CG)", cgfrle);
    printf("---------------------------------------------------------------------\n");
    printf("%-45s | %20.4f\n", "Total Wing Area (S)", total_S);
    printf("%-45s | %20.4f\n", "Aspect Ratio (AR)", ar);
    printf("---------------------------------------------------------------------\n");
    printf("%-45s | %20.8fs\n","Executed time",cpu_time_used);
    printf("=====================================================================\n");

    return 0;
}