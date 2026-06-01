from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def proxy():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        # 외부 통신이 뚫려있으므로 실시간으로 chess.com을 가져옵니다.
        response = requests.get("https://www.chess.com", headers=headers, timeout=10)
        return response.text
    except Exception as e:
        return str(e), 500
