import json
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

def save_to_file(translated_pairs):
    file_path = "output.txt"
    with open(file_path, 'w') as file:
        for original_word, translated_word in translated_pairs:
            file.write(f'"{original_word}": "{translated_word}",\n')


# Example usage:
if __name__ == "__main__":
    translation_dict = {
    'a': ('ay',"ᔑ"),
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

    # Read input text from the JSON file
    input_file_path = "input.json"
    with open(input_file_path, 'r') as input_file:
        input_data = json.load(input_file)

    input_text = " ".join(input_data.keys())
    translated_text = translate_text(input_text, translation_dict)
    print("Original text:", input_text)
    print("Translated text:", translated_text)

    save_to_file(translated_text)
