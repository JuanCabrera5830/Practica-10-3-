def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

def main():
    numero = int(input("Introduce un numero: "))
    resultado = suma_recursiva(numero)
    print("La suma de los digitos es:", resultado)

if __name__ == "__main__":
    main()
