from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 08 para obtener el top 5 usuarios con más reacciones
resultado = (
    session.query(
        Usuario.nombre_usuario,
        func.count(Reaccion.id).label("total_reacciones")
    )
    .join(Reaccion, Usuario.id == Reaccion.usuario_id)
    .group_by(Usuario.id)
    .order_by(func.count(Reaccion.id).desc())
    .limit(5)  # Limitar a los 5 usuarios con más reacciones
    .all()
)
print("Top 5 usuarios con más reacciones:")
for result in resultado:
    print(f"Usuario: {result.nombre_usuario}, Total de reacciones: {result.total_reacciones}")