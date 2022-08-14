import json
import requests
#from text_api_config import apikey

 
text = "Molly Moon is a cow. She is part of the United Nations' Climate Action Committee."
headers = {
    "Content-Type": "application/json",
    "apikey": "7bd760c4-fd69-4d04-9bc0-d55bf2ea6dbc"
}
body = {
    "text": text
}
url = "https://app.thetextapi.com/text/ner"
 
response = requests.post(url, headers=headers, json=body)
ner = json.loads(response.text)["ner"]
print(ner)