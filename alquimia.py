# este modulo se encarga de crear todas los archivos pickle y devolverlso
import os
import stone
from editor import division
import pickle

class Alquimia:

    actualDocument = stone.File

    path = r'C:\\Users\\Road\\'

    def __init__(s, titulo, lineas, lineNumber) -> None:
            s.actualDocument = stone.File(titulo)
            s.actualDocument.lines = lineas
            s.actualDocument.lineNumber = lineNumber
    
    def listDocuments(s): # muestra los archivos tipo .flr
        division()
        print('Archivos para editar')
        division()
        for files in os.listdir(s.path):
            if os.path.isfile(os.path.join(s.path, files)):
                if files[-3:] == 'flr':
                    print(files)
    
    def writeDocument(s): # guarda el archivo
        titulo = f'{s.actualDocument.tittle}.flr'
        try:
            with open(s.path + titulo, 'wb') as file:
                pickle.dump(s.actualDocument, file)
            print('Documento guardado como: ', titulo)
        except:
            print('Imposible guardar: ', titulo)
    
    def deleteDocument(s): # elimina el archivo
        titulo = input('Nombre del archivo a eliminar: ')
        try:
            os.remove(os.path.join(s.path, titulo))
        except:
            print('Imposible eliminar', titulo)

    def visualizeDocument(s):
        titulo = input('Nombre del archivo a visualizar: ')
        try:
            with open(s.path + titulo, 'rb') as file:
                doc = pickle.load(file)
                division()
                print(doc.tittle)
                division()
                print(doc)
        except:
            print('Imposible visualizar', titulo)

    def getDocument(): #devuelve el archivo para su modificacion
        ...