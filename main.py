from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Endpoint para ver si funciona" : "Funcionando"}

@app.get("/{nombre}")
def nombre(nombre: str):
    return {"Endpoint nombre dice " : f" Hola {nombre} ! "}
