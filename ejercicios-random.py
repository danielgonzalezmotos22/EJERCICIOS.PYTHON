import  random

#ejercicio 1
a = random.randint (1, 10)
numero = input("Adivina el numero: ")

def aleatorio ():
    print (a)

if numero == a:
    print("Has hacertado")

else:
    print ("Te has equivocado",f"el numero es {a}")
