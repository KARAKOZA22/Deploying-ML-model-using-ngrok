import json
import requests

url = "https://1b68-35-231-174-42.ngrok-free.app/diabetes_prediction"

inputformodel = {
  "Pregnancies":9,
  "Glucose": 200,
  'BloodPressure':66,
  'SkinThickness':29,
  'Insulin':15 ,
  'BMI':26.6,
  "DiabetesPedigreeFunction":0.351,
  'Age':31

}

input_json = json.dumps(inputformodel)
response = requests.post(url, data =input_json )
print(response)
print(response.text)