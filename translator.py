import tkinter as tk

import laviera
from laviera import translation_dict
    #Add more translation mappings as needed


def translate_text(event=None):  # Add event=None as a parameter to handle the event
    input_text = input_field.get("1.0", "end-1c")  # Get input text from the entry field

    # Apply translation based on the dictionary
    translated_text = ""
    words = input_text.split()
    for word in words:
        translation = translation_dict.get(word.lower(), None)
        if translation is not None:
            translated_word = translation[0]
            unicode_char = translation[1] if len(translation) > 1 else ''
            translated_text += translated_word + " " + unicode_char + " "
        else:
            for char in word:
                translated_char = translation_dict.get(char.lower(), (char, ''))[0]
                translated_text += translated_char
            translated_text += " "

    output_field.delete("1.0", "end")  # Clear the output field
    output_field.insert("1.0", translated_text.strip())  # Display the translated text in the output field
# Create the GUI
root = tk.Tk()
root.configure(width=480,height=640)
root.title("Live Translation Program")

# Input field
input_field = tk.Text(root, height=10, width=100)
input_field.pack()

# Translate button


# Output field
output_field = tk.Text(root, height=10, width=100)
output_field.pack()
input_field.bind("<KeyRelease>", translate_text)
# Run the program
root.mainloop()
