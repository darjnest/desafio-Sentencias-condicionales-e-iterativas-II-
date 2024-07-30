import getpass
from string import ascii_lowercase

#Solicitar la contrasena de manera oculta
password = getpass.getpass("Ingrese la contraseña: ").strip().lower()

intentos = 0

guessed_password = ""

#Realiza la busqueda de fuerza bruta
for char in password: 
    for letter in ascii_lowercase:
        intentos += 1
        if char == letter:
            guessed_password += letter
            break

print(f"La contraseña fue forzada en {intentos} intentos.")
print(f"La contraseña adivinada es: {guessed_password}")