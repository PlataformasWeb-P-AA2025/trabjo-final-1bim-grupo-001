from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from Generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

# conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# consulta para obtener el usuario con más publicaciones
resultado = (
    session.query(
        Usuario.nombre_usuario,
        func.count(Publicacion.id).label("total_publicaciones") #usamos func para poder contar
    )
    .join(Publicacion, Usuario.id == Publicacion.usuario_id)
    .group_by(Usuario.id)
    .order_by(func.count(Publicacion.id).desc())
    .first()  # solo el de mayor número
)


print("Usuario con más publicaciones:")
if resultado:
    print(f"Usuario: {resultado.nombre_usuario}")
    print(f"Total de publicaciones: {resultado.total_publicaciones}")
else:
    print("No se encontraron publicaciones registradas.")
