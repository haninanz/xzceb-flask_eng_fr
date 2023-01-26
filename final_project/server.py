from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    textToTranslate = textToTranslate.split()
    text_json = translator.english_to_french(textToTranslate)
    text_dict = json.loads(text_json)
    text = ' '.join([dict['translation'] for dict in text_dict['translations']])
    return text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    textToTranslate = textToTranslate.split()
    text_json = translator.french_to_english(textToTranslate)
    text_dict = json.loads(text_json)
    text = ' '.join([dict['translation'] for dict in text_dict['translations']])
    return text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
