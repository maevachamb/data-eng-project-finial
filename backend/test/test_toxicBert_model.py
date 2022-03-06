import pytest
from detoxify import Detoxify
import toxicBert_model


def test_predict_text_toxicity():
    assert toxicBert_model.predict_text_toxicity(Detoxify('original'), 'i like new york') == {'text': 'i like new york', 'results': {'toxicity': '0.0', 'severe_toxicity': '0.0', 'obscene': '0.0', 'threat': '0.0', 'insult': '0.0', 'identity_attack': '0.0'}}
    assert toxicBert_model.predict_text_toxicity(Detoxify('unbiased'), 'i like new york') == {'text': 'i like new york', 'results': {'toxicity': '0.03', 'severe_toxicity': '0.0', 'obscene': '0.0', 'identity_attack': '0.01','insult': '0.01', 'threat': '0.0',  'sexual_explicit': '0.0'}}
    assert toxicBert_model.predict_text_toxicity(Detoxify('original'), 'you are such a dork') == {'text': 'you are such a dork', 'results': {'toxicity': '0.97', 'severe_toxicity': '0.02', 'obscene': '0.58', 'threat': '0.0', 'insult': '0.91', 'identity_attack': '0.01'}}