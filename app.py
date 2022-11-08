from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField


class ConvertForm(FlaskForm):
    text = StringField('Text')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


morse_dict = {
    'a': '▄ ▄▄▄ ',
    'b': '▄▄▄ ▄ ▄ ▄ ',
    'c': '▄▄▄ ▄ ▄▄▄ ▄ ',
    'd': '▄▄▄ ▄ ▄ ',
    'e': '▄ ',
    'f': '▄ ▄ ▄▄▄ ▄ ',
    'g': '▄▄▄ ▄▄▄ ▄ ',
    'h': '▄ ▄ ▄ ▄ ',
    'i': '▄ ▄ ',
    'j': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
    'k': '▄▄▄ ▄ ▄▄▄ ',
    'l': '▄ ▄▄▄ ▄ ▄ ',
    'm': '▄▄▄ ▄▄▄ ',
    'n': '▄▄▄ ▄ ',
    'o': '▄▄▄ ▄▄▄ ▄▄▄ ',
    'p': '▄ ▄▄▄ ▄▄▄ ▄ ',
    'q': '▄▄▄ ▄▄▄ ▄ ▄▄▄ ',
    'r': '▄ ▄▄▄ ▄ ',
    's': '▄ ▄ ▄ ',
    't': '▄▄▄ ',
    'u': '▄ ▄ ▄▄▄ ',
    'v': '▄ ▄ ▄ ▄▄▄ ',
    'w': '▄ ▄▄▄ ▄▄▄ ',
    'x': '▄▄▄ ▄ ▄ ▄▄▄ ',
    'y': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ',
    'z': '▄▄▄ ▄▄▄ ▄ ▄ ',
    '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
    '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
    '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄ ',
    '4': '▄ ▄ ▄ ▄ ▄▄▄ ',
    '5': '▄ ▄ ▄ ▄ ▄ ',
    '6': '▄▄▄ ▄ ▄ ▄ ▄ ',
    '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄ ',
    '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ',
    '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ',
    '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
    ' ': '       '
}

def convert(text):
    morse_text = ''
    for letter in text:
        if letter in morse_dict:
            morse_text = morse_text + morse_dict[letter] + '   '
    print(morse_text)
    print("ok")


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/morsecode.html')
def morsecode():
    convert_form = ConvertForm()
    return render_template('morsecode.html', form=convert_form)



@app.route('/convert', methods=["POST"])
def convert():
    if request.method == "POST":
        data = request.form
        print(data["text"])
        text_to_convert = data["text"].lower()
        morse_text = """ """
        for letter in text_to_convert:
            if letter in morse_dict:
                morse_text = morse_text + morse_dict[letter] + '   '
        print(morse_text)
        form = ConvertForm()
        return render_template("morsecode.html", morse=morse_text, form=form)



if __name__ == "__main__":
    app.run(debug=True)


home()
