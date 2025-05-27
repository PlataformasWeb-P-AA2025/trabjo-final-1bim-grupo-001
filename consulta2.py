from sqlalchemy import create_engine, and_, not_, or_
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos

# importamos las clases ORM necesarias
from generar_tablas import Usuario, Publicacion, Reaccion

# creamos el engine y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

print("Reacciones a una publicación específica\n")
contenido = "Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada."
publicacion = session.query(Publicacion).filter_by(contenido=contenido).first()
if publicacion:
    for reaccion in publicacion.reacciones:
        print(reaccion)
        print("---------")
else:
    print("Publicación no encontrada\n")