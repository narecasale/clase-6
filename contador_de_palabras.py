"""
crear un programa que:
1) pedimos al usuario que ingrese una frase
2) determinar para esa frase:
   -cuantas palabras tiene
   -cuantas letras tiene
   -devolver la palabra mas larga
   -salir
3) mostrar los resultados en pantalla
"""
# ==== funciones =====

def contar_palabras (frase):
    a = len(frase.split())
    return a

def contar_letras (frase):
    b = len(frase.replace(" ", ""))
    return b

def devolver_palabra (frase):
    palabras = frase.split()
    return max(palabras, key= len)
# ==== programa ====

texto = input("ingrese una frase")

opcion = 0

while opcion != 4:
    print("====MENU====")
    print("contar palabras")
    print("contar letras")
    print("devolver palabra mas larga")
    print("salir")

    opcion = int(input("eliga una opcion"))

    if opcion == 1:
        print("cantidad de palabras",contar_palabras(texto))

    elif opcion ==2:
        print("cantidad de letras",contar_letras(texto))

    elif opcion ==3:
        print("palabra mas larga",devolver_palabra(texto))    

    elif opcion ==4:
        print("bye bye")

    else :
        print("la opcion no es valida,volve a intentar")        