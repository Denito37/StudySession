from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def read_test():
    response = client.get('/Questions')
    assert response.status_code == '200'

def read_topic_test(topic:str):
    response = client.get(f'/Questions{topic}')
    assert response.status_code == '200'

def create_test():
    response = client.post('/Questions')
    assert response.status_code == '201'