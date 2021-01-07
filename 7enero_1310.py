class Queue:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self, elem):
        self.__data.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str(elem) #str() cambiar valores a String
        cadena = cadena + "|"
        return cadena

# tarea priority

class BoundedPriorityQueue:
    def __init__(self, niveles):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def length(self):
        return self.__size

    def enqueue(self, prioridad, elem):
        if prioridad < len(self.__data) and prioridad >= 0:
        #if prioridad < self.length() and prioridad >= 0:
            self.__data[prioridad].enqueue(elem)
            self.__size += 1

    def dequeue(self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size -= 1
                    return nivel.dequeue()

    def to_string(self):
        for nivel in range(len(self.__data)):
            print(f" Nivel {nivel} ---> {self.__data[nivel].to_string()}")


"""
#pruebas_colas

from colas import Queue, BoundedPriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(55)
q1.enqueue(66)
print(q1.to_string())
print("")

print("Prueba 2 de Queue")
c1={"ID": 1, "Nombre": "Jorge", "Balance": 20.5}
c2={"ID": 2, "Nombre": "Mariana", "Balance": 18.0}
c3={"ID": 3, "Nombre": "Alex", "Balance": 1.1}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
sig = atencion.dequeue()
print(f"Bienvenido {sig['Nombre']}, en que podemos servirle hoy")
print(atencion.to_string())

print("")
print("Pruebas de colas con prioridad acotada")
maestres = {"prioridad":4, "descripcion":"Maestre", "personas":["Aemon", "Luwin"]}
niños = {"prioridad":2, "descripcion":"Niños", "personas":["Santi", "Angel"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos", "personas":["Diana", "Maria"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.to_string()

"""
