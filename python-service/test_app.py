import pytest
from app import app  # Import the Flask app from your app.py

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client  # This client will be used in the test functions

def test_home(client):
    # Test the /api/python route
    response = client.get('/api/python')
    assert response.status_code == 200
    assert b"Hello from Python Service!" in response.data  # Check for the string in the response body

def test_health(client):
    # Test the /api/python/health route
    response = client.get('/api/python/health')
    assert response.status_code == 200
    assert b"Health: OK" in response.data  # Check for the health status in the response body
