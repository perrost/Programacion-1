def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))

resultado = area_triangulo(base, altura)

print("El area del triangulo es:", resultado)