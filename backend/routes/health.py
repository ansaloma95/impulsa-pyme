# Importamos APIRouter, que sirve para agrupar rutas relacionadas
from fastapi import APIRouter

# Creamos un router específico para health
# Esto permite separar las rutas por responsabilidad
router = APIRouter()


@router.get("/health")
def health_check():
    """
    Endpoint de salud del sistema.

    Se usa para verificar si el backend está activo.
    Normalmente lo consultan:
    - servidores
    - contenedores Docker
    - sistemas de monitoreo
    """
    return {
        "status": "ok",
        "service": "impulsa-pyme-backend"
    }
