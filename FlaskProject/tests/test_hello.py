import pytest
from flaskr.hello import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_welcome_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to our home page." in response.data

def test_hello_empty(client):
    response = client.get('/hello/')
    assert response.status_code == 200

def test_hello_me(client):
    response = client.get('/hello/me')
    assert response.status_code == 200

def test_hello_me_slash_you(client):
    response = client.get('/hello/me/you')
    assert response.status_code == 404

def test_user_empty(client):
    response = client.get('/user')
    assert response.status_code == 404

def test_user_me(client):
    response = client.get('/user/me')
    assert response.status_code == 200
    assert b"Logged as me" in response.data

def test_int_display_0(client):
    response = client.get('/int_display/0')
    assert response.status_code == 200
    assert b"Parameter : 0" in response.data

def test_projects(client):
    response = client.get('/projects/')
    assert response.status_code == 200
    assert b"The project page" in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"The about page" in response.data

def test_redirect(client):
    response = client.get("/redirect", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/logout"

def test_logout(client):
    response = client.get("/logout")
    assert response.status_code == 401