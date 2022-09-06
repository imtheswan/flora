### Clase base de cada documento

from audioop import add
import string


class File():
    tittle = ''

    lineNumber = 0
    charNumber = 0
    instructionNumber = 0
    subinstructionNumber = 0

    lines = [] # lista con todas las instrucciones
    extraLines = [] # lista de instrucciones extra con diccionarios y listas de referencia

    def __init__(s, tittle):
        s.tittle = tittle
        ...
    
    def __str__(s): # define como debe imprimirse el archivo
        texto = ''
        newLines = [] # diccionario de nuevas lineas
        jl = 1 # saltos de linea en una linea
        arras = '' # letras antesde la nueva linea
        return str(s.lines)
        #for line in s.lines:
        #    try:
        #        texto = texto[0:-2] + '\n'
        #    except:
        #        ...
        #    for c in line:
        #        arras += c
        #        if c == '\n':
        #            arras += '\t'
        #    texto += str(jl) + ".\t" + arras
        #    arras = ''
        #    jl += 1
        #return texto

    def writeLine(s, ins, address = [0]): ## Recibe la instruccion a añadir
        if address[0] == 0:
            #print('Natural appending')
            s.lineNumber += 1
            s.lines.append(ins)
        else:
            #print('Not natural')
            sublineNumber = 0
            lineToRun = s.lines
            c = 0
            for direccion in address:
                #print('Starting')
                found = False
                i = 0
                encount = 0
                while not found:
                    #print('Buscando')
                    if type(lineToRun[i]) == list:
                        last = address[-1]
                        encounter = 0
                        for c in address:
                            if c == last:
                                encounter += 1
                        #print('Found list at ', i)
                        sublineNumber += 1
                        #print('Direccion: ', direccion)
                        #print('Numero sublinea:', sublineNumber)
                        if direccion == sublineNumber:
                            encount += 1
                        if direccion == sublineNumber and encount == encounter:
                            #print('Sublinea encontrada')
                            #print('I: ', i)
                            try:
                                if direccion == address[-1]:
                                    lineToRun[i].append(ins)
                                else:
                                    lineToRun = lineToRun[i]
                            except:
                                #print('Probablemente nunca ejecutado')
                                newLine = []
                                lineToRun.append(newLine)
                            sublineNumber = 0
                            i = 0
                            found = True
                            encount = 0
                    if i == len(lineToRun) - 1:
                        if c == len(address) -1:
                            newLine = [ins]
                        else:
                            newLine = []
                        lineToRun.append(newLine)
                        #print('No se encotro, cro nuevo')
                        break
                    #print('Fin de busqueda')
                    i += 1
                c += 1    

    def deleteLine(s, ins):
        ...
    
    def insertLine(s):
        ...