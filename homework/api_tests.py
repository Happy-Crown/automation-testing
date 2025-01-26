import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture
def unsupported_url():
    return "https://jsonplaceholder.typicode.com/posts/12345678"


def test_success_get_request(base_url):
    response = requests.get(base_url)
    resp_data = response.json()
    assert response.status_code == 200
    assert "title" in resp_data[0]
    assert "body" in resp_data[0]

def test_no_content_get_request(unsupported_url):
    # Отправляем get запрос на несуществующий эндпоинт
    response = requests.get(unsupported_url)
    assert response.status_code == 404

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_request_with_ids(base_url, post_id):
    response = requests.get(f"{base_url}/{post_id}")
    assert response.status_code == 200
    assert "id" in response.json()

def test_succes_post_request(base_url):
    test_data = {
        "userId": 15,
        "title": "autotest title",
        "body": "autotest body"
    }
    response = requests.post(base_url, test_data)
    response_data = response.json()
    
    assert response.status_code == 201
    assert response_data['title'] == "autotest title"
    assert response_data['body'] == "autotest body"
   
def test_success_put_request(base_url):
    request_body = {
        "id": 1,
        "title": 'footprint',
        "body": 'bar bar',
        "userId": 15
        }
    response = requests.put(f"{base_url}/1", request_body)
    resp_data = response.json()

    assert response.status_code == 200
    assert resp_data['title'] == "footprint"
    assert resp_data['body'] == "bar bar"
    
def test_negative_put_request(unsupported_url):
    # Отправляем запрос на несуществующий id
    response = requests.put(unsupported_url)

    assert response.status_code == 500

def test_delete_request(base_url):
    response = requests.delete(f"{base_url}/1")
    assert response.status_code == 200