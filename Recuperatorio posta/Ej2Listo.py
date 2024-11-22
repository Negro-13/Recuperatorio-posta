lista1 = ["manzana", "banana", "pera", "manzana", "naranja", "pera","pera"]


def countElems(lista1):
    dic = {}
    dic.setdefault('CantPeras', lista1.count('pera'))
    dic.setdefault('CantBananas', lista1.count('banana'))
    dic.setdefault('CantManzanas', lista1.count('manzana'))
    dic.setdefault('CantNaranja', lista1.count('naranja'))
    return dic
print(countElems(lista1))
    