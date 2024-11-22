paises = ['Argentina', 'Chile', 'Brasil', 'China', 'Japon', 'Peru', 'Mexico', 'Francia', 'España', 'Italia']

#Las siguientes listas las muestro para var si se ejecuta
paises[0: 2] = ['USA', 'Nigeria', 'Canada']
print(f'Lista modificada: {paises}')

del paises[7:9]
print(f"La lista sin los ultimos 3 paises es: {paises}")

izqPaises = paises[0:5]
derPaises = paises[5:8]
newPaises = ['Bolivia', 'Venezuela']
finalList = izqPaises + newPaises + derPaises

paises = finalList

#listaFinal

print(f'La lista despues de todas las modificaciones es: {paises}')