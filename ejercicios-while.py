# ============================
#   EJERCICIOS CON WHILE
# ============================

def contar_hasta_10():
    resultado = ""
    numero_inicial = 1
    while numero_inicial <= 10:
        #resultado = resultado + str(numero_inicial)
        resultado = f"{resultado}{numero_inicial},"
        #print (numero_inicial)
        numero_inicial = numero_inicial + 1
        
    return resultado

print (contar_hasta_10())   





def suma_hasta_cero():
    sumatorio = 0
    numero = None
    while numero != 0:
         numero = int(input("Introduce un numero: "))
         sumatorio += numero
    return sumatorio 



def adivinar_numero():
    numero_aleatorio = 7
    num_user = None
    while num_user != 7:
        num_user = int(input("Adivina el numero: "))
    print(f"Acertaste el numero era {numero_aleatorio}")

if __name__ == "__main__":
    print("Ejecutando tests...")

    # ------- Test contar_hasta_10 -------
    assert contar_hasta_10() == "1,2,3,4,5,6,7,8,9,10", \
        f"contar_hasta_10() debería devolver '1,2,3,4,5,6,7,8,9,10', pero devolvió {contar_hasta_10()}"

    # ------- Test suma_hasta_cero -------
    # Para pruebas: 5 + 3 + 2 = 10
    # (El alumno debe simularlo en su código)
    print("Cuando te lo pida introduce los numeros 5,3 y 2")
    assert suma_hasta_cero() == 10, \
        f"suma_hasta_cero() debería devolver 10, pero devolvió {suma_hasta_cero()}"

    # ------- Test adivinar_numero -------
    # Secuencia simulada: 3, 5, 7 → 3 intentos
    assert adivinar_numero() == 3, \
        f"adivinar_numero() debería devolver 3, pero devolvió {adivinar_numero()}"