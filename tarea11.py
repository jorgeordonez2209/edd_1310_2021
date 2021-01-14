import time

def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def cuenta_regresiva(value):
    if value >= 0:
        print(str(value) + "...")
        time.sleep(1.0)
        cuenta_regresiva(value - 1)

    if value == 0:
        print("Se acabo el tiempo")

def pila_rec(pila):
    n = len(pila)
    if n%2 == 1:
        print(f"El elemento medio {pila[n//2]} se eliminara")
        pila.remove(pila[n//2])
        
    else:
        i = n//2
        print(f"Los elementos medios {(pila[i], pila[i-1])} se eliminaran")
        pila.remove(pila[i])
        pila.remove(pila[i-1])
        
def main():
    datos = [4, 2, 3, 5, 9, 7, 1000, 2,5,11]
    res = suma_lista_rec(datos)
    print(res)
    

def main2():
    cuenta_regresiva(10)

def main3():
    pila = [2, 7, 6, 3, 1]
    pila2= [13, 2, 6, 87, 22, 56, 1000, 7]
    pila_rec(pila)
    print(pila)
    pila_rec(pila2)
    print(pila2)
    
#main()
main2()
#main3()
