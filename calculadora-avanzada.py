"""Calcauladora Avanzada"""

print("Bienvenido a la calculadora avanzada")
print("Para salir, escriba salir.")
print("Las operaciones son: suma, resta, multi, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un numero: ")
        if resultado.lower() == "salir":
            break 
        resultado = int(resultado)
    op = input("Ingresar operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresar siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2

    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es {resultado}")
