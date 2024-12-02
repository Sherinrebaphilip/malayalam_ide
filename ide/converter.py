import re


def convert_to_manglish(text):
    """
    Convert Malayalam script to Manglish.
    """
    mapping = {
        "അല്ല":"alla","അ": "a", "ആ": "aa", "ഇ": "i", "ഈ": "ii", "ഉ": "u", "ഊ": "uu",
        "എ": "e", "ഏ": "ee", "ഐ": "ai", "ഒ": "o", "ഓ": "oo", "ഔ": "au",
        "ക": "k", "ഖ": "kha", "ഗ": "ga", "ഘ": "gha", "ങ": "nga",
        "ച": "cha", "ഛ": "chha", "ജ": "ja", "ഝ": "jha", "ഞ": "nya",
        "ട": "ta", "ഠ": "tha", "ഡ": "da", "ഢ": "dha", "ണ": "na",
        "ത": "tha", "ഥ": "thha", "ദ": "dha", "ധ": "dhha", "ന": "na",
        "പ": "pa", "ഫ": "pha", "ബ": "ba", "ഭ": "bha", "മ": "ma",
        "യ": "y", "ര": "ra", "ല": "la", "ല്ല":"lla", "വ": "va", "ശ": "sha",
        "ഷ": "shha", "സ": "sa", "ഹ": "ha", "ള": "lla", "ഴ": "zha",
        "റ": "ra", "ം": "m", "്": "", "ാ": "aa", "ി": "i", "ീ": "ii",
        "ു": "u", "ൂ": "uu", "ൃ": "r", "െ": "e", "േ": "ee", "ൈ": "ai",
        "ൊ": "o", "ോ": "oo", "ൗ": "au", "ൻ": "n","ൽ":"il",
    }
    return ''.join([mapping.get(char, char) for char in text])


def convert_to_malayalam(text):
    """
    Convert Manglish back to Malayalam.
    """
    reverse_mapping = {
        "അല്ല":"alla","a": "അ", "aa": "ആ", "i": "ഇ", "ii": "ഈ", "u": "ഉ", "uu": "ഊ",
        "e": "എ", "ee": "ഏ", "ai": "ഐ", "o": "ഒ", "oo": "ഓ", "au": "ഔ",
        "ka": "ക", "kha": "ഖ", "ga": "ഗ", "gha": "ഘ", "nga": "ങ","lla":"ല്ല",
        "cha": "ച", "chha": "ഛ", "ja": "ജ", "jha": "ഝ", "nya": "ഞ",
        "ta": "ട", "tha": "ഠ", "da": "ഡ", "dha": "ഢ", "na": "ണ",
        "tha": "ത", "thha": "ഥ", "dha": "ദ", "dhha": "ധ", "na": "ന",
        "pa": "പ", "pha": "ഫ", "ba": "ബ", "bha": "ഭ", "ma": "മ",
        "ya": "യ", "ra": "ര", "la": "ല", "va": "വ", "sha": "ശ",
        "shha": "ഷ", "sa": "സ", "ha": "ഹ", "la": "ള", "zha": "ഴ",
        "ra": "റ", "m": "ം", "a": "ാ", "i": "ി", "ii": "ീ", "u": "ു",
        "uu": "ൂ", "r": "ൃ", "e": "െ", "ee": "േ", "ai": "ൈ","ൽ":"il",
        "o": "ൊ", "oo": "ോ", "au": "ൗ","n":"ൻ","alla":"അല്ല"
    }

    # Process the input text
    words = text.split()
    malayalam_words = []
    for word in words:
        malayalam_word = ""
        while word:
            for key in sorted(reverse_mapping.keys(), key=len, reverse=True):
                if word.startswith(key):
                    malayalam_word += reverse_mapping[key]
                    word = word[len(key):]
                    break
            else:
                # If no match is found, add the character as-is
                malayalam_word += word[0]
                word = word[1:]
        malayalam_words.append(malayalam_word)
    return " ".join(malayalam_words)



