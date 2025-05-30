from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def read_test():
    response = client.get('/Questions')
    assert response.status_code == '200'

def read_topic_test():
    response = client.get('/Questions/algebra')
    assert response.status_code == '404'
