from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from Generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# Conexión y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

print("Conteo de cada tipo de reacción usada\n")
from sqlalchemy import func
resultados = session.query(
    Reaccion.tipo_reaccion,
    func.count(Reaccion.id)
).group_by(Reaccion.tipo_reaccion).all()

for tipo, cantidad in resultados:
    print(f"Reacción: {tipo} - Veces usada: {cantidad}")
print("---------")