import pytest
import requests
from api_tests import base_url

@pytest.mark.parametrize("post_id, status_code",[
    (1, 200),
    (15, 200),
    (25, 200)
])
def test_parametrize_get_requests(base_url, post_id, status_code):
    response = requests.get(f"{base_url}/{post_id}")
    assert response.status_code == status_code
    assert "id", "title" in response.json()

@pytest.mark.parametrize("post_id, status_code", [
    (1231312, 404),
    ("testststst", 404)
])
def test_negative_get_requests(base_url, post_id, status_code):
    response = requests.get(f"{base_url}/{post_id}")
    assert response.status_code == status_code

@pytest.mark.parametrize("test_data",[
    {"userId": "11", "title": "test 11", "body": "test 11. test 11"},
    {},
    {"body": "test 12. test 12"},
    {"title": "test123"},
    {"userId": "1"}
])
def test_parametrize_post_requests(base_url, test_data):
    response = requests.post(base_url, test_data)
    assert response.status_code == 201
    for key in test_data:
        assert response.json()[key] == test_data[key]

@pytest.mark.parametrize("post_id, status_code", [
    (1, 200),
    (10, 200),
    (12312312313, 200)
])
def test_parametrize_delete_requests(base_url, post_id, status_code):
    response = requests.delete(f"{base_url}/{post_id}")
    assert response.status_code == status_code

@pytest.mark.parametrize("post_id, status_code", {
    (0, 500),
    (433434343, 500)
})
def test_negative_put_requests(base_url, post_id, status_code):
    response = requests.put(f"{base_url}/{post_id}")
    assert response.status_code == status_code