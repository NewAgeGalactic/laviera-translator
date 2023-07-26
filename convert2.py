def split_into_chunks(word):
    return [word[i:i+3] for i in range(0, len(word), 3)]

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        words = file.read().split()

    with open(output_file, 'w') as file:
        for word in words:
            chunks = split_into_chunks(word)
            file.write(' '.join(chunks) + '\n')

if __name__ == "__main__":
    input_filename = "input.txt"  # Replace with the path to your input file
    output_filename = "output.txt"  # Replace with the desired path for the output file

    process_file(input_filename, output_filename)
    print("Word chunks have been written to", output_filename)
