## Autor: Oscar Martinez
## Given an array of integers, find the pair of adjacent elements that has the 
## largest product and return that product.
##     Example
##         For inputArray = [3, 6, -2, -5, 7, 3], the output should be
##         adjacentElementsProduct(inputArray) = 21.
##         7 and 3 produce the largest product.
## 
##         Input/Output
##             [execution time limit] 4 seconds (py3)
## 
##             [input] array.integer inputArray
##             An array of integers containing at least two elements.
##             Guaranteed constraints:
##             2 ≤ inputArray.length ≤ 10,
##             -1000 ≤ inputArray[i] ≤ 1000.
## 
##             [output] integer
##             The largest product of adjacent elements.

## Solucion propuesta:
## Obtener el valor inicial de las posiciones 0 y 1 del arreglo como valor
## maximo inicial y a partir de ahi realizar la multiplicacion de los valores 
## hasta len(inputArray) - 1 ya que si no nos saldremos del arreglo, por ultimo
## regresamos el valor mas grande encontrado

def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) -1):
        if inputArray[i] * inputArray[i + 1] > max:
            max = inputArray[i] * inputArray[i + 1]
    return max

if __name__ == '__main__':
    print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))