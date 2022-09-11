### Clase base de cada documento

from cgitb import text


class File:
    tittle = ''

    lineNumber = 0
    subLineNumber = 0
    charNumber = 0

    lines = {} # dict con todas las instrucciones
    subLines = []
    #subLines = [] # diccionario con listas y referencias de numero de instruccion a la que pertenece
    #extraLines = [] # lista de instrucciones extra con diccionarios y listas de referencia

    #def __init__(s, tittle, lineNumber, subLineNumber, charNumber, lines, sublines, extraLines):
    #    s.tittle = tittle
    #    s.lineNumber = lineNumber
    #    s.subLineNumber = subLineNumber
    #    s.charNumber = charNumber
    #    s.lines = lines
    #    s.subLines = sublines
    #    s.extraLines = extraLines

    def __init__(s, tittle, lineNumber, subLineNumber, charNumber, lines, sublines):
        s.tittle = tittle
        s.lineNumber = lineNumber
        s.subLineNumber = subLineNumber
        s.charNumber = charNumber
        s.lines = lines
        s.subLines = sublines
    
    def __str__(s): # define como debe imprimirse el archivo
        text = ''   
        for line in s.lines:
            text += f'{line}: {s.lines[line]} \n'
            try:
                for sline in s.subLines[line - 1]:
                    text += f'\t {sline}: {s.subLines[line - 1][sline]} \n'
            except:
                ...
        return text
        ...

    def writeLine(s, texto): ## Recibe la instruccion a añadir
        s.lineNumber += 1
        newLine = Line(texto)
        s.lines[s.lineNumber] = newLine
    
    def writeSubLine(s, ind, text):
        try:
            s.subLines[ind][len(s.subLines[ind]) + 1] = Line(text)
        except:
            newsub = {1:Line(text)}
            s.subLines.append(newsub) 

    def deleteLine(s, index):
        old_dict = {} # para almacenar una copia del diccinario

        for key in s.lines:
            old_dict[key] = s.lines[key]
        while index < len(s.lines):
            s.lines[index] = old_dict[index + 1]
            index += 1

        del s.lines[index]        
        del old_dict

    def insertLine(s, index, texto):
        s.lineNumber += 1
        old_dict = {} # para almacenar una copia del diccinario
        for key in s.lines:
            old_dict[key] = s.lines[key]
        s.lines[index] = Line(texto)
        #print('Old dict tiene elemetnos', len(old_dict))
        while index <= len(s.lines):
            index += 1
            try:
                s.lines[index] = old_dict[index - 1]
            except:
                ...


class Line:
    
    text = ''
    #slNummber = 0 # numero de sublineas
    #subLines = {} # {direccion o numero de sublinea: Objeto linea}
    
    def __init__(s, text) -> None:
        s.text = text

    def __str__(s) -> str:
        return str(s.text)
    
    #def addSubLine(s, text):
    #    s.slNummber += 1
    #    newSubLine = Line(text)
    #    s.subLines[s.slNummber] = newSubLine

