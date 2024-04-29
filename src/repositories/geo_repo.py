from geoalchemy2 import WKTElement
from sqlalchemy import func
from src.core.db import async_session_factory
from sqlalchemy import insert, select, update, delete
from src.models.geo_models import Locations


class GeoRepo:
    model = Locations

    async def create_location_coords(self, location_coords: str) -> None:
        async with async_session_factory() as session:
            coordinates_str = f'POINT({location_coords})'
            location_coords_wkt = WKTElement(coordinates_str)
            stmt = insert(self.model).values(location_coords=location_coords_wkt)
            await session.execute(stmt)
            await session.commit()

    async def get_location_coords(self, location_coords: str) -> str:
        async with async_session_factory() as session:
            coordinates_str = f'POINT({location_coords})'
            location_coords_wkt = WKTElement(coordinates_str)
            stmt = (
                select(func.ST_AsText(self.model.location_coords).label("location_coords_text"))
                .filter(self.model.location_coords == location_coords_wkt)
            )
            res = await session.execute(stmt)
            res = res.scalar()
            if res:
                coords = res[6:-1]
                return coords

