from fastapi.testclient import TestCliente

from main import app

client = TestCliente(app)

def test_home():
    response = client.get('/')
    assert response.json() == {'Hello': 'World!!!!!'}
