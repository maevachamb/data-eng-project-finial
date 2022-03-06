from detoxify import Detoxify

#To load the model
def load_model(model_name):
    return Detoxify(model_name)

def predict_text_toxicity(model, text):
    d = model.predict(text)
    keys_values = d.items()
    
    for key, value in keys_values:
        d[key] = round(value, 2)
    
    toxicity = {str(key): str(value) for key, value in keys_values}
        
    return {"text": text, "results": toxicity}