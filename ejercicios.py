import  random
a = random.randint (1, 10)
def aleatorio (numero):
    print (a)

if __name__ == "__main__":
    numero = input("Adivina el numero: ")

if numero == a:
    print("Has hacertado")

else:
    print ("Te has equivocado",f"el numero es {a}")
