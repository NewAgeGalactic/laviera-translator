import json
from googletrans import Translator

def detect_language(text):
    # Use the Google Translate API to detect the language of the input text
    translator = Translator()
    result = translator.detect(text)
    print("Detect result:", result)  # Debugging print statement
    return result.lang if result is not None else 'en'

def translate_to_english(text):
    # Use the Google Translate API to translate the text to English
    translator = Translator()
    result = translator.translate(text, src=detect_language(text), dest='en')
    return result.text

def process_input_text(input_data):
    if not input_data:
        raise ValueError("Invalid input data. The input JSON data is empty or not provided.")

    if isinstance(input_data, dict):
        # Extract words from the dictionary and join them into a string
        input_text = " ".join(input_data.keys())
    elif isinstance(input_data, str):
        # If the input is already a string, use it directly
        input_text = input_data
    else:
        raise ValueError("Invalid input data format. It should be either a dictionary or a string.")

    # Detect the language of the input text
    detected_language = detect_language(input_text)

    if detected_language != 'en':
        # Translate non-English input to English
        translated_text = translate_to_english(input_text)
    else:
        translated_text = input_text

    return detected_language, translated_text

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

    return translated_pairs

def save_to_file(translated_pairs, detected_language):
    file_path = f"output_{detected_language}.txt"
    with open(file_path, 'w') as file:
        file.write(f"Detected Language: {detected_language}\n")
        for original_word, translated_word in translated_pairs:
            file.write(f' "{original_word}": ("{translated_word}","")\n')

# Example usage:
if __name__ == "__main__":
    translation_dict = {
        # ... (existing translation dictionary remains the same)
            'b': ('bs',"ʖ"),
    'c': ('see',"ᓵ"),
    'd': ('du',"⟍̅"),
    'e': ('eh',"ᒷ"),
    'f': ('fr',"⎓"),
    'g': ('ge',"˧"),
    'h': ('hn',"⍑"),
    'i': ('ie',"¦"),
    'j': ('ya',"⋮"),
    'k': ('har',"ꖌ"),
    'l': ('leh',"ꖎ"),
    'm': ('meh',"ᒲ"),
    'n': ('ne',"リ"),
    'o': ('ohe',"𝙹"),
    'p': ('pu',"!¡"),
    'q': ('cue',"ᑑ"),
    'r': ('rue',"∷"),
    's': ('see',"ᓭ"),
    't': ('tra',"ℸ"),
    'u': ('we',"⚍"),
    'v': ('va',"⍊"),
    'w': ('vik',"∴"),
    'x': ('xsh',"/"),
    'y': ('vi',"ǁ"),
    'z': ('cha',"⨅"),
    }

    input_file_path = "input.json"  # Change this to the path of your input file

    try:
        # Read input data from the JSON file or text file
        with open(input_file_path, 'r') as input_file:
            try:
                input_data = json.load(input_file)
            except json.JSONDecodeError:
                # If the JSON decode fails, assume it's plain text
                input_data = input_file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_file_path}' not found.")
    print("Input data:", input_data)  # Debugging print statement
    # Process input text and detect the language
    detected_language, translated_text = process_input_text(input_data)

    # Translate the English input
    translated_text = translate_text(translated_text, translation_dict)
    print("Original text (not translated to English):", input_text)
    print("Detected Language:", detected_language)
    print("Translated text:", translated_text)

    # Save the output to the file with detected language in the filename
    save_to_file(translated_text, detected_language)
