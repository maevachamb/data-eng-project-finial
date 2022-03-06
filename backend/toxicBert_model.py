from detoxify import Detoxify

#To load the model
def load_model(model_name):
    return Detoxify(model_name)

def predict_text_toxicity(model, text):
    # This function do toxicity prediction on a text and return the toxicity.
    # if ((text == '') or (text == 'None') ):
    #     toxicity = 'empty ! Try again'
    # else:
    
    d = model.predict(text)
    keys_values = d.items()
    for key, value in keys_values:
    	d[key] = round(value, 2)
    toxicity = {str(key): str(value) for key, value in keys_values}
        
    return {"text": text, "results": toxicity}
