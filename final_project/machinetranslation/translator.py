import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(version=VERSION, \
authenticator=authenticator)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    if english_text is not None:
        result = language_translator.translate(\
text=english_text, model_id='en-fr').get_result()
    else:
        raise ValueError('english_text must be a string')
    text_json = json.dumps(result, indent=2)
    return text_json

def french_to_english(french_text):
    if french_text is not None:
        result = language_translator.translate(\
text=french_text, model_id='fr-en').get_result()
    else:
        raise ValueError('french_text must be a string')
    text_json = json.dumps(result, indent=2)
    return text_json
