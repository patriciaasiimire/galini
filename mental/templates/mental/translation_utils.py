# translation_utils.py
from google.cloud import translate_v2 as translate
from google.api_core.exceptions import GoogleAPIError
import os

def translate_text(text, target_language):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c\credentials.json'
    client = translate.Client()
    result = client.translate(text, target_language=target_language)
    return result['translatedText']