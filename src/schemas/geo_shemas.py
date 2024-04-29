from pydantic import BaseModel


class LocationCreateSchema(BaseModel):
    location: str
