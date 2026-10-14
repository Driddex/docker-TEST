import requests
import os

BASE_URI = os.environ.get('BASE_URI', 'http://127.0.0.1:5000')
target_url = f"{BASE_URI}/p"

print("Отправка тестового запроса на бэкенд...")

try:
    post_method = requests.post(target_url, json={
        "id": 1
    })
    
    print("Статус-код ответа:", post_method.status_code)
    print("Данные от сервера:", post_method.json())

except Exception as e:
    print(f"Ошибка подключения: {e}")