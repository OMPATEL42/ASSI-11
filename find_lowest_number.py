import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

number_found = False
lowest_number = None

with open(input_filename, 'r') as input_file:
    for line in input_file:
        try:
            number = float(line.strip())
            if not number_found:
                lowest_number = number
                number_found = True
            elif number < lowest_number:
                lowest_number = number
        except ValueError:
            continue

with open(output_filename, 'w') as output_file:
    if number_found:
        output_file.write(f"{lowest_number:.10g}\n")
    else:
        output_file.write("No numbers found in file\n")
