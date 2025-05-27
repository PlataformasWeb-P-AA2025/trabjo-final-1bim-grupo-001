from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Publicacion, Reaccion
from configuracion import cadena_base_datos

# conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 08 para obtener publicaciones sin reacciones
resultado = (
    session.query(Publicacion)
    .outerjoin(Reaccion)
    .filter(Reaccion.id == None)
    .all()
)
print("Publicaciones sin reacciones:")

#Si no hay publicaciones sin reacciones, se imprime un mensaje
if not resultado:
    print("No hay publicaciones sin reacciones.")
