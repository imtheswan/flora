import stone

documento = stone.File('Moya')

print('walin')

documento.writeLine("Primera", [0])
documento.writeLine('Segunda', [0])
documento.writeLine('Tercera', [0])
documento.writeLine('Sublinea 1', [1])
documento.writeLine('Nueva sublinea 1', [1])
documento.writeLine('Sublinea 2', [2])
documento.writeLine('Nueva Sublinea 2', [2])

print(documento.lines)
