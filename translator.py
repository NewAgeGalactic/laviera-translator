import tkinter as tk
from laviera_dict import translation_dict


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
    for word in words: # get the input text
        # Find all possible replacements for the word
        replacements = find_replacements(word.lower())
        if replacements:  # if there are any replacements
            translated_word = word # use the original word
            # Replace each subword with its translation
            
            for subword, translated_subword in replacements: # get the word in subword
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
def open_help():
    print()

root = tk.Tk()
root.configure(width=480,height=640)
root.title("Laviera translator")
info = tk.Label(text="welcome to the official laviera translator!")
info.pack()
# Input field
input_field = tk.Text(root, height=10, width=100)
input_field.pack()
button = tk.Button(
    text="Click me!",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=open_help()   
)
button.pack()
button1 = tk.Button(
    text="Click me!",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=open_help()
)
button1.pack()


# Output field
output_field = tk.Text(root, height=10, width=100)
output_field.pack()
input_field.bind("<KeyRelease>", translate_text)

input_field.configure(bg='lightblue')
output_field.configure(bg="green")

# Run the program
root.mainloop()
