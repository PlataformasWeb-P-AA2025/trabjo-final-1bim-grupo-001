from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

# conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

#Consulta 06 para obtener la publicacion mas reaccionada
resultado = (
    session.query(
        Publicacion.contenido,
        func.count(Publicacion.reacciones).label("total_reacciones")
    )
    .join(Publicacion.reacciones)
    .group_by(Publicacion.id)
    .order_by(func.count(Publicacion.reacciones).desc())
    .first()  # solo la más reaccionada
)
print("La publicación más reaccionada es:")
print(f"{resultado.contenido} \nCon: \n{resultado.total_reacciones} reacciones.")