import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from myphone import number

# Verificar e analisar o número de telefone
try:
    pepnumber = phonenumbers.parse(number)
except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f"Erro ao analisar o número: {e}")
    exit()

# Obter descrição da localização
location = geocoder.description_for_number(pepnumber, "pt")
if not location:
    print("Localização não encontrada")
    exit()

print(f"Localização: {location}")

# Obter nome da operadora
service_pro = carrier.name_for_number(pepnumber, "pt")
print(f"Operadora: {service_pro}")

# Configurar a API do OpenCage
key = 'e5f1cac6177942a6924ca32804498f29'
geocoder = OpenCageGeocode(key)

# Geocodificar a localização
results = geocoder.geocode(location)
if not results:
    print("Geocodificação falhou")
    exit()

# Obter coordenadas
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"Latitude: {lat}, Longitude: {lng}")

# Criar e salvar o mapa
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
print("Mapa salvo como mylocation.html")
