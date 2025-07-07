# import requests
# import json

# def  callOLLAMA(user_message):
#         url = "http://localhost:11434/api/generate"
#         payload = {
#             "model": "phi3",
#             "prompt": user_message,
#             "stream": False
#         }
#         response = requests.post(
#             url, 
#             headers={"Content-Type": "application/json"},
#             data = json.dumps(payload),
#             timeout =120
#         )
#         if response.status_code == 200:
#             result = response.json()
#             bot_response = result.get("response", "Sorry I am unable to process your request.")
#             return bot_response.strip()
    

import requests
import json

def callOLLAMA(user_message):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3",
        "prompt": user_message,
        "stream": False
    }
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=120
        )
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I am unable to process your request.")
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
