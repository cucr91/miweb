"""Calculadora Basica"""

n1 = input("Ingresar primer numero: ")
n2 = input("Ingresar Segundo numero: ")

n1 = int(n1)
n2 = int(n2)

# operaciones basicas: Suma, Resta, Multiplicacion y Division.
suma = n1+n2
resta = n1-n2
multi = n1*n2
div = n1/n2

# Mensaje para el usuario
mensaje = f"""
El resultado para los numeros {n1} y {n2} son: 
Para la suma es {suma}
Para la resta es {resta}
Para la multiplicación es {multi}
Para la división es {div}
"""
print("Muchas gracias por usar esta aplicacion" + mensaje)
