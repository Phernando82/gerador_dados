from geopy import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "4.403373"
Longitude = "-64.907227"

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
