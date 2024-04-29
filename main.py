from fastapi import FastAPI
from src.api_v1.geo import router as router_v1

app = FastAPI(openapi_url='/src/openapi.json')
app.include_router(router_v1)