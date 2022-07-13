import numpy as np
from geopy import Nominatim, Point
from shapely.geometry import Polygon


# Função gera Cidade e Estado

# primeiro gerar latitude e longitude aleatoria com numpy



def random_lat_lon(n=1, lat_min=-90., lat_max=90., lon_min=-180., lon_max=180.):
    """
    this code produces an array with pairs lat, lon
    """
    lat = np.random.uniform(lat_min, lat_max, n)
    lon = np.random.uniform(lon_min, lon_max, n)
    coord = np.array(tuple(zip(lat, lon)))
    return coord


print(random_lat_lon())


# saber se essa latitude e longitude está no Brasil
def area_contem_cliente(a, c):
    ponto = Point(c)
    poligono = Polygon(a)
    return poligono.contains(ponto)


cidade = (-15.7801, -47.9292)

brasil = [(-8.046177, -34.584961),
          (-20.784877, -40.737305),
          (-33.713374, -53.481445),
          (-30.285635, -57.612305),
          (-16.370743, -60.249023),
          (-7.436552, -73.696289),
          (4.403373, -64.907227),
          (4.228090, -51.547852)]

print(area_contem_cliente(brasil, cidade))

# determinar Cidade, Estado, País e CEP

geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "-16.6799"
Longitude = "-49.255"

location = geolocator.reverse(Latitude + "," + Longitude)
print(location)
address = location.raw['address']
print(address)
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
print('City : ', city)
print('State : ', state)
print('Country : ', country)
print('Zip Code : ', zipcode)