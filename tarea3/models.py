from sqlalchemy import Column, Integer, String
from database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"

    idPelicula = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100))
    genero = Column(String(50))
    ano = Column(Integer)
    
class Usuario(Base):
    __tablename__ = "usuarios"
    idUsuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    password = Column(String(50))

