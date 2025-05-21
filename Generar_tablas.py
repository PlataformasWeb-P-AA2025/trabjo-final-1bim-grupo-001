from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()

class usuarios(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(500))
    publicacion = relationship("publicacion", back_populates="usuario")
    reacciones = relationship("reacciones", back_populates="usuario")

    def __repr__(self):
        return "Usuario: nombre=%s" % self.nombre_usuario

class publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    publicacion = Column(String(500))
    usuario = relationship("usuario", back_populates="publicacion")
    reacciones = relationship("reacciones", back_populates="publicacion")

    def __repr__(self):
        return "Publicacion: %s" % self.publicacion

class reacciones(Base):
    __tablename__ = 'reaccion'
    id = Column(Integer, primary_key=True)
    publicacion_id = Column(Integer, ForeignKey("publicacion.id"))
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    tipo_reaccion = Column(String(100))

    publicacion = relationship("publicacion", back_populates="reacciones")
    usuario = relationship("usuarios", back_populates="reacciones")

    def __repr__(self):
        return "Usuario: %s \nPublicacion: %s \nTipo_reaccion: %s" % (
            self.usuario,
            self.publicacion,
            self.tipo_reaccion
        )

Base.metadata.create_all(engine)