# llm_connector.py
import requests
import json

def stream_response(prompt: str, model: str = "mistral"):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }

    try:
        with requests.post(url, json=payload, headers=headers, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line.decode('utf-8'))
                        yield chunk.get("response", "")
                    except Exception as e:
                        yield f"\n[Error: {e}]"
    except Exception as e:
        yield f"\n[Connection error: {e}]"
