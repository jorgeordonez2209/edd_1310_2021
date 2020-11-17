class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value #sin encapsular
        self.siguiente=siguiente

class LinkedList:
    def __init__(self):
        self.__head=None

    def is_empty(self):
        return self.__head==None

    def append(self, value):
        nuevo=Nodo(value)
        if self.__head==None: # o tambien self.__is_empty()
            self.__head=nuevo
        else:
            curr_node=self.__head #poner curr_node al final de los nodos
            while curr_node.siguiente != None: #poner curr_node al final de los nodos
                curr_node=curr_node.siguiente #poner curr_node al final de los nodos
            curr_node.siguiente=nuevo

    def transversal(self):
        curr_node=self.__head
        while curr_node!=None:
            print(f"{curr_node.data}--> ", end="")
            curr_node=curr_node.siguiente
        print(" ")
# curr_node ->>>> todo el nodo #curr_node.data-->>>> dato que hay en el nodo

    def remove(self, value):
        curr_node=self.__head
        while curr_node.data != value and curr_node.siguiente != None #and--->tomar en cuenta las dos
            curr_node=curr_node.siguiente
        if curr_node.data == value:
