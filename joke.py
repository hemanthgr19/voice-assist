import requests

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

ar = [" "," "]
ar[0]= json_data["setup"]
ar[1]= json_data["punchline"]

def joke():
    return ar


