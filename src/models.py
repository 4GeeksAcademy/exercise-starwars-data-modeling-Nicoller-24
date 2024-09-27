import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class PersonajesFavoritos(Base):
    __tablename__ = 'personajesFavoritos'
    id = Column(Integer, primary_key=True)
    user_favorito = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario")
    characters_favorito = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship("Personajes")


class PlanetasFavoritos(Base):
    __tablename__ = 'planetasFavoritos'
    id = Column(Integer, primary_key=True)
    user_favorito = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario")
    planeta_favorito = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship("Planetas")


class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    pasword = Column(String(250), nullable=False)


    def to_dict(self):
        return {}

## Generar el diagrama ER a partir de la base de datos
render_er(Base, 'diagram.png')
