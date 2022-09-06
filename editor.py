## este modulo controla la parte de escritura e instrucciones del mismo
from os import system
import stone
import alquimia

def division():
        print('--------------------------------------------------------------------------------------------------')

def instructions(): # despliega las instrucciones
        print('''Escribe lo que quieras. Si quieres ingresar un comando escribe ":" antes de él
Ejemplos de comandos son:
:w para guardar; :q para salir; :n para una nueva instrucción o da dos saltos de línea;
:h para desplegar la ayuda; :s para una sublínea; 
:nwq que agregará una nueva línea, guardará el archivo y abrirá el editor
:e<número> para editar una línea o sublínea especifíca;
:d<número> para eliminar una linea, siempre usa estos 2 comandos individualmente
Es posible encadenar comandos como
''')

def clear():
    system("cls")
    print('\b\b')

class Editor():

    queque = [] # lista de instrucciones a ejecutar
    document = stone.File # Este es el documento File de stone
    linea = '' # el texto de La linea que esta siendo modificada
    
    vl = 0 # numero de saltos de linea para nueva linea

    actualSubLine = [] ## indica la dirccion de la linea a editar 1.1,  2.3.4
    writingSubline = False

    def __init__(s, tittle): # Ejecuta la secuencia de inicio
        s.document = stone.File(tittle)
        s.actualSubLine.append(0)
        division()
        print("\t\t", s.document.tittle)
        division()
        instructions()
        division()
        print(s.document)
        s.editor()

    def editor(s): # Recibe la entrada e instrucciones
        print('Línea: ', s.document.lineNumber)
        inp = input('>  ')
        if len(inp) > 0:
            if inp[0] == ':':
                inp = inp[1:len(inp)]
                if inp[0] == 'e' or inp[0] == 'd': # revisar que e o d sean las primeras letras del queque
                    ... 
                for instruction in inp:
                    s.queque.append(instruction)
            else:
                s.linea += inp + '\n'
            s.vl = 0
        else:
            s.vl += 1
        s.commandLine()

    def commandLine(s): # Ejecuta las instrucciones
        exit = 0
        if s.vl >= 2:
            s.document.writeLine(s.linea, [0])
        for command in s.queque:
            if command == 'w':
                alquimia.guardarArchivo(s.document)
            elif command == 'n': # nueva liena
                s.document.writeLine(s.linea, [0])
            elif command == 'q': # salir
                exit = 1
            elif command == 'h': # ayuda
                division()
                instructions()
                division()
            elif command == 's': #sublinea
                s.document.writeLine(s.linea, [s.document.lineNumber])
                s.actualSubLine.append(1)
                ...
            elif command == 'e':
                ...
            elif command == 'd':
                ...
        s.queque.clear()
        if exit != 1:
            s.editor()

### Linea
### Sublínea con index 0 en sublineas 
# [
#    [linea 0
#    [sublienas de sublinea 0]]
#    [liena 1]
#    [linea 2]
# ]
    