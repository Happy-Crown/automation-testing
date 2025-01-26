import requests


def test_success_get_request():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_no_content_get_request():
    # Отправляем get запрос на несуществующий эндпоинт
    response = requests.get("https://jsonplaceholder.typicode.com/postsawdawdawd")
    assert response.status_code == 404

def test_succes_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    test_data = {
        "userId": 15,
        "title": "autotest title",
        "body": "autotest body"
    }
    response = requests.post(url, test_data)
    response_data = response.json()
    
    assert response.status_code == 201
    assert response_data['title'] == "autotest title"
    assert response_data['body'] == "autotest body"
   
def test_success_put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    request_body = {
        "id": 1,
        "title": 'footprint',
        "body": 'bar bar',
        "userId": 15
        }
    response = requests.put(url, request_body)
    resp_data = response.json()

    assert response.status_code == 200
    assert resp_data['title'] == "footprint"
    assert resp_data['body'] == "bar bar"
    
def test_negative_put_request():
    # Отправляем запрос на несуществующий id
    url = "https://jsonplaceholder.typicode.com/posts/12343"
    response = requests.put(url)

    assert response.status_code == 500
