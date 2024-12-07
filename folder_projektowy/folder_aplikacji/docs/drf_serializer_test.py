from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Tworzenie nowych obiektów
stanowisko = Stanowisko.objects.create(nazwa="Kierownik", opis="Zarządza tymi co zarządzają")
osoba = Osoba.objects.create(imie="Jan", nazwisko="Malinowski", plec=2, stanowisko=stanowisko)

# Inicjalizacja serializera dla Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# Serializacja do JSON
osoba_json = JSONRenderer().render(osoba_serializer.data)
print(osoba_json)

# Deserializacja z JSON do słownika
stream = io.BytesIO(osoba_json)
data = JSONParser().parse(stream)

# Tworzenie obiektu deserializera dla danych JSON
deserializer = OsobaSerializer(data=data)

# Walidacja danych
print(deserializer.is_valid())
print(deserializer.errors)

# Zapis do bazy danych, jeśli dane są poprawne
if deserializer.is_valid():
    deserializer.save()

# Test z błędnymi danymi
invalid_data = {'imie': 'Adam', 'nazwisko': 'Nowak', 'plec': 'Nieznany', 'stanowisko': stanowisko.id}
invalid_serializer = OsobaSerializer(data=invalid_data)
print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

# Inicjalizacja serializera dla Stanowiska
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# Serializacja Stanowiska do JSON
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# Deserializacja Stanowiska z JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data=data)
print(deserializer.is_valid())
if deserializer.is_valid():
    deserializer.save()
