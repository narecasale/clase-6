# 1 pedir los 3 numeros
numeros = []

for i in range (3):
    n = float(input(f"ingrese el primer numero {i + 1}" ))
    numeros.append(n)

#2 ordenarlos de mayor a menor
numeros.sort(reverse=True)

#3 mostrar el resultado
print("\n los numeros ordenados de mayor a menor son:")
for num in numeros:
    print(num)

# ===============================================================================

a = float(input("ingrese el primer numero:"))
b = float(input("ingrese el segundo numero:"))
c = float(input("ingrese el tercer numero:"))   

mayor = max(a,b,c)
menor = min(a,b,c)
medio = (a+b+c) - (mayor + menor)

print("\n numeros ordenados de mayor a menor: ")
print(mayor,medio,menor)

# ===========================================================================================

numeros = []

for i in range(3):
    numeros[1] = float(input (f"ingrese el numero {i + 1}:"))

max=0

for i in range(3):
    if numeros[1] > max:
        max = numeros[1]

min = max

for i in range(3):
    if numeros[i] < min:
        min = numeros[i]

medio = (a+b+c) - (max+min)
