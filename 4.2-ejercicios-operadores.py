
def suma(x,y):
    
    return x+y


def comparacion(x,y):
  if x <= y:
      return True
  
  else:
      return False

def mayor_que(x,y):
  if x > y:
      return True
  
  else:
      return False

def menor_que(x,y):
  if x < y:
      return True
  
  else:
      return False

def modulo0(x,y):
    if x % y == 0:
        return True
    else:
        return False
def mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


def edad_18_45(edad):
    if edad >= 18 and edad <= 45:
        return True
    else:
        return False


def edad_45_60(edad):
    if edad >= 45 and edad <= 60:
        return True
    else:
        return False
def edad_mayor_60(edad):
    if edad > 60:
        return True
    else:
        return False




if __name__ == "__main__":
    # Pruebas de validación para las funciones definidas usando assertions

    # Prueba suma
    a = suma(5,5)
    assert suma(2, 3) == 5, f"suma(2, 3) debería ser 5, pero fue {suma(2, 3)}"
    assert suma(-1, 5) == 4, f"suma(-1, 5) debería ser 4, pero fue {suma(-1, 5)}"

    # Prueba comparacion
    assert comparacion(5, 5) == True, f"comparacion(5, 5) debería ser True, pero fue {comparacion(5, 5)}"
    assert comparacion(5, 3) == False, f"comparacion(5, 3) debería ser False, pero fue {comparacion(5, 3)}"

    # Prueba mayor_que
    assert mayor_que(10, 5) == True, f"mayor_que(10, 5) debería ser True, pero fue {mayor_que(10, 5)}"
    assert mayor_que(3, 7) == False, f"mayor_que(3, 7) debería ser False, pero fue {mayor_que(3, 7)}"

    # Prueba menor_que
    assert menor_que(3, 7) == True, f"menor_que(3, 7) debería ser True, pero fue {menor_que(3, 7)}"
    assert menor_que(10, 5) == False, f"menor_que(10, 5) debería ser False, pero fue {menor_que(10, 5)}"

    # Prueba modulo0
    assert modulo0(10, 2) == True, f"modulo0(10, 2) debería ser True, pero fue {modulo0(10, 2)}"
    assert modulo0(10, 3) == False, f"modulo0(10, 3) debería ser False, pero fue {modulo0(10, 3)}"

    # Prueba mayor_edad
    assert mayor_edad(20) == True, f"mayor_edad(20) debería ser True, pero fue {mayor_edad(20)}"
    assert mayor_edad(16) == False, f"mayor_edad(16) debería ser False, pero fue {mayor_edad(16)}"

    # Prueba edad_18_45
    assert edad_18_45(25) == True, f"edad_18_45(25) debería ser True, pero fue {edad_18_45(25)}"
    assert edad_18_45(50) == False, f"edad_18_45(50) debería ser False, pero fue {edad_18_45(50)}"

    # Prueba edad_45_60
    assert edad_45_60(50) == True, f"edad_45_60(50) debería ser True, pero fue {edad_45_60(50)}"
    assert edad_45_60(30) == False, f"edad_45_60(30) debería ser False, pero fue {edad_45_60(30)}"

    # Prueba edad_mayor_60
    assert edad_mayor_60(65) == True, f"edad_mayor_60(65) debería ser True, pero fue {edad_mayor_60(65)}"
    assert edad_mayor_60(55) == False, f"edad_mayor_60(55) debería ser False, pero fue {edad_mayor_60(55)}"

    print("Todas las pruebas pasaron exitosamente.")
