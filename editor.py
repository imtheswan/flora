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
:h para desplegar la ayuda; :s para una sublínea; :x para instrucciones extra en la sublinea
Es posible encadenar comandos como
:nwq que agregará una nueva línea, guardará el archivo y abrirá el editor
:i<número> para insertar una linea;
:d<número> para eliminar una linea, siempre usa estos 2 comandos individualmente
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
        s.document = stone.File(tittle,0,0,0,{}, [])
        division()
        print("\t\t", s.document.tittle)
        division()
        instructions()
        division()
        print(s.document)
        s.editor()

    def editor(s): # Recibe la entrada e instrucciones
        inp = input('>  ')
        if len(inp) > 0:
            if(inp[0] == ':'):
                inp = inp[1:len(inp)]
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
        if s.vl >= 2: # Nueva linea
            #s.newLine()
            s.document.writeLine(s.linea)
            s.refresh()
        i = 0
        insert = False
        delete = False
        for command in s.queque:
            if command == 'w': ##Guardar
                alquimia.Alquimia(
                    s.document.tittle, 
                    s.document.lines, 
                    s.document.lineNumber).writeDocument()
            elif command == 'n': ##Nueva linea
                #s.newLine()
                s.document.writeLine(s.linea)
                s.refresh()
            elif command == 'q': # Salir del editor
                exit = 1
            elif command == 'h': # desplegar ayuda
                division()
                instructions()
                division()
            elif command == 's': # Insertar sublinea
                s.document.writeSubLine(s.document.lineNumber + 1, s.linea)
                s.refresh()
            elif command == 'i':
                insert = True
            elif insert:
                try:
                    command = int(command)
                    s.document.insertLine(command, s.linea)
                    s.refresh()
                except:
                    print('Imposible insertar en', command)
                insert = False
            elif command == 'd':
                delete = True
            elif delete:
                try:
                    command = int(command)
                    s.document.deleteLine(command)
                    s.refresh()
                except:
                    print('Imposible eliminar linea', command)
                delete = False
            else:
                print('Comando: ', command, 'no existe')
            i += 1
        s.queque.clear()
        if exit != 1:
            s.editor()

    def newLine(s):
        s.document.writeLine(s.linea)
        s.refresh()

    def refresh(s):
        s.linea = ''
        s.vl = 0
        clear()
        division()
        print('\t\t', s.document.tittle)
        division()
        print(s.document)
