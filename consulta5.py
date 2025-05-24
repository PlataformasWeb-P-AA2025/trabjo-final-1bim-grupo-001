from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from Generar_tablas import Usuario, Reaccion

# Crear la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

print("Consulta: Número de reacciones por usuario:\n")

resultados = (
    session.query(Usuario.nombre_usuario, func.count(Reaccion.id).label("total_reacciones"))#usamos func para poder contar
    .join(Reaccion, Usuario.id == Reaccion.usuario_id)
    .group_by(Usuario.id)
    .order_by(func.count(Reaccion.id).desc())
    .all()
)

for nombre, total in resultados:
    print(f"{nombre}: {total} reacciones")
