def split_into_chunks(word):
    return [word[i:i+3] for i in range(0, len(word), 3)]

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        words = file.read().split()

    with open(output_file, 'w') as file:
        for word in words:
            chunks = split_into_chunks(word)
            lines = []
            current_line = ""
            for chunk in chunks:
                if len(current_line) + len(chunk) <= 6:
                    current_line += chunk + " "
                else:
                    lines.append(current_line.strip())
                    current_line = chunk + " "
            if current_line:
                lines.append(current_line.strip())
            file.write('\n'.join(lines) + '\n')

if __name__ == "__main__":
    input_filename = "input.txt"  # Replace with the path to your input file
    output_filename = "output.txt"  # Replace with the desired path for the output file

    process_file(input_filename, output_filename)
    print("Word chunks have been written to", output_filename)
