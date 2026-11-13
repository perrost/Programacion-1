while True:
    try:
        dim = int(input("Dimensiones: "))
        if dim <= 0 or (dim % 2 == 0):
            print("Debe ser un numero impar y positivo")
            continue
        break
    except ValueError as error:
        print("Error: ", error)
simbolo = "*"
vacio = " "
for i in range(1,dim+1):
    print(i*simbolo)
print("-"*dim)
for i in range(dim, 0, -1):
    print(i*simbolo)
print("-"*dim)
for i in range(1,dim+1):
    print(vacio*((dim)-i),"*"*i, sep="")
print("-"*dim)
for i in range(dim, 0, -1):
    print(vacio*((dim)-i),"*"*i, sep="")
print("-"*dim)
j = 0
for i in range (1, dim+1, 2):
    
    print(vacio*int(((dim-1)/2)-j), simbolo*i, vacio*int(((dim-1)/2)-j), sep="")
    j +=1