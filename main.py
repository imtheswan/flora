import stone
import editor

def bienvenida():
    print('''
    Bienvenido a Flora!!
    El editor de texto\n''')

def menu():
    print('''
1] Crear nuevo archivo
2] Editar archivo
3] Visualizar archivo
4] Eliminar Archivo
5] Para salir
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
        ...
    elif en == '4':
        ...
    elif en == '5':
        exit()
    else:
        print('Opción inváilda')
        menu()
