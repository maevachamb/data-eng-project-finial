from flask import Flask, request, render_template
from detoxify import Detoxify
from langdetect import detect

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # get the text from the form
    sentence = request.form['user_text'].lower()

    if detect(sentence) == 'en':
        sa = Detoxify()
        dd = sa.predict(text=sentence)

        tox = round(dd['toxicity'], 2)
        sev_tox = round(dd['severe_toxicity'], 2)
        obs = round(dd['obscene'], 2)
        thr = round(dd['threat'], 2)
        ins= round(dd['insult'], 2)
        att = round(dd['identity_attack'], 2)

        return render_template('index.html', score=[tox, sev_tox, obs, thr, ins, att], text=sentence)
    else:
        error = 'The text need to be in english!'
        return render_template('index.html', error)

    

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)