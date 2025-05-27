from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 07 para obtener los usuarios que reaccionaron a sus propias publicaciones
resultado = (
    session.query(
        Usuario.nombre_usuario,
        Publicacion.contenido,
        Reaccion.tipo_reaccion
    )
    .join(Reaccion, Usuario.id == Reaccion.usuario_id) 
    .join(Publicacion, Reaccion.publicacion_id == Publicacion.id) 
    .filter(Reaccion.usuario_id == Publicacion.usuario_id) # Filtro para que el usuario reaccione a su propia publicación
    .all()
)
print("Usuarios que reaccionaron a sus propias publicaciones")
print("-----------------------------------------------------")
for result in resultado:
    print(f"Usuario: {result.nombre_usuario}  reaccionó a su propia publicación: {result.contenido}, con: {result.tipo_reaccion}.")
