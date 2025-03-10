from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_cities_spain():
    response = client.get('/countries/Spain')
    assert response.status_code == 200
    assert response.json() == ["Madrid", "Barcelona"]