class Converter:
    def __init__(self):
        # Mapping for Python keywords and operators
        self.python_keywords = {
            "def": "def",
            "print": "print",
            "return": "return",
            "if": "if",
            "else": "else",
            "for": "for",
            "while": "while",
            "import": "import",
            "from": "from",
            "try": "try",
            "except": "except",
            "finally": "finally",
            "break": "break",
            "continue": "continue",
            "pass": "pass",

            # Malayalam Keywords to Python
            "നിർവചിക്കുക": "def",
            "അച്ചടിക്കുക": "print",
            "ഇറക്കുമതി": "import",
            "ക്ലാസ്": "class",
            "എന്നാൽ": "if",
            "അല്ലെങ്കിൽ": "else",
            "സമയം": "while",
            "വേണ്ടി": "for",
            "ൽ": "in",
            "പരിധി": "range",
            "അഥവാ": "or",
            "ഒപ്പം": "and",
            "തെറ്റാണ്":"False",
            "ഒന്നുമില്ല":"None",
            "സത്യമാണ്":"True",
            "എന്ന":"as",
            "ഉറപ്പിക്കുക":"assert",
            "അസിങ്ക്":"assync",
            "കാത്തിരിക്കുക":"await",
            "തകർക്കുക":"break",
            "തുടരുക":"continue",
            "മാറ്റുക":"del",
            "വേറെ":"elif",
            "ഒഴികെ":"except",
            "അവസാനമായി":"finally",
            "നിന്ന്":"from",
            "ആഗോള":"global",
            "ആണ്":"is",
            "ലാംഡ":"lambda",
            "പ്രാദേശികമല്ല":"nonlocal",
            "അല്ല":"not",
            "അഥവാ":"or",
            "കടക്കുക":"pass",
            "ഉയർത്തുക":"raise",
            "മടങ്ങുക":"return",
            "ശ്രമിക്കുക":"try",
            "കൂടെ":"with",
            "ഉത്പാദനം":"yield",
            "അബ്സോല്യൂട്ട്()":"abs()",
            "എല്ലാം()":"all()",
            "ഏതെങ്കിലും()":"any()",
            "ബൈനറി()":"bin()",
            "ബൂൾ()":"bool()",
            "ബൈറ്റുകൾ()":"bytes()",
            "നിഘണ്ടു()":"dict()",
            "ഫ്ലോട്ടുകൾ()":"float()",
            "പൂർണ്ണസംഖ്യ()":"int()",
            "നീളം()":"len()",
            "പട്ടിക()":"list()",
            "പരമാവധി()":"max()",
            "കുറഞ്ഞത്()":"min()",
            "പരിധി()":"range()",
            "സജ്ജീകരിക്കുക()":"set()",
            "നാഴികക്കല്ല്()":"str()",
            "ആകെയുള്ളത്()":"sum()",
            "ട്യൂപിള്()":"tuple()",
            "സിപ്()":"zip()",
            "സ്വഭാവം()":"char()",
            "സ്ഥിരം":"Constant",
            "ഫംഗ്ഷൻ":"Function",
            "സൂചിക":"Loop",
            "സ്ഥിതി":"Condition",
            "ക്ലാസ്":"Class",
            "ഒബ്ജക്റ്റ്":"Object",
            "മൊഡ്യൂൾ":"Module",
            "ഇറക്കുമതി":"import",
            "നിഘണ്ടു":"Dictionary",
            
        }

    def translate_line(self, line):
        """
        Translates a single line of code from Malayalam to Python.
        """
        leading_spaces = len(line) - len(line.lstrip())
        indentation = line[:leading_spaces]
        content = line[leading_spaces:]

        # Split the content into tokens
        tokens = re.findall(r'\s+|".*?"|[\w\u0D00-\u0D7F]+|[^\w\s]', content)
        translated_tokens = []

        for token in tokens:
            if token.isspace():
                translated_tokens.append(token)  # Preserve spaces as is
            elif token.startswith('"') and token.endswith('"'):
                # Convert the string to Manglish
                malayalam_string = token[1:-1]
                manglish_string = convert_to_manglish(malayalam_string)
                translated_tokens.append(f'"{manglish_string}"')
            elif token in self.python_keywords:
                translated_tokens.append(self.python_keywords[token])  # Translate keywords
            else:
                translated_tokens.append(token)  # Preserve unrecognized tokens

        return indentation + ''.join(translated_tokens).strip()

    def convert_code(self, code):
        """
        Converts the entire code block from Malayalam to Python, line by line.
        """
        lines = code.splitlines()
        translated_lines = [self.translate_line(line) for line in lines]
        return "\n".join(translated_lines)


# Wrapper Function
def process_code(code):
    """
    Wrapper function to create a Converter instance and translate the given code.
    Returns the translated code.
    """
    converter = Converter()
    translated_code = converter.convert_code(code)
    return translated_code