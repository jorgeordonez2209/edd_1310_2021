from prueba import Array2D

class JuegoDeLaVida:
    c_viva=1
    c_muerta=0

    def __init__(self, rens, cols, generaciones, poblacion):
        self.largo=cols
        self.alto=rens
        self.grid=Array2D(self.alto, self.largo)
        self.grid.clearing(self.c_muerta)
        self.generaciones=generaciones

        for celula in poblacion:
            self.grid.set_item(celula[0], celula[1], self.c_viva)

    def configura_generacion(self,nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0],celula[1],self.c_viva)

    def imprime_grid(self):
        for r in range(self.grid.get_num_rows()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r,c) == 0:
                    print("░░",end="")
                else:
                    print("▓▓",end="")
            print("")

    def get_num_rows(self):
        return self.alto

    def get_num_cols(self):
        return self.largo

    def set_celula_muerta(self, row, col):
        self.grid.set_item(row, col, self.c_muerta)

    def set_celula_viva(self, row, col):
        self.grid.set_item(row, col, self.c_viva)

    def get_is_viva(self, row, col):
        return self.grid.get_item(row, col)== self.c_viva

    def get_is_muerta(self, row, col):
        return self.grid.get_item(row, col)== self.c_muerta

    def get_numero_vecinos_vivos(self , row , col ):
        limites=[ row-1 , row+1 , col-1 , col+1 ]
        vivos = 0
        limites=self.__ajusta_limites__(limites)
        if row >= 0 and row <= self.alto-1 and col >= 0 and col <= self.largo -1 :
            for r in range(limites[0],limites[1]+1):
                for c in range(limites[2],limites[3]+1):
                    if r == row and c == col:
                        continue
                    else :
                        if self.grid.get_item(r,c) == self.CELULA_VIVA :
                            vivos += 1
        else :
            print("Coordenada la celula fuera del grid")

        return vivos


algo=JuegoDeLaVida[(1,2), (2,1), (2,2), (2,3)]
print(algo)

