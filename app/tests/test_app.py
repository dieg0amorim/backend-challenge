import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_validate_jwt_valid(client):
    valid_token = "valid_token_example"
    response = client.post('/validate', json={"token": valid_token})
    assert response.status_code == 200
    assert response.json['valid'] is True

def test_validate_jwt_invalid(client):
    invalid_token = "invalid_token_example"
    response = client.post('/validate', json={"token": invalid_token})
    assert response.status_code == 200
    assert response.json['valid'] is False

def test_missing_token(client):
    response = client.post('/validate', json={})
    assert response.status_code == 400
    assert response.json['error'] == "Token is missing"