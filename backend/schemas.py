from pydantic import BaseModel

class PeliculaBase(BaseModel):
    titulo: str
    genero: str
    ano: int

class PeliculaCreate(PeliculaBase):
    pass

class Pelicula(PeliculaBase):
    idPelicula: int

class UsuarioLogin(BaseModel):
    nombre: str
    password: str
    
    class Config:
        orm_mode = True
        
