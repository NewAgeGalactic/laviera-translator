def find_replacements(word, translation_dict):
    replacements = []
    for i in range(len(word) - 2):
        for j in range(i + 2, len(word) + 1):
            subword = word[i:j]
            if subword in translation_dict:
                replacements.append((subword, translation_dict[subword][0]))
    return replacements

def translate_text(input_text, translation_dict):
    # Split input text into individual words
    words = input_text.split()
    translated_words = []

    # Apply translation based on the dictionary
    for word in words:
        # Find all possible replacements for the word
        replacements = find_replacements(word.lower(), translation_dict)
        if replacements:
            translated_word = word
            # Replace each subword with its translation
            for subword, translated_subword in replacements:
                translated_word = translated_word.replace(subword, translated_subword)
            translated_words.append(translated_word)
        else:
            translated_word = ""
            for char in word:
                translated_char = translation_dict.get(char.lower(), (char, ''))[0]
                translated_word += translated_char
            translated_words.append(translated_word)

    translated_text = " ".join(translated_words)

    return translated_text

def createoutput(translated_text, input_text, translation_dict):
    output_lines = []
    lines = input_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("'"):
            word_start = line.find("'") + 1
            word_end = line.find("'", word_start)
            word = line[word_start:word_end]

            value_start = line.find("('") + 2
            value_end = line.find("', '", value_start)
            value = line[value_start:value_end]

            if word in translation_dict:
                output_lines.append(f"'{word}': ('{translation_dict[word][0]}', '{value}'),")
            else:
                output_lines.append(lines[i])
        else:
            output_lines.append(lines[i])

        i += 1

    file_path = "output.txt"
    with open(file_path, 'w') as file:
        file.write("\n".join(output_lines))

def main():
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

    # Read input text from a file
    file_path = "output3.txt"
    with open(file_path, 'r') as file:
        input_text = file.read()

    translated_text = translate_text(input_text, translation_dict)

    # Print the translated text to the console
    print(translated_text)

    # Save the translated text and input text to output file
    createoutput(translated_text, input_text, translation_dict)
if __name__ == "__main__":
    main()
