import requests

url = "http://127.0.0.1:8000/submit_json"
data = {
    "username": "John",
    "age": 30
}

response = requests.post(url, json=data)
print(response.json())  # 응답 출력
