edad = input("Ingresar edad: ")
edad = int(edad)

if edad >= 60:
    print("Puedes ingresar, tienes descuento por ser adulto mayor")
elif edad >=18:
    print("Puedes ingresar, eres mayor de edad")
else:
    print("Lamentablemente no puedes ingresar")

print("Gracias por visitarnos")