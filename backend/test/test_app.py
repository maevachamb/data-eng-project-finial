import json


def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'message': 'Index'}
    assert expected == json.loads(res.get_data(as_text=True))

"""def test_predict_toxicity(app, client):
    del app
    response = client.get('/predict_toxicity', data="i like new york")
    assert response.status_code == 400"""