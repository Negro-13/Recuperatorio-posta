matrix = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [14,14,15,16]]

def suma_diagonales(matrix):
    diagPrincipal = 0
    diagSecond = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x == y:
                diagPrincipal += matrix[x][y]
            if x + y == 3:
                diagSecond += matrix[x][y]
    return diagPrincipal, diagSecond

print(f"La suma de los valores de la diagonal principal es: {suma_diagonales(matrix)[0]}")
print(f"La suma de los valores de la diagonal secundaria es: {suma_diagonales(matrix)[1]}")