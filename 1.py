while True:                 #Bucle inicial para rectificar errores de input
    op=input("Ingrese la operacion que desea testear: ")
    if op not in "+-*/%":
        print ("Operacion invalida, intente nuevamente")
    else:
        break

n1=int(input("Ingrese el primer numero a operar: "))
n2=int(input("Ingrese el segundo numero a operar: "))

print(f"{n1 op n2}")

if op == "+":
    print (f"{n1+n2}")
elif op == "-":
    print (f"{n1-n2}")
elif op == "*":
    print (f"El resultado es {n1*n2}")
elif op == "/":
    print (f"El resultado es {n1/n2}")
else:
    print (f"El resultado es {n1%n2}")
