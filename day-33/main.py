import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data.get("iss_position"))

parameters = {
    "lat": 54.900650,
    "lng": 52.296280,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
print(response.json())