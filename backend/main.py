from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Importar la base de datos solo si vamos a usarla
USE_DB = False  # Cambia a True cuando tengas base de datos
if USE_DB:
    from database import SessionLocal, engine, Base
    import models as models, schemas as schemas
    Base.metadata.create_all(bind=engine)

app = FastAPI()

# Permitir CORS para tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajusta luego a la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware para logging
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"{request.method} {request.url}")
    response = await call_next(request)
    return response

# Dependencia para obtener la sesión de DB
if USE_DB:
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

# Datos de prueba
def get_prueba_peliculas():
    return [
        {"idPelicula": 1, "titulo": "Pelicula 1", "genero": "Acción", "anio": 2021},
        {"idPelicula": 2, "titulo": "Pelicula 2", "genero": "Comedia", "anio": 2020},
        {"idPelicula": 3, "titulo": "Pelicula 3", "genero": "Drama", "anio": 2022},
    ]

# Rutas de prueba (si no hay DB, solo esta raíz funciona)
@app.get("/")
def raiz():
    return {"mensaje": "API de Películas funcionando sin base de datos!"}

# Rutas que usan DB (solo activas si USE_DB = True)
if USE_DB:
    # GET todas las películas
    @app.get("/peliculas", response_model=list[schemas.Pelicula])
    def listar_peliculas(db: "Session" = Depends(get_db)):
        return db.query(models.Pelicula).all()

    # GET película por ID
    @app.get("/buscarPeliculas/{pelicula_id}", response_model=schemas.Pelicula)
    def obtener_pelicula(pelicula_id: int, db: "Session" = Depends(get_db)):
        pelicula = db.query(models.Pelicula).filter(models.Pelicula.idPelicula == pelicula_id).first()
        if not pelicula:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")
        return pelicula

    # POST crear película
    @app.post("/crearPelicula", response_model=schemas.Pelicula)
    def crear_pelicula(pelicula: schemas.PeliculaCreate, db: "Session" = Depends(get_db)):
        nueva = models.Pelicula(**pelicula.model_dump())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva

    # PUT actualizar película
    @app.put("/actualizaPelicula/{pelicula_id}", response_model=schemas.Pelicula)
    def actualizar_pelicula(pelicula_id: int, pelicula: schemas.PeliculaCreate, db: "Session" = Depends(get_db)):
        peli = db.query(models.Pelicula).filter(models.Pelicula.idPelicula == pelicula_id).first()
        if not peli:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")
        for key, value in pelicula.model_dump().items():
            setattr(peli, key, value)
        db.commit()
        db.refresh(peli)
        return peli

    # DELETE película
    @app.delete("/borrarPelicula/{pelicula_id}")
    def borrar_pelicula(pelicula_id: int, db: "Session" = Depends(get_db)):
        pelicula = db.query(models.Pelicula).filter(models.Pelicula.idPelicula == pelicula_id).first()
        if not pelicula:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")
        db.delete(pelicula)
        db.commit()
        return {"mensaje": "Pelicula eliminada"}

    # POST login
    @app.post("/login")
    def login(usuario: schemas.UsuarioLogin, db: "Session" = Depends(get_db)):
        db_usuario = db.query(models.Usuario).filter(models.Usuario.nombre == usuario.nombre).first()
        if not db_usuario or db_usuario.password != usuario.password:
            raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
        return {"mensaje": "Correcto"}

# Si no usamos base de datos, devolver datos de prueba
else:
    # GET todas las películas (datos de prueba)
    @app.get("/peliculas")
    def listar_peliculas():
        return get_prueba_peliculas()

    # GET película por ID (datos de prueba)
    @app.get("/buscarPeliculas/{pelicula_id}")
    def obtener_pelicula(pelicula_id: int):
        peliculas = get_prueba_peliculas()
        pelicula = next((p for p in peliculas if p["idPelicula"] == pelicula_id), None)
        if not pelicula:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")
        return pelicula

    # POST crear película (datos de prueba, solo agrega a la lista)
    @app.post("/crearPelicula")
    def crear_pelicula(pelicula: dict):
        peliculas = get_prueba_peliculas()
        nueva_pelicula = {"idPelicula": len(peliculas) + 1, **pelicula}
        peliculas.append(nueva_pelicula)
        return nueva_pelicula

    # PUT actualizar película (datos de prueba)
    @app.put("/actualizaPelicula/{pelicula_id}")
    def actualizar_pelicula(pelicula_id: int, pelicula: dict):
        peliculas = get_prueba_peliculas()
        index = next((i for i, p in enumerate(peliculas) if p["idPelicula"] == pelicula_id), None)
        if index is None:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")
        peliculas[index] = {"idPelicula": pelicula_id, **pelicula}
        return peliculas[index]

    # DELETE película (datos de prueba)
    @app.delete("/borrarPelicula/{pelicula_id}")
    def borrar_pelicula(pelicula_id: int):
        peliculas = get_fake_peliculas()
        index = next((i for i, p in enumerate(peliculas) if p["idPelicula"] == pelicula_id), None)
        if index is None:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")
        peliculas.pop(index)
        return {"mensaje": "Pelicula eliminada"}

    # POST login (datos de prueba)
    @app.post("/login")
    def login(usuario: dict):
        # En el caso de datos de prueba, solo verifica un login ficticio
        if usuario.get("nombre") == "admin" and usuario.get("password") == "admin123":
            return {"mensaje": "Correcto"}
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")