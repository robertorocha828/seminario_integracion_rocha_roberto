from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_world import router
from routers.hello_world_mp import router as router_mp

app = FastAPI(title="Curso FastAPI + uv")
app.include_router(router)
app.include_router(router_mp)
