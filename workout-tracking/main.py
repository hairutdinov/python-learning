import requests
from datetime import datetime

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "a19322c7"
API_KEY = "4799559beb60c19808380b94587f0be9"

GENDER = "male"
WEIGHT = 60.0
HEIGHT = 178
AGE = 24

exercise_text = input("Tell me which exercises you did: ")

params = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

now = datetime.now()

response = requests.post(url=exercise_endpoint, headers=headers, json=params)
data = response.json()

exercises = data.get("exercises")

sheety_endpoint = "https://api.sheety.co/62ee1c8b4ba956b76a657316912f8e4e/workoutTracking/workouts"

# r = requests.get(sheety_endpoint, headers=headers)
# print(r.json())
#
# exit(0)

for exercise in exercises:
    sheety_body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_body, headers={
        "Authorization": "Bearer skikdf23984eoeajsdf9q123kl"
    })
    print(response.json())

