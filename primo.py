

import math

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False

    return True


def main():
    numero = int(input("Ingresa un numero: "))

    if es_primo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")


main()