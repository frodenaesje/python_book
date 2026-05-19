def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for i, line in enumerate(lines, start=1):
            file.write(f"{i:3}: {line}")

if __name__ == "__main__":
    input_file = r".\ch_02\sc_02_01.py"  # Change this to your input file name
    output_file = "sc_02_01.txt"  # Change this to your desired output file name
    add_line_numbers(input_file, output_file)