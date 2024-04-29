from src.core.settings import settings


class YandexGeoсoderClient:

    def __init__(self, client):
        self.client = client

    async def get_location_coords(self, location: str):
        url = f'https://geocode-maps.yandex.ru/1.x/?apikey={settings.yandex_geocoder_api_key}&geocode={location}&format=json'
        async with self.client() as client:
            response = await client.get(url)
            response = response.json()
            coords = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            return coords
