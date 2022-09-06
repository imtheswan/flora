import alquimia
import editor

def bienvenida():
    print('''
    Bienvenido a Flora!!
    El editor de texto\n''')

def menu():
    print('''
1] Crear nuevo archivo
2] Editar archivo
3] Listar archivos
4] Visualizar archivo
5] Eliminar archivo
6] Para salir
''')

bienvenida()
menu()

while True:
    en = input(':>  ')
    if en == '1':
        tittle = input("Ingresa el título del archivo: ")
        editor.clear()
        myeditor = editor.Editor(tittle)
        editor.clear()
        bienvenida()
    elif en == '2':
        ...
    elif en == '3':
        alquimia.Alquimia.listDocuments(alquimia.Alquimia)
    elif en =='4':
        alquimia.Alquimia.visualizeDocument(alquimia.Alquimia)
    elif en == '5':
        alquimia.Alquimia.deleteDocument(alquimia.Alquimia)
    elif en == '6':
        exit()
    else:
        print('Opción inváilda')
        menu()
