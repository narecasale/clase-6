""""
calculadora-funciones
ingresar parametros y retornar el resultado de la operacion"""

# ==== FUNCIONES ====

def sumar (a,b):
    return a + b

def restar (a,b):
    return a -b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    if b != 0:
        return a/b
    else:
        return "error!"
    
def potencia (a,b):
    return a**b

# === programa principal ===

opcion = 0

while opcion !=6:
 print("\==== ingrese una opcion ====")    
 print(" 1_ sumar")
 print(" 2_ restar")
 print(" 3_ multiplicar")
 print(" 4_ dividir")
 print(" 5_ potencia")
 print(" 6_ salir")

 opcion = int(input ("seleccione una opcion:"))

 if opcion in [1,2,3,4,5]:
     x = float(input("ingrese el primer numero"))
     y = float(input("ingrese el segundo numero"))

 if opcion == 1:
     print("resultado", sumar(x,y))

 elif opcion ==2:
     print("resultado", restar(x,y))

 elif opcion ==3:
     print("resultado", multiplicar(x,y))    

 elif opcion ==4:
    print("resultado", dividir(x,y))

 elif opcion ==5:
    print("resultado", potencia(x,y))

 elif opcion ==6:
    print("nos vemos!")

 else:
    print("opcion no valida, vuelve a intentarlo")

    