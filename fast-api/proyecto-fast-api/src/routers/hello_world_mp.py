from fastapi import APIRouter
from pydantic import BaseModel


hello_world_router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@hello_world_router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde el Sistema de Admisión del Instituto Central Técnico (FastAPI + uv)",
            "autor": "Ing. Roberto Rocha",
            "version": "0.1.0"}

@hello_world_router.get("/roberto")
def endpoint_roberto() -> Mensaje:
    return {"texto" : "Roberto Rocha: tu postulación a Desarrollo de Software fue recibida", 
            "campo_interno" : "imprime desde endpoint de admisión"}


@hello_world_router.get("/rocha", response_model=Mensaje)
def endpoint_rocha():
    return {"texto": "Hernán Varas: tu nota del examen es 8.5 sobre 10", 
            "prioridad": 5, 
            "campo_interno": "no debería salir"}

@hello_world_router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Christian Cañar: tus documentos están completos", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra" : "no debe salir esto"}