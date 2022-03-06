from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from toxicBert_model import load_model, predict_text_toxicity
from langdetect import detect

app = Flask(__name__)
CORS(app,  support_credentials=True)

model = load_model('original')

@app.route('/')
def index():
    return jsonify({'message': 'Index'})


@app.route('/predict_toxicity',methods=['GET'])
@cross_origin(supports_credentials=True)
def predict_toxicity():
    # This function take the text from the user, do the prediction and return the toxicity.
    global model
    user_text = str(request.args["user_text"])
    return jsonify(predict_text_toxicity(model, user_text))

    #To detect if text is in english
"""if detect(user_text) == 'en':
        return jsonify(predict_text_toxicity(model, user_text))
    
    else:
        error = {'text':user_text, 'results':'The text need to be in english!'}
        return jsonify(error)"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000",debug=False)
