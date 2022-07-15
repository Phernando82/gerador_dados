from random import uniform
from geopy import Nominatim
from shapely.geometry import Polygon, Point


class endereco_completo:
    def __init__(self, address, city, state, country, code, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.code = code
        self.zipcode = zipcode


def gera_endereco():
    while True:
        lat = float(format(uniform(-33.6328, 5.2616), '.4f'))
        lon = float(format(uniform(-73.9800, -34.7932), '.4f'))
        cidade = (lat, lon)
        brasil = [(-8.046177, -34.584961),
                  (-20.784877, -40.737305),
                  (-33.713374, -53.481445),
                  (-30.285635, -57.612305),
                  (-16.370743, -60.249023),
                  (-7.436552, -73.696289),
                  (4.403373, -64.907227),
                  (4.228090, -51.547852)]
        ponto = Point(cidade)
        poligono = Polygon(brasil)
        if poligono.contains(ponto):
            Latitude = str(lat)
            Longitude = str(lon)
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.reverse(Latitude + "," + Longitude)
            # print(location)
            address = location.raw['address']
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
            code = address.get('country_code')
            zipcode = address.get('postcode')
            endereco = endereco_completo(address, city, state, country, code, zipcode)
            return endereco


saida = gera_endereco()
# print(saida.address)
# print(saida.city)
# print(saida.state)
# print(saida.country)
# print(saida.code)
# print(saida.zipcode)
# coordenadas dos extremos:

# NORTE latitude: 5.2616 longitude: -602114
# SUL latitude: -33.6328 longitude: -53.3594
# OESTE latitude: -7.5015 longitude: -73.9800
# LESTE latitude: -7.1507 longitude: -34.7932
