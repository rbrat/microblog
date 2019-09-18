import json
import requests
from flask_babel import _
from flask import current_app


def translate(text, source_language, dest_language):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    lang= f'{source_language}-{dest_language}' if source_language!='' else f'{dest_language}'
    r = requests.get(f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={app.config['YA_TRANSLATOR_KEY']}&text={text}&lang={lang}&options=1")
    if r.status_code != 200:
        #raise Exception(json.dumps({'text':r.status_code, 's_lang':source_language,'d_lang':dest_language }))
        #print()  
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
