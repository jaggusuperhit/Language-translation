from flask import Flask, render_template, request
from langdetect import detect
from deep_translator import GoogleTranslator

app = Flask(__name__)

# List of languages supported by deep_translator
languages = {
    'en': 'english',
    'es': 'spanish',
    'fr': 'french',
    'de': 'german',
    'pt': 'portuguese',
    'hi': 'hindi',
    # Add more languages as needed
}

def detect_and_translate(text, target_lang):
    try:
        # Detect language
        result_lang = detect(text)

        # Translate text
        translator = GoogleTranslator(source=result_lang, target=target_lang)
        translated_text = translator.translate(text)

        return result_lang, translated_text
    
    except Exception as e:
        return None, str(e)


@app.route('/')
def index():
    return render_template('index.html', languages=languages)


@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""
    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']
        detected_lang, translation = detect_and_translate(text, target_lang)

    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=languages)


if __name__ == '__main__':
    app.run(debug=True)