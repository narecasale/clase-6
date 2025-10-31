"""
1.el programa pide al usuario ingresar una plabra o frase
2.se muestra un menu con funciones para analizar la cadena:
  -contar cuantas letras tiene
  -contar cuantas vocales tiene
  -invertir la cadena
  ver si alguna palabra o frase es un palindromo
  -salir

  3.cada accion es una funcion 

"""

# ===FUNCIONES====

def contar_letras (cadena):
    a = len(cadena.replace(" ", ""))
    return a

def contar_vocales (cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    total = 0

    for v in vocales:
        total += cadena.count(v)

    return total   

def invertir_cadena (cadena):
    return cadena[::-1]

"""
[::-1] -----slice(revanado)

-inicio:fin:paso
-si no ponemos inicio ni fin,se toma toda la cadena
el -1 en paso significa ir de atras hacia adelante

"hola"[::-1] ----empieza en la ultima letra y va hacia atras "aloh"
"""

def es_palindromo(cadena):
    limpio = cadena.replace(" ", "").lower()

    return limpio == limpio [::-1]

#===== programa principal ========

texto = input("ingrese una palabra o frase")

opcion = 0

while opcion != 5:
    print("\n ===== MENU =======")
    print ("1- contar letras")
    print ("2- contar vocales")
    print ("3- invertir cadena")
    print ("4- comprobar si la palabra o frase es un palindromo")
    print ("5- salir")

    opcion = int(input("seleccione una opcion: "))
 
    if opcion == 1:
        print("cantidad de letras: ", contar_letras(texto))

    elif opcion == 2:
        print("cantidad de vocales: ", contar_vocales(texto))

    elif opcion == 3:
          print("invertida: ",invertir_cadena(texto) )

    elif opcion == 4:
         if es_palindromo(texto):
           print("esta palabra es un palidromo: ")

         else:
          print("no es un palidromo")

    elif opcion == 5:
          print("chao")

    else:
     print("opcion no valida, vuelve a intentar")

