import json
from laviera import translation_dict
def find_replacements(word, translation_dict):
    replacements = []
    for i in range(len(word) - 2):
        for j in range(i + 2, len(word) + 2):
            subword = word[i:j]
            if subword in translation_dict:
                replacements.append((subword, translation_dict[subword][0]))
    return replacements

def translate_text(input_text, translation_dict):
    # Split input text into individual words
    words = input_text.split()
    translated_pairs = []

    # Apply translation based on the dictionary
    for word in words:
        # Find all possible replacements for the word
        replacements = find_replacements(word.lower(), translation_dict)
        if replacements:
            translated_word = word
            # Replace each subword with its translation
            for subword, translated_subword in replacements:
                translated_word = translated_word.replace(subword, translated_subword)
            translated_pairs.append((word, translated_word))
        else:
            translated_word = ""
            for char in word:
                translated_char = translation_dict.get(char.lower(), (char, ''))[0]
                translated_word += translated_char
            translated_pairs.append((word, translated_word))
    print(translated_pairs)
    return translated_pairs
        

def save_to_file(translated_pairs):
    file_path = "output.txt"
    with open(file_path, 'w') as file:
        for original_word, translated_word in translated_pairs:
           file.write(f' "{original_word}": ("{translated_word}",""),\n')

def process_text_file(input_file_path, translation_dict):
    with open(input_file_path, 'r') as input_file:
        input_text = input_file.read()
        translated_pairs = translate_text(input_text, translation_dict)
        save_to_file(translated_pairs)

def process_json_file(input_file_path, translation_dict):
    with open(input_file_path, 'r') as input_file:
        input_data = json.load(input_file)
        input_text = " ".join(input_data.keys())
        translated_pairs = translate_text(input_text, translation_dict)
        save_to_file(translated_pairs)

# Example usage:
if __name__ == "__main__":

    input_file_path = "input.json"  # Change to your input file path
    if input_file_path.endswith('.json'):
        process_json_file(input_file_path, translation_dict)
    else:
        process_text_file(input_file_path, translation_dict)
        
