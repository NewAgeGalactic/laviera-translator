import wx



class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1252, 758), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # Create a panel
        panel = wx.Panel(self)

        # Create a vertical box sizer to arrange the elements
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create input and output text controls
        self.input_text_ctrl = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 300),
                                           style=wx.TE_MULTILINE)
        self.output_text_ctrl = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 300),
                                            style=wx.TE_MULTILINE)

        # Add the input and output text controls to the main sizer
        main_sizer.Add(self.input_text_ctrl, 0, wx.ALL, 5)
        main_sizer.Add(self.output_text_ctrl, 0, wx.ALL, 5)

        # Set the main sizer as the sizer for the panel
        panel.SetSizer(main_sizer)

        # Create a toolbar
        self.toolbar = wx.ToolBar(panel)
        self.toolbar.AddTool(wx.ID_ANY, "Translate", wx.Bitmap("image1.bmp", wx.BITMAP_TYPE_ANY))
        self.toolbar.Realize()

        # Bind the EVT_TOOL event to the translate_text function
        

        # Set up the sizer for the toolbar and panel
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel_sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(panel_sizer)

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

        def translate_text(self, event):
            print("cat")
            input_text = event.GetString()
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

            createoutput(translated_text, input_text)
            self.output_text_ctrl.SetValue(translated_text)


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        frame.Show(True)
        return True

translation_dict = {
    'aa': ('ays','ᔑᔑ'),
    'bb': ('bas','ʖʖ'),
    'cc': ('cas','ᓵᓵ'),
    'dd': ('das',''),
    'ee': ('eas',''),
    'ff': ('fas',''),
    'gg': ('get',''),
    'hh': ('ha',''),
    'ii': ('ey',''),
    'jj': ('ya',''),
    'kk': ('ka',''),
    'll': ('la',''),
    'nn': ('na',''),
    'oo': ('ohu',''),
    'pp': ('pa',''),
    'qq': ('que',''),
    'rr': ('re',''),
    'ss': ('su',''),
    'tt': ('za',''),
    'uu': ('ue',''),
    'vv': ('ve',''),
    'ww': ('we',''),
    'xx': ('xe',''),
    'yy': ('ye',''),
    'zz': ('da',''),
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
    'any': ('any-we','ᔑリǁ'),
    'at': ('a-tra',),
    'anyway': ('an-vick-ahwe',),
    'ability': ('aysab-vitra',),
    'are': ('',''),
    'able': ('vik',''),
    'absoloutley': ('abys-oh-letra',''),
    'aquire': ('ar-patra',''),
    'buy': ('see-whe',''),
    'bat': ('sab-tra',''),
    'back': ('sal-char',''),
    'ball': ('sa-lar',''),
    'base': ('say-char',''),
    'big': ('be-sige',''),
    'call': ('say-lah',''),
    'carry': ('say-rah-leh',''),
    'cheap': ('sena-chapu',''),
    'card': ('see-rodue',''),
    'capacity': ('setra-ve',''),
    'code': ('so-sune',''),
    'cold': ('seo-lune',''),
    'click': ('sele-sar',''),
    'child': ('sene-lehdo',''),
    'client': ('seleh-hentra',''),
    'daily': ('do-whaleh',''),
    'damage': ('dure-gamy',''),
    'miata': ('mia-tra','0-0'),
    'exc': ('sab',''),
    'ca': ('say',''),
    'ch': ('sena',''),
    'da': ('Dowh',''),
    'da': ('dure',''),
    'ehx': ('Hex',''),
    'exp': ('ha',''),
    'bso': ('scoh',''),
    'lehehwhie': ('letra',''),
    'lehoh': ('loneh',''),
    'psw': ('Hex',''),
    'tra': ('tre-na',''),
    'nsl': ('sey',''),
    'ato': ('rue',''),
    'aff': ('afas',''),
    'tho': ('tran ',''),
    'tha': ('tran',''),
    'ayleho': ('alee',''),
    'staff': ('see-tra-afas',''),
    'lat': ('letra',''),
    'thi': ('tra-ien',''),
    'ngs': ('neh-la',''),
    'ing': ('ie-neh',''),
    'is': ('i-se',''),
    'lik': ('le-hara',''),
    'to': ('tra-ohe',''),
    'wha': ('vik-eneh',''),
    'whe': ('vik-enay',''),
    'ㅁ': ('ay',"ᔑ"),
    'ㅠ': ('bs',"ʖ"),
    'ㅊ': ('see',"ᓵ"),
    'ㅇ': ('du',"⟍̅"),
    'ㄷ': ('eh',"ᒷ"),
    'ㄹ': ('fr',"⎓"),
    'ㅎ': ('ge',"˧"),
    'ㅗ': ('hn',"⍑"),
    'ㅑ': ('ie',"¦"),
    'ㅓ': ('ya',"⋮"),
    'ㅏ': ('har',"ꖌ"),
    'ㅣ': ('leh',"ꖎ"),
    'ㅡ': ('meh',"ᒲ"),
    'ㅜ': ('ne',"リ"),
    'ㅐ': ('ohe',"𝙹"),
    'ㅔ': ('pu',"!¡"),
    'ㅂ': ('cue',"ᑑ"),
    'ㄱ': ('rue',"∷"),
    'ㄴ': ('see',"ᓭ"),
    'ㅅ': ('tra',"ℸ"),
    'ㅕ': ('we',"⚍"),
    'ㅍ': ('va',"⍊"),
    'ㅈ': ('vik',"∴"),
    'ㅌ': ('xsh',"/"),
    'ㅛ': ('vi',"ǁ"),
    'ㅋ': ('cha',"⨅"),
    'Allt': ('ay-leh',''),
    'Bara': ('ohne-levi',''),
    'ehx': ('Hex',''),
    'Detta': ('trahn-iey',''),
    'En': ('ohne-eh',''),
    'fin': ('fuieneey',''),
    'Gröt': ('puoh-rueie-dugi-eh',''),
    'hitta': ('fuienehdu',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),
    # 'ehx': ('Hex',''),

    'ehx': ('Hex','')
}
# Create the GUI
app = MyApp()
app.MainLoop()