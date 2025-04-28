import pytest
from app import app  # Import the Flask app from your app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/api/python')
    assert response.status_code == 200
    assert b"Hello from Python Service!" in response.data

def test_health(client):
    response = client.get('/api/python/health')
    assert response.status_code == 200
    assert b"All Systems Operational" in response.data  # Fixed line
