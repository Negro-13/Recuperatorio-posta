lista1 = ["manzana", "banana", "pera", "manzana", "naranja", "pera","pera"]

dic = {}

def countElems(lista1):
    dic.setdefault('CantPeras', lista1.count('pera'))
    dic.setdefault('CantBananas', lista1.count('banana'))
    dic.setdefault('CantManzanas', lista1.count('manzana'))
    dic.setdefault('CantNaranja', lista1.count('naranja'))
    return dic
print(countElems(lista1))
lista = list(countElems(lista1).items())

for i in range(len(lista)):
    archivo = open('conteo_palabras.txt', 'a')
    archivo.write(f'{lista[i]}\n')
    archivo.close()
