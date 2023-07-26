import csv

from laviera import translation_dict

def strip_dict_and_write_to_csv(dictionary, output_file):
    stripped_dict = {}
    for key, value in dictionary.items():
        stripped_value = tuple(val.strip() for val in value if val.strip())
        stripped_dict[key.strip()] = stripped_value
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value 1', 'Value 2'])  # Write header row
        for key, value in stripped_dict.items():
            writer.writerow([key] + list(value))



output_file = 'stripped_dictionary.csv'
strip_dict_and_write_to_csv(translation_dict, output_file)
print(f"Dictionary stripped and written to '{output_file}' file.")