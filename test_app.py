import pytest
from main01 import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'TenshI' in response.data  # Check if title is in the response

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Service 0' in response.data  # Check if the menu is in the response

def test_contacts(client):
    response = client.get('/contacts')
    assert response.status_code == 200
    assert b'TenshI' in response.data


