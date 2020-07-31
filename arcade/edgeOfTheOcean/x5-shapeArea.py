## Autor: Oscar Martinez
## Below we will define an n-interesting polygon. Your task is to find the 
## area of a polygon for a given n.
## 
## A 1-interesting polygon is just a square with a side of length 1. An 
## n-interesting polygon is obtained by taking the n - 1-interesting polygon 
## and appending 1-interesting polygons to its rim, side by side. You can see 
## the 1-, 2-, 3- and 4-interesting polygons in the picture attached.
## 
##     Example
##         For n = 2, the output should be
##         shapeArea(n) = 5;
##         For n = 3, the output should be
##         shapeArea(n) = 13.
##     
##     Input/Output
##         [execution time limit] 4 seconds (py3)
## 
##         [input] integer n
##         Guaranteed constraints:
##         1 ≤ n < 104.
## 
##         [output] integer
##         The area of the n-interesting polygon.

## Solucion propuesta: el cuadro principal se compone de dos subcuadrados
## normales de n y n - 1 donde n es el numero dado, por lo que para obtener el
## patros solicitado solo debemos sumar los cuadrados de n y n-1

def shapeArea(n):
    return n ** 2 + (n - 1) ** 2

if __name__ == '__main__':
    print(shapeArea(1))
    print(shapeArea(2))
    print(shapeArea(3))
    print(shapeArea(4))
    print(shapeArea(5))