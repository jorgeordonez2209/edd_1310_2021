def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

def printRev(n):
    if n > 0:
        printRev(n - 1)
        print(n)

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    if n > 1:
        return (fibonacci(n - 1) + fibonacci(n - 2))

def main():
    for num in range(1, 11, 1):
        r = factorial(num)
        print(f"El factorial de {num} es {r}")

def main2():
    printRev(20)

def main3():
    for num in range(11):
        print(str(fibonacci(num)) + ",", end="")
    print("")

main3()

####
def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def main():
    datos = [4, 2, 3, 5,9,7,1000]
    res = suma_lista_rec(datos)
    print(res)

main()
