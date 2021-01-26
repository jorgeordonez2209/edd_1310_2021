class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        #regla 1
        if self.__root == None:
            self.__root = NodoArbol(value, None, None)
        #regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, no se ingresa nada")
        elif value < nodo.data:
            #regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            #regla 2
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)

    def __recorrdio_in(self, nodo):
        if nodo != None:
            self.__recorrdio_in(nodo.left)
            print(nodo.data, end=", ")
            self.__recorrdio_in(nodo.right)

    def __recorrdio_pre(self, nodo):
        if nodo != None:
            print(nodo.data, end=", ")
            self.__recorrdio_pre(nodo.left)
            self.__recorrdio_pre(nodo.right)

    def __recorrdio_pos(self, nodo):
        if nodo != None:
            self.__recorrdio_pos(nodo.left)
            self.__recorrdio_pos(nodo.right)
            print(nodo.data, end=", ")

    def transversal(self, format="in orden"):
        if format =="in orden":
            self.__recorrdio_in(self.__root)
        elif format == "pre orden":
            print("Recorrido en pre")
            self.__recorrdio_pre(self.__root)
        elif format == "pos orden":
            print("Posorden")
            self.__recorrdio_pos(self.__root)
        else:
            print("Error, ese formato no existe")
        print("")

    def search(self, value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root, value)

    def __search(self, nodo, value):
        if nodo == None: #caso base recursividad
            return None
        elif nodo.data == value: #caso base recursividad
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            #print("Buscar a la izq")
            return self.__search(nodo.left, value)
        else:
            #print("Buscar a la der")
            return self.__search(nodo.right, value)

### 26 de enero 2021
    def remove(self, value):
        if self.__root == None:
            print("Nada que eliminar")
        else:
            self.__remove(None, None, self.__root, value)

    def __remove(self, padre_hi, padre_hd, actual, value):
        if actual == None:
            print("Caso base")
            return None
        elif actual.data == value:
            print("Encontrado: ", actual.data)
            # caso 1: hoja
            if actual.left == None and actual.right == None:
                if padre_hi != None:
                    padre_hi.left = None
                else:
                    padre_hd.right = None
            # caso 2: con un hijo
            if (actual.left != None and actual.right == None) or (actual.left == None and actual.right != None):
                print("Es un nodo con un hijo", actual.data)
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None
            # caso 3: con los ods hijos

            # return actual
        elif value < actual.data:
            print("Buscar a la izquierda")
            self.__remove(actual, None, actual.left, value)
        else:
            print("Buscar a la derecha")
            self.__remove(None, actual, actual.right, value)


"""
from arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)
abb.insert(15)
abb.insert(23)
abb.insert(110)
abb.insert(90)
abb.insert(120)
abb.insert(100)
abb.insert(55)
abb.insert(58)
abb.insert(115)

abb.transversal()
abb.remove(120)
abb.transversal()


"""
