using HelpWindows;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Windows;
using System.Windows.Controls;

namespace LavieraTranslator
{
    public partial class MainWindow : Window
    {
        private Dictionary<string, string> translationDict = new Dictionary<string, string>
        {
            // Define your translation dictionary here
             { "aa", "ays" },
        { "bb", "bas" },
        { "cc", "cas" },
        { "dd", "das" },
        { "ee", "eas" },
        { "ff", "fas" },
        { "gg", "get" },
        { "hh", "ha" },
        { "ii", "ey" },
        { "jj", "ya" },
        { "kk", "ka" },
        { "ll", "la" },
        { "nn", "na" },
        { "oo", "ohu" },
        { "pp", "pa" },
        { "qq", "que" },
        { "rr", "re" },
        { "ss", "su" },
        { "tt", "za" },
        { "uu", "ue" },
        { "vv", "ve" },
        { "ww", "we" },
        { "xx", "xe" },
        { "yy", "ye" },
        { "zz", "da" },
        { "a", "ay" },
        { "b", "bs" },
        { "c", "see" },
        { "d", "du" },
        { "e", "eh" },
        { "f", "fr" },
        { "g", "ge" },
        { "h", "hn" },
        { "i", "ie" },
        { "j", "ya" },
        { "k", "har" },
        { "l", "leh" },
        { "m", "meh" },
        { "n", "ne" },
        { "o", "ohe" },
        { "p", "pu" },
        { "q", "cue" },
        { "r", "reh" },
        { "s", "see" },
        { "t", "ra" },
        { "u", "we" },
        { "v", "va" },
        { "w", "vik" },
        { "x", "xsh" },
        { "y", "vi" },
        { "z", "cha" },
        { "any", "any-we" },
        { "at", "a-tra" },
        { "anyway", "an-vick-ahwe" },
        { "ability", "aysab-vitra" },
        { "are", "" },
        { "able", "vik" },
        { "absoloutley", "abys-oh-letra" },
        { "aquire", "ar-patra" },
        { "buy", "see-whe" },
        { "bat", "sab-tra" },
        { "back", "sal-char" },
        { "ball", "sa-lar" },
        { "base", "say-char" },
        { "big", "be-sige" },
        { "call", "say-lah" },
        { "carry", "say-rah-leh" },
        { "cheap", "sena-chapu" },
        { "card", "see-rodue" },
        { "capacity", "setra-ve" },
        { "code", "so-sune" },
        { "cold", "seo-lune" },
        { "click", "sele-sar" },
        { "child", "sene-lehdo" },
        { "client", "seleh-hentra" },
        { "daily", "do-whaleh" },
        { "damage", "dure-gamy" },
        { "miata", "mia-tra" },
        { "exc", "sab" },
        { "ca", "say-" },
        { "ch", "sena-" },
        { "da", "dure-" },
        { "ehx", "Hex" },
        { "exp", "ha-" },
        { "bso", "scoh-" },
        { "lehehwhie", "letra-" },
        { "lehoh", "loneh-" },
        { "psw", "Hex-" },
        { "tra", "rea-na" },
        { "nsl", "sey-" },
        { "ato", "rue-" },
        { "aff", "afas-" },
        { "tho", "reanohe-" },
        { "tha", "reah-" },
        { "ayleho", "alee-" },
        { "staff", "see-tra-afas" },
        { "lat", "letra-" },
        { "thi", "reahneh" },
        { "ngs", "neh-la" },
        { "ing", "ie-neh" },
        { "is", "i-se" },
        { "lik", "le-hara" },
        { "to", "traoh" },
        { "wha", "vik-eneh-" },
        { "whe", "vik-enay-" },
        { "ㅁ", "ay" },
        { "ㅠ", "bs" },
        { "ㅊ", "see" },
        { "ㅇ", "du" },
        { "ㄷ", "eh" },
        { "ㄹ", "fr" },
        { "ㅎ", "ge" },
        { "ㅗ", "hn" },
        { "ㅑ", "ie" },
        { "ㅓ", "ya" },
        { "ㅏ", "har" },
        { "ㅣ", "leh" },
        { "ㅡ", "meh" },
        { "ㅜ", "ne" },
        { "ㅐ", "ohe" },
        { "ㅔ", "pu" },
        { "ㅂ", "cue" },
        { "ㄱ", "rue" },
        { "ㄴ", "see" },
        { "ㅅ", "tra" },
        { "ㅕ", "we" },
        { "ㅍ", "va" },
        { "ㅈ", "vik" },
        { "ㅌ", "xsh" },
        { "ㅛ", "vi" },
        { "ㅋ", "cha" },
        { "Allt", "ay-leh" },
        { "Bara", "ohne-levi" },
        { "Detta", "trahn-iey" },
        { "En", "ohne-eh" },
        { "fin", "fuieneey" },
        { "Gröt", "puoh-rueie-dugi-eh" },
        { "hitta", "fuienehdu" },
        { "when", "vihnehne" },
        { "ught", "uegehntra" },
        { "that", "trahnaytra" },
        { "this", "trahniesee" },
        { "was", "viaysee" },
        { "pos", "puohsee" },
        { "sible", "seeiebuleheh" },
        { "ng", "nehge" },
        { "dec", "duehsee" },
        { "ided", "ieduehdu" },
        { "make", "mehay" },
        { "pro", "purueohe-" },
        { "gram", "gerueaymeh" },
        { "would", "viohuelehdu" },
        { "help", "hnehlehpu" },
        { "me", "meeh" },
        { "with", "vietrahn" },
        { "my", "mehwi" },
        { "stu", "seetraue-" },
        { "dies.", "duieehsee" },
        { "ma", "mehay" },
        { "de", "dueh" },
            // Add more translations as needed
        };

