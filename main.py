from mtr_parser import parse_mtr_output
from data_analyzer import (calculate_average_latency, find_high_loss_hops,
                           detect_bottlenecks, calculate_rtt_fluctuations,
                           overall_network_stability, calculate_overall_average_latency)

def main():
    file_path = input("Enter the path to the MTR report file: ")
    parsed_data = parse_mtr_output(file_path)

    if not parsed_data:
        print("No data parsed. Please check the file format and path.")
        return

    # Enhanced analysis
    bottlenecks = detect_bottlenecks(parsed_data)
    fluctuations = calculate_rtt_fluctuations(parsed_data)
    stability_score = overall_network_stability(parsed_data)
    overall_avg_latency = calculate_overall_average_latency(parsed_data)  # Corrected placement

    print("\nEnhanced Analysis Results:")
    print(f"Overall Network Stability Score: {stability_score:.2f}/100")
    if bottlenecks:
        print("\nDetected Potential Bottlenecks:")
        for hop in bottlenecks:
            print(f"Hop {hop['hop']} ({hop['hostname']}) with avg latency {hop['avg']} ms")
    else:
        print("\nNo significant bottlenecks detected.")

    print("\nRTT Fluctuations (Standard Deviation):")
    for fluctuation in fluctuations:
        print(f"Hop {fluctuation['hop']}: {fluctuation['std_dev']:.2f} ms")
    
    print(f"\nOverall Average Latency: {overall_avg_latency} ms")  # Now correctly placed within main

if __name__ == "__main__":
    main()
