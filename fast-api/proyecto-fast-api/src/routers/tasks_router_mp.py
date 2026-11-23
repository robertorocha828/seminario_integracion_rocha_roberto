# app/routers/paso1_postulacion_create_body.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

postulaciones_router = APIRouter()


class PostulacionCreate(BaseModel):
    """Lo que el cliente envía para crear una postulación. Sin id: lo asigna el servidor."""
    aspirante: str = Field(min_length=3, max_length=100)
    observaciones: str | None = None
    jornada: str = "matutina"
    documentos: list[str] = Field(default_factory=list)
    nota_examen: float | None = Field(default=None, ge=0, le=10)  

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "aspirante": "Christian Cañar",
                    "observaciones": "Prefiere entrevista en la tarde",
                    "jornada": "vespertina",
                    "documentos": ["copia de cédula", "título de bachiller"],
                    "nota_examen": 8.0,
                }
            ]
        }
    }

class PostulacionRead(BaseModel):
    """Lo que el servidor expone al leer una postulación. Incluye campos calculados por el servidor."""
    id: int
    aspirante: str
    observaciones: str | None
    jornada: str
    documentos: list[str]
    nota_examen: float | None
    admitido: bool


class PostulacionUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    aspirante: str | None = Field(default=None, min_length=3, max_length=100)
    observaciones: str | None = None
    jornada: str | None = None
    documentos: list[str] | None = None
    nota_examen: float | None = Field(default=None, ge=0, le=10)
    admitido: bool | None = None


POSTULACIONES: list[dict] = [
    {"id": 1, "aspirante": "Roberto Rocha", "observaciones": None, "jornada": "matutina", "documentos": ["copia de cédula", "título de bachiller"], "nota_examen": 9.5, "admitido": False},
    {"id": 2, "aspirante": "Hernán Varas", "observaciones": None, "jornada": "vespertina", "documentos": ["copia de cédula"], "nota_examen": 8.5, "admitido": False},
]
NEXT_ID = len(POSTULACIONES) + 1

@postulaciones_router.post("/postulaciones", response_model=PostulacionRead)
def create_postulacion(postulacion: PostulacionCreate) -> dict:
    global NEXT_ID
    nueva_postulacion = {
        "id": NEXT_ID,
        "admitido": False,
        "notas_internas": "creado desde la API",  # campo interno, nunca debería salir al cliente
        **postulacion.model_dump(),
    }
    POSTULACIONES.append(nueva_postulacion)
    NEXT_ID += 1
    return nueva_postulacion


@postulaciones_router.get("/postulaciones", response_model=list[PostulacionRead])
def list_postulaciones() -> list[dict]:
    return POSTULACIONES

@postulaciones_router.patch("/postulaciones/{postulacion_id}", response_model=PostulacionRead)
def update_postulacion(postulacion_id: int, update: PostulacionUpdate) -> dict:
    for postulacion in POSTULACIONES:
        if postulacion["id"] == postulacion_id:
            cambios = update.model_dump(exclude_unset=True)
            postulacion.update(cambios)
            return postulacion
    raise HTTPException(status_code=404, detail="Postulación no encontrada")

@postulaciones_router.post("/postulaciones/from-model")
def create_from_model(postulacion: PostulacionCreate) -> dict:
    global NEXT_ID
    data = postulacion.model_dump()
    nueva_postulacion = {"id": NEXT_ID, "admitido": False, **data}
    POSTULACIONES.append(nueva_postulacion)
    NEXT_ID += 1

    validada = PostulacionRead.model_validate(nueva_postulacion)
    return validada.model_dump()


@postulaciones_router.get("/postulaciones/{postulacion_id}/raw-vs-validated")
def compare_raw_validated(postulacion_id: int) -> dict:
    raw = next((p for p in POSTULACIONES if p["id"] == postulacion_id), None)
    if raw is None:
        raise HTTPException(status_code=404, detail="Postulación no encontrada")

    validada = PostulacionRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validada.model_dump(),
        "validated_model_dump_json": validada.model_dump_json(),
    }

@postulaciones_router.delete("/postulaciones/{postulacion_id}")
def delete_postulacion(postulacion_id: int) -> dict:
    for index, postulacion in enumerate(POSTULACIONES):
        if postulacion["id"] == postulacion_id:
            postulacion_eliminada = POSTULACIONES.pop(index)

            return {
                "mensaje": "Postulación eliminada correctamente",
                "postulacion_eliminada": postulacion_eliminada
            }

    raise HTTPException(
        status_code=404,
        detail="Postulación no encontrada"
    )

@postulaciones_router.get("/postulaciones/{postulacion_id}", response_model=PostulacionRead)
def get_postulacion_by_id(postulacion_id: int) -> dict:
    for postulacion in POSTULACIONES:
        if postulacion["id"] == postulacion_id:
            return postulacion
    raise HTTPException(
        status_code=404,
        detail="Postulación no encontrada"
    )