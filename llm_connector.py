import os
from dotenv import load_dotenv
import requests
load_dotenv()

def stream_response(prompt: str):
    url = os.getenv("API_URL")
    model = os.getenv("MODEL", "mistral")

    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    response = requests.post(url, json=payload, headers=headers, stream=True)
    if response.status_code == 200:
        for chunk in response.iter_lines():
            if chunk:
                yield chunk.decode("utf-8")
    else:
        raise Exception(f"Error: {response.status_code}")
