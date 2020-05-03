import requests
def stock():
    id_clothe = "13890859"
    # id_clothe = "13890827"
    url = "https://asos2.p.rapidapi.com/products/v3/detail"
    params = {"id":id_clothe, "store":"RU", "lang":"ru-RU"}
    headers = {
        'x-rapidapi-host': "asos2.p.rapidapi.com",
        'x-rapidapi-key': "416e441340msh0635d590fcc1199p1c2df8jsnde8bc34ad1f3"
        }
    response = requests.get(url, headers=headers, params=params).json()["isInStock"]
    return response
