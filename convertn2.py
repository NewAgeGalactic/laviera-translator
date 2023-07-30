def read_input_file(input_file):
    data_list = []
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                nn = line.replace("'", r"\'")  # Escape single quotes in the word
                data_list.append(f"'{nn}': ('', ''),")
    return data_list

def save_output_file(output_file, data_list):
    with open(output_file, 'w') as file:
        for item in data_list:
            file.write(item + '\n')

def main(input_file, output_file):
    data_list = read_input_file(input_file)
    save_output_file(output_file, data_list)

if __name__ == "__main__":
    input_file_path = "output.txt"  # Change this to the path of your input file
    output_file_path = "output2.txt"  # Change this to the path where you want to save the output
    main(input_file_path, output_file_path)
