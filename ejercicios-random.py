import  random

#ejercicio 1
a = random.randint (1, 10)
numero = input("Adivina el numero: ")

if numero == a:
    print("Has hacertado")

else:
    print (f"Te has equivocado, el numero es {a}")
