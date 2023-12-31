from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def encriptar_texto(texto, clave):
    f = Fernet(clave)
    texto_encriptado = f.encrypt(texto.encode())
    return texto_encriptado

def desencriptar_texto(texto_encriptado, clave):
    f = Fernet(clave)
    texto_desencriptado = f.decrypt(texto_encriptado).decode()
    return texto_desencriptado

# Generar una clave secreta

clave_secreta = generar_clave()

# texto a encriptar

texto_original = "Todo lo puedo en Cristo, que me fortalece!"

# Encriptar el texto

texto_encriptado = encriptar_texto(texto_original, clave_secreta)

print("*"*100)
print(f"Texto Original: {texto_original}")
print(f"Texto Encriptado: {texto_encriptado}")
print("*"*100)

#Desencriptar Texto
texto_desencriptado = desencriptar_texto(texto_encriptado, clave_secreta)

print(f"Texto Encriptado: {texto_desencriptado}")
print("*"*100)