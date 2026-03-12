import random
import string

print("=== GENERADOR DE CONTRASEÑAS SEGURAS ===")

longitud = int(input("¿Cuántos caracteres quieres para tu contraseña? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("\nTu contraseña segura es:")
print(contraseña)