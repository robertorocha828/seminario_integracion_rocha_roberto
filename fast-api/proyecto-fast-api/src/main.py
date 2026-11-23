from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_world import router
from routers.tasks_router import tasks_router
from routers.tasks_router_mp import postulaciones_router
from routers.hello_world_mp import hello_world_router

app = FastAPI(title="Curso FastAPI + uv")
app.include_router(router)
app.include_router(tasks_router)
app.include_router(postulaciones_router)
app.include_router(hello_world_router)
