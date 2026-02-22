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