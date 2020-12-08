from array2d import Array2D
from pila import Stack

class LaberintoADT: #crear el laberinto
    """
    0 pasillo, 1 pared, S salida, E entrada
    pasillo es una tupla((2,1), (2,2), (2,3), (2,4), (3,2), (4,2))
    entrada en una tupla (5,2)
    salida(2,5)
    """
    def __init__(self, rens, cols, pasillos, entrada, salida):
        self.__laberinto=Array2D(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0], pasillo[1], '0')
        self.set_entrada(entrada[0], entrada[1])
        self.set_salida(salida[0], salida[1])
        self.__camino=Stack()
        self.__previa=None

    def to_string(self):
        self.__laberinto.to_string()

    def mostrar(self):
        self.__laberinto.to_string()

    """
    establece la entrada de 'E' en la matriz, verificar limites
    """
    def set_entrada(self, ren, col):
        #Terminar validacion de coordenada
        self.__laberinto.set_item(ren, col, 'E')

    """
    Establece salida, dentro de los limites perifericos de la matriz
    """
    def set_salida(self, ren, col):
        #Terminar validacion
        self.__laberinto.set_item(ren, col, 'S')

    def es_salida(self, ren, col): #posicion actual es salida?
        return self.__laberinto.get_item(ren, col)=='S'

    def buscar_entrada(self):
        encontrado=False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon, columna)=='E':
                    self.__camino.push((renglon, columna))
                    encontrado=True
        return encontrado

    def set_previa(self, pos_previa):
        self.__previa=pos_previa

    def get_previa(self):
        return self.__previa

    def imprimir_camino(self):
        self.__camino.to_string()

    def get_pos_actual(self):
        return self.__camino.peek()

    def resolver_laberinto(self):
        actual=self.__camino.peek() #(5, 2)

        #buscar izquierda
        #agregar validaciones para los limites del laberinto
        if actual[1]-1!=-1 and self.__laberinto.get_item(actual[0], actual[1]-1)=='0' and self.get_previa() != (actual[0], actual[1]-1) and self.__laberinto.get_item(actual[0], actual[1]-1) !='X':
            self.set_previa(actual)
            self.__camino.push((actual[0], actual[1]-1))

        #buscar arriba
        elif actual[0]-1!=-1 and self.__laberinto.get_item(actual[0]-1, actual[1])=='0' and self.get_previa() != (actual[0]-1, actual[1]) and self.__laberinto.get_item(actual[0]-1, actual[1]) !='X':
            self.set_previa(actual)
            self.__camino.push((actual[0]-1, actual[1]))

        #buscar derecha
        elif 1==0:
            pass

        #buscar abajo
        elif 1==0:
            pass

        else:
            self.__laberinto.set_item(actual[0], actual[1], 'X')
            self.__previa=actual
            self.__camino.pop()


"""
#prueba
from backtracking import LaberintoADT
import time
pasillos_inicial=(2,1), (2,2), (2,3), (2,4), (3,2), (4,2)
lab=LaberintoADT(6, 6, pasillos_inicial, (5, 2), (2, 5))
lab.buscar_entrada()

lab.to_string()
#imprimir pila
lab.imprimir_camino()
while not lab.es_salida(lab.get_pos_actual()[0], lab.get_pos_actual()[1]):
    lab.resolver_laberinto()
    lab.imprimir_camino()
    time.sleep(1.0)
"""
