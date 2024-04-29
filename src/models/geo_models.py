import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from src.models.base import Base


class Locations(Base):
    __tablename__ = 'locations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_coords = Column(Geometry('POINT'))

    def __repr__(self) -> str:
        return f"Locations(id={self.id}, name={self.location_coords})"
