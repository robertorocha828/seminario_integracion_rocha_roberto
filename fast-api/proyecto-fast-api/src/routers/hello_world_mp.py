from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class MensajeAdmision(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde el Sistema de Admisión",
            "autor": "Ing. Roberto Rocha",
            "version": "0.1.0"}


@router.get("/notificacion")
def endpoint_notificacion() -> MensajeAdmision:
    return {"texto" : "Roberto Rocha: tu postulación a Desarrollo de Software fue recibida",
            "campo_interno" : "revisado por el comité de admisiones"}



@router.get("/resultado", response_model=MensajeAdmision)
def endpoint_resultado():
    return {"texto": "Hernán Varas: tu nota del examen es 8.5 sobre 10",
            "prioridad": 5,
            "campo_interno": "no debería salir: nota mínima definida por el comité"}


@router.get("/campo-extra", response_model=MensajeAdmision)
def endpoint_campo_extra():
    return {"texto": "Christian Cañar: tus documentos están completos",
            "prioridad": 5,
            "campo_interno": "sí debe salir incluido en el modelo",
            "campo_extra" : "no debe salir esto"}