from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()


class usuarios(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(500))
    publicacion_usuario = relationship("Publicacion_usuario", back_populates="usuarioa")


    def __repr__(self):
        return "Usuario: nombre=%s" % (
                          self.nombre_usuario )


class publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    publicacion = Column(String(500))
    publicacion_usuario = relationship("Publicacion_usuario", back_populates="publicaciones")

    def __repr__(self):
        return "Usuario: nombre=%s" % (
                          self.publicacion)
    


    
class publicacion_usuario(Base):
    __tablename__ = 'publicacion_usuario'
    id = Column(Integer, primary_key=True)
    publicacion_id =  Column(Integer, ForeignKey("publicacion.id"),primary_key=True)
    usuario_id =Column(Integer, ForeignKey("usuario.id"),primary_key=True)

    publicacion = relationship("Publicacion", back_populates="usuarios")
    usuario = relationship("Usuarios", back_populates="publicaciones")

    


    def __repr__(self):
        return "Usuario: nombre=%s \n Publicacion: publicacion=%s \n "%(
                          self.usuario
                          self.publicacion,
                            )
    

class emociones(Base):
    __tablename__ = 'emocion'
    id = Column(Integer, primary_key=True)
    publicacion_id =  Column(Integer, ForeignKey("publicacion.id"),primary_key=True)
    usuario_id =Column(Integer, ForeignKey("usuario.id"),primary_key=True)
    tipo_emocion = Column(String(100))

    publicacion = relationship("Publicacion", back_populates="usuarios")
    usuario = relationship("Usuarios", back_populates="publicaciones")

    def __repr__(self):
        return "Usuario: nombre=%s \n Publicacion: publicacion=%s \n Tipo_emocion:tipo_emocion =%s \n"%(
                          self.usuario
                          self.publicacion,
                            )