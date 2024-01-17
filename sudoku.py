"""
Determine si un tablero de Sudoku de 9 x 9 es válido. 
Solo las celdas llenas deben validarse de acuerdo con las siguientes reglas:

1) Chequear que el tablero introducido sea un tablero 9x9 
2) Cada fila debe contener los dígitos 1-9 sin repetición.
3) Cada columna debe contener los dígitos 1-9 sin repetición.
4) Cada uno de los nueve subcuadros de 3 x 3 de la cuadrícula debe contener 
los dígitos 1-9 sin repetición. 

"""

#Este seria el tablero donde se realizara el juego, debes reemplazar el '.' por el numero que desees
#Si al ejecutar el codigo, este tira un error que dice ''el tablero ingresado no es valido''
#Se debe a que en alguna fila, columna o subcuadro el numero se encuentra repetido.

board = board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]


class ValidarSudoku:
    def __init__(self,tablero) -> None:
        self.tablero = tablero
        self.listainvertida = list()
        
    def chequeo(self):
        # chequear el tablero introducido sea un 9x9
        assert len(self.tablero) == 9, "el tablero ingresado no es 9x9" #filas
        for fila in self.tablero:
            assert len(fila) == 9, "el tablero ingresado no es 9x9"
    
    def chequeo_filas(self,lista_chequear='tablero_general'):
        if lista_chequear == 'tablero_general':
            lista_chequear = self.tablero
            
        for fila in lista_chequear:
            for elemento in fila:
                if elemento != '.':
                    assert fila.count(elemento) == 1, "el tablero ingresado no es valido"
                    
    
    def chequeo_colum(self):
        for column_index in range (0,9):
            for row_index in range (0,9):
                self.listainvertida.append(self.tablero[row_index][column_index])
            
            self.chequeo_filas([self.listainvertida])
            self.listainvertida.clear()
                    
         
    def chequeo_subcuadros(self):
        #dividimos una gran tarea en pequeñas
        #tenemos 9 sub cuadros, y se chequearia de 3 en 3
        self.chequeo3_subcuadros(0,3)
        self.chequeo3_subcuadros(3,6)
        self.chequeo3_subcuadros(6,9)
        
        
    def chequeo3_subcuadros(self,rang1,rang2):
        self.listainvertida.clear()   
        for column_index in range(0,9):
            if column_index == 3 or column_index == 6:
                self.listainvertida.clear()
            for row_index in range(rang1,rang2):
                self.listainvertida.append(self.tablero[row_index][column_index])
                if len(self.listainvertida) == 9:
                    self.chequeo_filas([self.listainvertida])
        
                          
#instanciar el objeto
sudoku = ValidarSudoku(board)
sudoku.chequeo()
sudoku.chequeo_filas()
sudoku.chequeo_colum()
sudoku.chequeo_subcuadros()
