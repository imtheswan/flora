# este modulo se encarga de crear todas los archivos pickle y devolverlso
import os
import stone
from editor import division
import pickle

class Alquimia:

    actualDocument = stone.File

    

    def __init__(s, titulo, lineas, lineNumber) -> None:
            s.actualDocument = stone.File(titulo, 0,0,0,{}, [])
            s.actualDocument.lines = lineas
            s.actualDocument.lineNumber = lineNumber

    def list(s, path):
        for files in os.listdir(path):
            if os.path.isfile(os.path.join(path, files)):
                if files[-3:] == 'flr':
                    print(files)
    
    def listDocuments(s): # muestra los archivos tipo .flr
        division()
        print('Archivos para editar')
        division()
        try:
            path = r"."
            s.list(s, path)
                # casa
        except Exception as e:
            print(e)
            ...
    
    def write(s, path, titulo):
        with open(titulo, 'wb') as file:
            pickle.dump(s.actualDocument, file)
        print(' .... Documento guardado como: ', titulo)

    def writeDocument(s): # guarda el archivo
        titulo = f'{s.actualDocument.tittle}.flr'
        try:
            path = r"."
            s.write(path, titulo)
                # casa
        except:
            print(' .... Imposible guardar: ', titulo)

    def delete(s, path, titulo):
        try:
            os.remove(titulo)
            print(' ....',titulo, 'eliminado')
        except Exception as e:
            print(' .... Imposible eliminar', titulo)
            print(e)
    
    def deleteDocument(s): # elimina el archivo
        titulo = input('Nombre del archivo a eliminar: ')
        try:
            path = r"."
            s.delete(s,path, titulo)
                # casa
        except Exception as e:
            print(' .... Imposible eliminar: ', titulo)
            print(e)
    def visualize(s, titulo):
        try:
            with open(titulo, 'rb') as file:
                doc = pickle.load(file)
                division()
                print(doc.tittle)
                division()
                print(doc)
        except Exception as e:
            print(' .... Imposible visualizar', titulo)
            print(' .... Error: ', e)

    def visualizeDocument(s):
        titulo = input('Nombre del archivo a visualizar: ')
        try:
            path = r"."
            s.visualize(s, titulo)
                # casa
        except:
            print(' .... Imposible visualizar: ', titulo)
        

    def getDocument(): #devuelve el archivo para su modificacion
        ...