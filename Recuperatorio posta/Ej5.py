matrix = [[1,2,3],[4,5,6],[7,8,9]]

def sumFilas(matrix):
    count = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            sum = 0
            sum += matrix[x][y]
    return sum

print(sumFilas(matrix))