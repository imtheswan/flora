from pydoc import doc
import stone

documento = stone.File('MyDoc', 0, 0, 0, {}, [])

documento.writeLine('Primera linea')
documento.writeLine('Segunda Linea')
documento.writeLine('Tercera linea')
documento.writeLine('Cuarta linea')
documento.writeLine('Quinta linea')
documento.insertLine(2, 'Sexta, pero Insertar en segunda')
documento.writeLine('Septima linea')
documento.writeLine('Octava linea')
documento.insertLine(5, 'Novena pero en 5')
print(documento)
documento.deleteLine(2)
documento.deleteLine(5)
documento.writeSubLine(1, 'Primera sublinea')
documento.writeSubLine(2, 'segunda sublinea')
documento.writeSubLine(3, 'tercerfa sublinea')
documento.writeSubLine(1, 'segunda primera sublinea')
print('\n\n')
print(documento)
