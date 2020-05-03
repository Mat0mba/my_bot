# import googlemaps
# def geocode(location):
#     gmaps = googlemaps.Client(key='AIzaSyDUlMecAStMAhWnzRTu55Cjsk-cGlgVc5U')
#     # Получаем геокод места
#     geocode_result = gmaps.geocode(location)[0]
#     lat = geocode_result["geometry"]["location"]["lat"]
#     lng = geocode_result["geometry"]["location"]["lng"]
#     return [lat, lng]
import requests
from bs4 import BeautifulSoup
def location_city(city):
    URL = "https://yandex.ru/maps/202/new-york/search/"
    headers = {"user-agent": "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)"}
    session = requests.session()
    response = session.get(URL + city, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")
    location = soup.find("div", class_="clipboard__action-wrapper _inline").next_element.split(", ")
    lat = location[0]
    lng = location[1]
    return [lat, lng]

