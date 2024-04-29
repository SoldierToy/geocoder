import httpx

from src.services.geo_service import GeoService
from src.repositories.geo_repo import GeoRepo
from src.utils.yandex_geocoder import YandexGeoсoderClient


def geo_service_depends():
    return GeoService(GeoRepo, yandex_geocoder_client_depends)


def yandex_geocoder_client_depends():
    return YandexGeoсoderClient(httpx.AsyncClient)
