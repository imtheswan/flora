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

    def __init__(s, tittle): # Ejecuta la secuencia de inicio
        s.document = stone.File(tittle)
        division()
        print("\t\t", s.document.tittle)
        division()
        instructions()
        division()
        print(s.document)
        s.editor()

    def editor(s): # Recibe la entrada e instrucciones
        inp = input('>  ')
        epos = False
        if len(inp) > 0:
            if(inp[0] == ':'):
                inp = inp[1:len(inp)]
                for instruction in inp:
                    s.queque.append(instruction)
                    if instruction != 'e':
                        epos = True
                if 'e' in s.queque and epos:
                    s.queque.clear()

            else:
                s.linea += inp + '\n'
            s.vl = 0
        else:
            s.vl += 1
        s.commandLine()

    def commandLine(s): # Ejecuta las instrucciones
        exit = 0
        if s.vl >= 2:
            s.newLine()
        for command in s.queque:
            if command == 'w':
                alquimia.Alquimia(
                    s.document.tittle, 
                    s.document.lines, 
                    s.document.lineNumber).writeDocument()
            elif command == 'n':
                s.newLine()
            elif command == 'q':
                exit = 1
            elif command == 'h':
                division()
                instructions()
                division()
            elif command == 's':
                ...
            elif command == 'e':
                ...
        s.queque.clear()
        if exit != 1:
            s.editor()

    def newLine(s):
        s.document.writeLine(s.linea)
        s.linea = ''
        s.vl = 0
        clear()
        division()
        print('\t\t', s.document.tittle)
        division()
        print(s.document)
    