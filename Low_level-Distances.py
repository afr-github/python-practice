## NUMBERS ##
from functools import partial

from geopy import distance
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example")
geocode = partial(geolocator.geocode, language="es")
geocode = lambda query: geolocator.geocode("%s, Ciudad Juárez, Municipio de Juárez, Chihuahua," % query)
location1 = geocode("Calle Prado Sur 5818")
location2 = geocode("Av Cesareo Santos 6592")
distance_km = distance.distance("{},{}".format(location1.latitude, location1.longitude),"{},{}".format(location2.latitude, location2.longitude)).kilometers
distance_km_circle = distance.great_circle("{},{}".format(location1.latitude, location1.longitude),"{},{}".format(location2.latitude, location2.longitude)).kilometers
elipsoide_km = distance.geodesic("{},{}".format(location1.latitude, location1.longitude), "{},{}".format(location2.latitude, location2.longitude), ellipsoid="GRS-80").miles


reverse = partial(geolocator.reverse, language="es")
#print(reverse("31.6602825,-106.389065").address)
#print(reverse("{},{}".format(location.latitude,location.longitude)).address)

print("The distance between {} and {} is {} Km.".format(location1.address, location2.address, distance_km))
print("The great circle distance between {} and {} is {} Km.".format(location1.address, location2.address, distance_km_circle))
print("Elipsoid for {} and {} is {} Km.".format(location1.address, location2.address, elipsoide_km))
## note ##
# distance.EARTH_RADIUS can be modified to fit calculations
# Error of about 0.5% ~ International Union of Geodesy and Geophysics, (2a + b)/3 = 6371.0087714150598 kilometers approx 6371.009 km (for WGS-84)
