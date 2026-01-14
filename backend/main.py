from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ImpulsaPYME backend activo"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "impulsa-pyme-backend"
    }
