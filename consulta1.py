from sqlalchemy import create_engine, and_, not_, or_
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos

# importamos las clases ORM necesarias
from Generar_tablas import Usuario, Publicacion, Reaccion

# creamos el engine y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

print("Publicaciones de un usuario específico (este caso: Karen)\n")
usuario = session.query(Usuario).filter_by(nombre_usuario="Karen").first()
if usuario:
    for pub in usuario.publicaciones:
        print(pub)
        print("---------")
else:
    print("Usuario no encontrado\n")