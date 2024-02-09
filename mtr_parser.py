# mtr_parser.py
def parse_mtr_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    for line in lines[2:]:  # Skip the header lines
        parts = line.split()
        if len(parts) >= 8:
            hop_info = {
                'hop': parts[0].strip('.'),
                'hostname': parts[1],
                'loss': parts[2].strip('%'),
                'sent': parts[3],
                'last': parts[4],
                'avg': parts[5],
                'best': parts[6],
                'worst': parts[7]
            }
            parsed_data.append(hop_info)

    return parsed_data
