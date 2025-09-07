import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Iron Lady' in response.data

def test_chatbot_greeting(client):
    response = client.post('/chatbot', json={'message': 'hello'})
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_chatbot_about(client):
    response = client.post('/chatbot', json={'message': 'what is iron lady'})
    assert response.status_code == 200
    assert b"leadership and transformation organization" in response.data

def test_chatbot_farewell(client):
    response = client.post('/chatbot', json={'message': 'bye'})
    assert response.status_code == 200
    assert b"Thank you for connecting" in response.data

def test_chatbot_unknown(client):
    response = client.post('/chatbot', json={'message': 'random question'})
    assert response.status_code == 200
    assert b"I'm happy to help but my knowledge is limited to Iron Lady" in response.data
