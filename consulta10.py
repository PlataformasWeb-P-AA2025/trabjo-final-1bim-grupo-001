from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 10 para obtener las publicaciones que recibieron todos los tipos de reacciones disponibles
tipos = session.query(Reaccion.tipo_reaccion).distinct().all()
total_tipos = len(tipos)


resultado = (
    session.query(
        Publicacion.contenido,
        func.count(func.distinct(Reaccion.tipo_reaccion)).label("tipos_usados")
    )
    .join(Reaccion)
    .group_by(Publicacion.id)
    .having(func.count(func.distinct(Reaccion.tipo_reaccion)) == total_tipos)
    .all()
)
print("Publicaciones con recibieron todas los tipos de reacciones:")
for result in resultado:
    print(f"Publicación: {result.contenido}, Tipos de reacciones usados: {result.tipos_usados}")