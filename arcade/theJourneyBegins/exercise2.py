## Autor: Oscar Martinez
## Given a year, return the century it is in. The first century spans from 
## the year 1 up to and including the year 100, the second - from the year 101 
## up to and including the year 200, etc.
## 
##     Example
##     For year = 1905, the output should be centuryFromYear(year) = 20.
##     For year = 1700, the output should be centuryFromYear(year) = 17.
## 
##     Input/Output
##         [execution time limit] 4 seconds (py3)
## 
##         [input] integer year
##         A positive integer, designating the year.
##         Guaranteed constraints:
##         1 ≤ year ≤ 2005.
## 
##         [output] integer
##         The number of the century the year is in.

## Solucion propuesta:
## Obtener el residuo del año entre 100, si el resultado es 0 regresar la 
## division truncada de año entre 100 si no regresar la division truncada de 
## año entre 100 y sumar 1

## Mejor solucion:
## Sumarle 99 al año, esto nos asegura que al realizar la division truncada
## entre 100 el resultado nor arrojara el siglo deseado

## Ejemplo año 1 -> siglo 1
## 1 + 99 = 100 -> 100 // 100 = 1

## Ejemplo año 1908 -> siglo 20
## 1908 + 99 = 2007 -> 2007 // 100 = 20

def centuryFromYear(year):
    if not(year % 100):
        return year // 100
    else:
        return year // 100 + 1

if __name__ == '__main__':
    print(centuryFromYear(54))
    print(centuryFromYear(100))