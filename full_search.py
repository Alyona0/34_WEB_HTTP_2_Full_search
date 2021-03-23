import sys
from io import BytesIO
import requests
from PIL import Image

toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "хххххххххххххххххххххххххххххххххххх",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    print('ошибка')
json_response = response.json()

# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима (долгота и широта):
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

# Задание 1. Размеры объекта в градусной мере и передача их в параметр spn
# Координаты крайних точек топонима:
toponym_upperCorner = toponym["boundedBy"]["Envelope"]["upperCorner"]
toponym_lowerCorner = toponym["boundedBy"]["Envelope"]["lowerCorner"]
toponym_right, toponym_upp = toponym_upperCorner.split(" ")
toponym_left, toponym_low = toponym_lowerCorner.split(" ")
delta_lon = str(float(toponym_right) - float(toponym_left))
delta_lat = str(float(toponym_upp) - float(toponym_low))

# Задание 1 и 3. Передача в параметры область показа spn, и метки pt
# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([delta_lon, delta_lat]),
    "l": "map",
    "pt": ",".join([toponym_longitude, toponym_lattitude, "flag"])
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()