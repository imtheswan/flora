### Clase base de cada documento

import string


class File():
    tittle = ''

    lineNumber = 0
    charNumber = 0
    instructionNumber = 0
    subinstructionNumber = 0

    lines = [] # lista con todas las instrucciones
    subLines = [] # diccionario con listas y referencias de numero de instruccion a la que pertenece
    extraLines = [] # lista de instrucciones extra con diccionarios y listas de referencia

    def __init__(s, tittle):
        s.tittle = tittle
        ...
    
    def __str__(s): # define como debe imprimirse el archivo
        texto = ''
        newLines = [] # diccionario de nuevas lineas
        jl = 1 # saltos de linea en una linea
        arras = '' # letras antesde la nueva linea
        for line in s.lines:
            try:
                texto = texto[0:-2] + '\n'
            except:
                ...
            for c in line:
                arras += c
                if c == '\n':
                    arras += '\t'
            texto += str(jl) + ".\t" + arras
            arras = ''
            jl += 1
        return texto

    def writeLine(s, ins): ## Recibe la instruccion a añadir
        s.lineNumber += 1
        s.lines.append(ins)
        ...

    def deleteLine(s, ins):
        ...
        
    #def writeSubLine(s, texto, newlines): ## recibe el indice e instruccion
    #    i = 0
    #    for line in s.subLines:
    #        ind = int(newlines[i])
    #        s.checkSubLine(ind, texto, line)
    #        i += 1
    #
    #def createSubLine(s, texto, ind, reachLine): #reachLines es una lista con la direccion de la sublinea 2.3.1 = [2,3,1]
    #    if type(reachLine[ind]) == list:
    #        ...
    #    else:
    #        s.createSubLine(texto, ind + 1, reachLine)
#
    #def checkSubLine(s, ind,texto, line):
    #    if (type(line) == string):
    #        ...
    #    elif type(line) == list:
    #        ...
    #    if(ind >len(s.subLines)):
    #            newLine = []
    #            newLine.append(ins)
    #            s.subLines.append(newLine)
    #    else:
    #        ...

    def deleteSubLine(s):
        ...

    def insertLine(s):
        ...
    
    def insertSubLine(s):
        ...