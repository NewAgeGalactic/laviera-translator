import tkinter as tk

translation_dict = {
    'a': 'ay',
    'b': 'bs',
    'c': 'see',
    'd': 'du',
    'e': 'eh',
    'f': 'fr',
    'g': 'ge',
    'h': 'hn',
    'i': 'ie',
    'j': 'ya',
    'k': 'har',
    'l': 'leh',
    'm': 'meh',
    'n': 'ne',
    'o': 'ohe',
    'p': 'pu',
    'q': 'cue',
    'r': 'rue',
    's': 'see',
    't': 'tra',
    'u': 'we',
    'v': 'va',
    'w': 'vik',
    'x': 'xsh',
    'y': 'vi',
    'z': 'cha',
    'any': 'any-we',
    'at': 'a-tra',
    'anyway': 'an-vick-ahwe',
    'ability': 'aysab-vitra',
    'are': '',
    'able': 'vik',
    'absoloutley': 'abys-oh-letra',
    'aquire': 'ar-patra',
    'buy': 'see-whe',
    'bat': 'sab-tra',
    'back': 'sal-char',
    'ball': 'sa-lar',
    'base': 'say-char',
    'big': 'be-sige',
    'call': 'say-lah',
    'carry': 'say-rah-leh',
    'cheap': 'sena-chapu',
    'card': 'see-rodue',
    'capacity': 'setra-ve',
    'code': 'so-sune',
    'cold': 'seo-lune',
    'click': 'sele-sar',
    'child': 'sene-lehdo',
    'client': 'seleh-hentra',
    'daily': 'do-whaleh',
    'damage': 'dure-gamy',
    'dangerous': 'dure-neegee'
    
    
    # Add more translation mappings as needed
}

def translate_text():
    input_text = input_field.get("1.0", "end-1c")  # Get input text from the entry field

    # Apply translation based on the dictionary
    translated_text = ""
    words = input_text.split()
    for word in words:
        translated_word = translation_dict.get(word.lower(), None)
        if translated_word is not None:
            translated_text += translated_word + " "
        else:
            for char in word:
                translated_char = translation_dict.get(char.lower(), char)
                translated_text += translated_char
            translated_text += " "

    output_field.delete("1.0", "end")  # Clear the output field
    output_field.insert("1.0", translated_text.strip())  # Display the translated text in the output field
# Create the GUI
root = tk.Tk()
root.title("Live Translation Program")

# Input field
input_field = tk.Text(root, height=5, width=50)
input_field.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Output field
output_field = tk.Text(root, height=5, width=50)
output_field.pack()

# Run the program
root.mainloop()
