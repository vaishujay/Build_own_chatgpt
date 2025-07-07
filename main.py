import requests 
import json

def querry_ollama(prompt, model= "phi3"):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 1000
    }
    
    response = requests.post(url, json = data, headers=headers, stream=True)
    response.raise_for_status()  # Raise an error for bad responses
    full_response = ""
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            full_response += chunk.get("response", "")
            if chunk.get("done", False):
                break
    return full_response

answer = querry_ollama("Just give me the name of the capital of India?")
print("Ollama's answer:", answer)