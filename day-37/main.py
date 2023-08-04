import requests
from datetime import datetime

USERNAME = "bulat"
TOKEN = "nhyNDfKqVKY3MEyojmc"
GRAPH_ID = "graph1"

user_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)

today = datetime.now()

pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.10",
}

graph1_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# response = requests.post(url=graph1_endpoint, headers=graph_headers, json=pixel_creation_config)
# print(response.text)

# response = requests.get(f"{graph1_endpoint}/20230613", headers=graph_headers)
# print(response.json())


# response = requests.put(f"{graph1_endpoint}/20230613", headers=graph_headers, json={
#     "quantity": "9.05"
# })
# print(response.json())

# response = requests.delete(f"{graph1_endpoint}/20230613", headers=graph_headers)
# print(response.text)