        public MainWindow()
        {

        }

        private List<Tuple<string, string>> FindReplacements(string word)
        {
            List<Tuple<string, string>> replacements = new List<Tuple<string, string>>();
            for (int i = 0; i < word.Length - 1; i++)
            {
                for (int j = i + 2; j <= word.Length; j++)
                {
                    string subword = word.Substring(i, j - i);
                    if (translationDict.ContainsKey(subword))
                    {
                        replacements.Add(new Tuple<string, string>(subword, translationDict[subword]));
                    }
                }
            }
            return replacements;
        }

        private void CreateOutput(string translatedText, string inputFieldText)
        {
            string filePath = "output.txt";
            using (StreamWriter file = new StreamWriter(filePath))
            {
                file.WriteLine(translatedText);
                file.WriteLine(inputFieldText);
            }
        }

        private void TranslateText(object sender, TextChangedEventArgs e)
        {
            string inputText = inputField.Text;

            // Split input text into individual words
            string[] words = inputText.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            List<string> translatedWords = new List<string>();

            // Apply translation based on the dictionary
            foreach (string word in words)
            {
                // Find all possible replacements for the word
                List<Tuple<string, string>> replacements = FindReplacements(word.ToLower());

                if (replacements.Count > 0)
                {
                    string translatedWord = word;

                    // Replace each subword with its translation
                    foreach (var replacement in replacements)
                    {
                        translatedWord = translatedWord.Replace(replacement.Item1, replacement.Item2);
                    }
                    translatedWords.Add(translatedWord);
                }
                else
                {
                    StringBuilder translatedWord = new StringBuilder();
                    foreach (char c in word)
                    {
                        string translatedChar = translationDict.TryGetValue(c.ToString().ToLower(), out string value)
                            ? value
                            : c.ToString();
                        translatedWord.Append(translatedChar);
                    }
                    translatedWords.Add(translatedWord.ToString());
                }
            }

            string translatedText = string.Join(" ", translatedWords);

            outputField.Text = translatedText;
            CreateOutput(translatedText, inputText);
            Console.WriteLine(translatedText);
        }
        private void OnHelpButtonClick(object sender, RoutedEventArgs e)
        {
            // Read the .md file and display its contents in the HelpWindow
            string helpFilePath = "help.md"; // Replace this with your actual file path
            string helpContent = File.ReadAllText(helpFilePath);

            HelpWindow helpWindow = new HelpWindow(helpContent);
            helpWindow.ShowDialog();
        }

        private void OnsettingsButtonClick(object sender, RoutedEventArgs e)
        {

        }
        private void OncontroClick(object sender, RoutedEventArgs e)
        {
            string helpFilePath = "controbutions.md"; // Replace this with your actual file path
            string helpContent = File.ReadAllText(helpFilePath);

            HelpWindow helpWindow = new HelpWindow(helpContent);
            helpWindow.ShowDialog();
        }
    }
        
}
