from tkinter import mainloop

print("--------------------------")
print("----------MAYOR-----------")
print("--------------------------")

#INPUT
a = int(input("Digite el Primer numero: "))
b = int(input("Digite el Segundo numero: "))
c = int(input("Digite el Tercer numero: "))

#PROCESS
if a > b and a > c:
    print("El numero mayor es el: {a}   ")

elif b > a and b > c:
    print("El numero mayor es el: {b}   ")

elif c > a and c > b:
    print("El numero mayor es el: {c}   ")
        

#OUTPUT
print("--------------RESULTADO------------" + "\nEl numero mayor es: " + str(c))

#Fin 
mainloop
