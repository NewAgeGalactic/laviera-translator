def process_translation_dict(translation_dict):
    csharp_list = []
    for key, (value, unicode_char) in translation_dict.items():
        csharp_entry = f'{{ "{key}", "{value}" }},'
        csharp_list.append(csharp_entry)

    return csharp_list
from laviera import translation_dict

input_dict = translation_dict

def main():
   
    csharp_list = process_translation_dict(input_dict)

    with open("output.cs", "w", encoding="utf-8") as output_file:  # Specify encoding as utf-8
        output_file.write("using System.Collections.Generic;\n\n")
        output_file.write("public static class TranslationDict\n")
        output_file.write("{\n")
        output_file.write("    public static Dictionary<string, (string, string)> Translations = new Dictionary<string, (string, string)>\n")
        output_file.write("    {\n")
        for entry in csharp_list:
            output_file.write("        " + entry + "\n")
        output_file.write("    };\n")
        output_file.write("}\n")

    print("C# list has been written to 'output.cs'")



if __name__ == "__main__":
    main()
