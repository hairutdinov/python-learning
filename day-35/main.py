import requests

# api_key = "9be796238c40e67ba4149de8c07dff09"
# api_endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
#
# api_params = {
#     "lat": 54.900650,
#     "lon": 52.296280,
#     "appid": api_key,
#     # "exclude": ",".join([
#     #     'current',
#     #     'minutely',
#     #     'daily',
#     #     'alerts',
#     # ])
# }
#
# response = requests.get(api_endpoint, params=api_params)
# print(response.json())

import os
print(os.environ.get("PWD"))