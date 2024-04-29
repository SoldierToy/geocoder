class GeoService:

    def __init__(self, repo, geocoder_client):
        self.repo = repo()
        self.geocoder_client = geocoder_client()

    async def create_or_update_location(self, location_name: str):
        location_geocoder_coords = await self.geocoder_client.get_location_coords(location_name)

        location_coords_db = await self.repo.get_location_coords(location_geocoder_coords)
        if location_coords_db:
            return location_coords_db
        else:
            await self.repo.create_location_coords(location_geocoder_coords)
