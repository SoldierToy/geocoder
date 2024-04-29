from fastapi import APIRouter, Depends

from src.schemas.geo_shemas import LocationCreateSchema
from src.depends.geo_service_depends import geo_service_depends

router = APIRouter(prefix='/v1')


@router.post("/add_location", status_code=201)
async def add_location(data: LocationCreateSchema, geo_service=Depends(geo_service_depends)):
    res = await geo_service.create_or_update_location(data.location)
    return res
