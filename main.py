from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abdulvaliy'

# Creating Morse Code application
morse_dictionary = {
    '·−': 'a', '−···': 'b', '−·−·': 'c', '−··': 'd', '·': 'e', '··−·': 'f', '−−·': 'g', '····': 'h',
    '··': 'i', '·−−−': 'j', '−·−': 'k', '·−··': 'l', '−−': 'm', '−·': 'n', '−−−': 'o', '·−−·': 'p',
    '−−·−': 'q', '·−·': 'r', '···': 's', '−': 't', '··−': 'u', '···−': 'v', '·−−': 'w', '−··−': 'x',
    '−·−−': 'y', '−−··': 'z', '': ' ', '−−··−−': ',', '·−·−·−': '.',
    '·−−−−': '1', '··−−−': '2', '···−−': '3', '····−': '4', '·····': '5',
    '−····': '6', '−−···': '7', '−−−··': '8', '−−−−·': '9', '−−−−−': '0'
}

letters = {'a': '·−', 'b': '−···', 'c': '−·−·', 'd': '−··', 'e': '·', 'f': '··−·', 'g': '−−·', 'h': '····',
          'i': '··', 'j': '·−−−', 'k': '−·−', 'l': '·−··', 'm': '−−', 'n': '−·', 'o': '−−−', 'p': '·−−·',
          'q': '−−·−', 'r': '·−·', 's': '···', 't': '−', 'u': '··−', 'v': '···−', 'w': '·−−', 'x': '−··−',
          'y': '−·−−', 'z': '−−··', ' ': ' ', ',': '−−··−−', '.': '·−·−·−', '1': '·−−−−', '2': '··−−−', '3': '···−−',
          '4': '····−', '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·', '0': '−−−−−'}


# ################## morse to sentence ##################



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/morse_translate', methods=['POST'])
def sentence_translate():
    sentence_list = request.form['text1'].lower()
    new_morse_code = ''
    for letter in list(sentence_list):
        new_morse_code += f'{letters[letter]} '
    return render_template('index.html', text1=request.form['text1'], text2=new_morse_code)


@app.route('/translate-to-sentence', methods=['POST'])
def morse_translate():
    user_list = request.form['text3'].split(' ')
    new_sentence = ''
    for morse in user_list:
        new_sentence += morse_dictionary[morse]
    return render_template('index.html', text3=request.form['text3'], text4=new_sentence)


if __name__ == "__main__":
    app.run(debug=True)
