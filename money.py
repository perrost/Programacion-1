#calcula del dinero sobrante de una compra

precio = int(input("Ingrese el precio del artículo: "))
pagado = int(input("Ingrese el importe pagado: "))

cambio = pagado - precio

print("\nCambio:", cambio, "pesos")

billetes_500 = cambio // 500
cambio = cambio % 500

billetes_200 = cambio // 200
cambio = cambio % 200

billetes_100 = cambio // 100
cambio = cambio % 100

billetes_50 = cambio // 50
cambio = cambio % 50

billetes_20 = cambio // 20
cambio = cambio % 20

monedas_10 = cambio // 10
cambio = cambio % 10

monedas_5 = cambio // 5
cambio = cambio % 5

monedas_2 = cambio // 2
cambio = cambio % 2

monedas_1 = cambio

print("\nDesglose del cambio:")
print("Billetes de $500:", billetes_500)
print("Billetes de $200:", billetes_200)
print("Billetes de $100:", billetes_100)
print("Billetes de $50:", billetes_50)
print("Billetes de $20:", billetes_20)
print("Monedas de $10:", monedas_10)
print("Monedas de $5:", monedas_5)
print("Monedas de $2:", monedas_2)
print("Monedas de $1:", monedas_1)