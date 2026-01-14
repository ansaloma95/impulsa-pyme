# Importamos FastAPI, el núcleo de la aplicación
from fastapi import FastAPI

# Importamos el router de health
# Esto conecta las rutas externas con la app principal
from backend.routes.health import router as health_router

# Creamos la aplicación principal
app = FastAPI()


@app.get("/")
def root():
    """
    Endpoint raíz del backend.

    Sirve como prueba rápida para saber
    que la API está respondiendo.
    """
    return {"message": "ImpulsaPYME backend activo"}


# Registramos las rutas de health en la aplicación
# A partir de aquí, /health queda disponible
app.include_router(health_router)
