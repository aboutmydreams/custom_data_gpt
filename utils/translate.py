from googletrans import Translator
from langdetect import detect


def get_language_type(text) -> str:
    language = detect(text)
    print(language, text[:10 if len(text) > 10 else len(text)])
    return language

def translate(text, dest='en') -> str:
    """
    text 可以是 md 格式
    """
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text
