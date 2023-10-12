import sqlite3

# Conexion con la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute(
    """
                    CREATE TABLE IF NOT EXISTS usuarios(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        email TEXT
                    )
                """
)

conn.commit()

# Crear registro -> C

def crear_usuario(nombre: str, email) -> str:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES(?, ?)", (nombre, email)) 
    conn.commit()
    return "Usuario Agregado"

# Obtener Registros
def obterner_usuarios() -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    usuarios = cursor.fetchall()

    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario)

    return lista_usuarios


# Actualizar usuario por id - > U

def actualizar_usuario(id:int, nombre:str, email:str) -> str:
    cursor.execute(
        "UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nombre, email, id)
    ) 
    conn.commit()
    return "Usuarios actualizado"

# Eliminar usuario
def eliminar_usuario(id) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"

# Leer registro por su ID

def obterner_usuario(id: int) -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if usuario:
        return usuario
    return "Usuario no encontrado"


# Crear usuario

# crear_usuario("Juan", "juan@example.com")
# crear_usuario("Jcva", "jcva@example.com")
# crear_usuario("Joselito", "jose@example.com")

# OBTENER USUARIO

# print(obterner_usuarios())

# ACTUALIZAR USUARIO
# print(actualizar_usuario(2, "jcva Coder", "jcva@example.com"))

# OBTENER USUARIO

# print(obterner_usuario(2))

# ELIMINAR USUARIO

# print(eliminar_usuario(3))