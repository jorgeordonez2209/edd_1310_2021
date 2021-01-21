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

    def remove(self, value):
        #if self.__root == None: #ya lo hace el search
        #    return False #ya lo hace el search
        #else:  #ya lo hace el search
        encontrado = self.search(value)
        #caso 1
        if encontrado.left == None and encontrado.right == None:
            print("Eliminando ", encontrado.data)
            encontrado = None
        #caso 2
        elif (encontrado.left != None and encontrado.right == None) or (encontrado.left == None and encontrado.right != None):
            print("A eliminar: ", encontrdo.data)


"""
#pruebas_abb
from arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)
abb.transversal("in orden")
abb.transversal("pre orden")
abb.transversal("pos orden")
res = abb.search(35)
print(f"El resultado es: {res}")
abb.remove(35)
abb.transversal()

"""
