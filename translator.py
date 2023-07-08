import tkinter as tk

import laviera
from laviera import translation_dict
    #Add more translation mappings as needed

def find_replacements(word):
    replacements = []
    for i in range(len(word) - 2):
        for j in range(i + 2, len(word) + 2):
            subword = word[i:j]
            if subword in translation_dict:
                replacements.append((subword, translation_dict[subword][0]))
    return replacements

def createoutput(translated_text, input_field):
    file_path = "output.txt"
    with open(file_path, 'w') as file:
        file.write(translated_text + '\n' + input_field)


def translate_text(event):
    input_text = input_field.get("1.0", "end-1c")  # Get input text from the entry field

    # Split input text into individual words
    words = input_text.split()
    translated_words = []

    # Apply translation based on the dictionary
    for word in words:
        replacements = find_replacements(word.lower())
        if replacements:
            translated_word = word
            
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
    
    output_field.delete("1.0", "end")  # Clear the output field
    output_field.insert("1.0", translated_text.strip())  # Display the translated text in the output field
    createoutput(translated_text, input_text)

# Create the GUI
root = tk.Tk()
root.configure(width=480,height=640)
root.title("Laviera translator")

# Input field
input_field = tk.Text(root, height=10, width=100)
input_field.pack()


# Output field
output_field = tk.Text(root, height=10, width=100)
output_field.pack()
input_field.bind("<KeyRelease>", translate_text)
# Run the program
root.mainloop()
