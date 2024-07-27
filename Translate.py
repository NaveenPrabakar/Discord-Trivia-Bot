from googletrans import Translator

# Initialize the translator
translator = Translator()

#all languages in the google translate API
languages = {
    "afrikaans": "af", "albanian": "sq", "amharic": "am", "arabic": "ar", "armenian": "hy",  "azerbaijani": "az",
    "basque": "eu", "belarusian": "be", "bengali": "bn", "bosnian": "bs", "bulgarian": "bg", "catalan": "ca",
    "cebuano": "ceb", "chichewa": "ny", "chinese (simplified)": "zh-cn", "chinese (traditional)": "zh-tw",
    "corsican": "co", "croatian": "hr", "czech": "cs", "danish": "da", "dutch": "nl", "english": "en",
    "esperanto": "eo", "estonian": "et", "filipino": "tl", "finnish": "fi", "french": "fr",
    "frisian": "fy", "galician": "gl", "georgian": "ka", "german": "de", "greek": "el",
    "gujarati": "gu", "haitian creole": "ht", "hausa": "ha", "hawaiian": "haw",
    "hebrew": "he", "hindi": "hi", "hmong": "hmn", "hungarian": "hu",
    "icelandic": "is", "igbo": "ig", "indonesian": "id", "irish": "ga",
    "italian": "it", "japanese": "ja", "javanese": "jw", "kannada": "kn", "kazakh": "kk", "khmer": "km",
    "kinyarwanda": "rw", "korean": "ko", "kurdish (kurmanji)": "ku", "kyrgyz": "ky",
    "lao": "lo", "latin": "la", "latvian": "lv", "lithuanian": "lt", "luxembourgish": "lb",
    "macedonian": "mk", "malagasy": "mg", "malay": "ms", "malayalam": "ml",
    "maltese": "mt", "maori": "mi", "marathi": "mr", "mongolian": "mn", "myanmar (burmese)": "my",
    "nepali": "ne", "norwegian": "no", "odia (oriya)": "or", "pashto": "ps", "persian": "fa",
    "polish": "pl", "portuguese": "pt", "punjabi": "pa", "romanian": "ro", "russian": "ru",
    "samoan": "sm", "scots gaelic": "gd", "serbian": "sr", "sesotho": "st", "shona": "sn",
    "sindhi": "sd", "sinhala": "si", "slovak": "sk", "slovenian": "sl", "somali": "so",
    "spanish": "es", "sundanese": "su", "swahili": "sw", "swedish": "sv",
    "tajik": "tg", "tamil": "ta", "tatar": "tt", "telugu": "te", "thai": "th",
    "turkish": "tr", "turkmen": "tk", "ukrainian": "uk", "urdu": "ur",
    "uyghur": "ug", "uzbek": "uz", "vietnamese": "vi", "welsh": "cy", "xhosa": "xh",
    "yiddish": "yi", "yoruba": "yo", "zulu": "zu"}


#Finds out which language the host wants to translate to
def language(choice):
    new = choice.lower()
    return languages[new]


# Translate a text
def change(question, choice):
    
    translated = translator.translate(question, src='en', dest= choice)

    return translated.text

