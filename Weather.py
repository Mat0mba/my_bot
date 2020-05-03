import requests
# from GeoCodeGoogle import geocode
from GeoCodeGoogle import location_city
def temp(city):
    code = location_city(city)
    headers = {"X-Yandex-API-Key": "49a3677f-d067-48a6-9d25-1b6a6f035daa"}
    response = requests.get(f"https://api.weather.yandex.ru/v1/forecast?lat={code[0]}3&lon={code[1]}&extra=false", headers=headers).json()
    temperature = response["fact"]["temp"]
    feels_like = response["fact"]["feels_like"]
    condition = response["fact"]["condition"]
    return [temperature, feels_like, condition]
