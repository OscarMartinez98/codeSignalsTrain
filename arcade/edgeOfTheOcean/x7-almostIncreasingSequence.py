## Autor: Oscar Martinez
## Given a sequence of integers as an array, determine whether it is possible 
## to obtain a strictly increasing sequence by removing no more than one 
## element from the array.
## 
## Note: sequence a0, a1, ..., an is considered to be a strictly increasing 
## if a0 < a1 < ... < an. Sequence containing only one element is also 
## considered to be strictly increasing.
## 
##     Example
##         For sequence = [1, 3, 2, 1], the output should be
##         almostIncreasingSequence(sequence) = false.
##         There is no one element in this array that can be removed in order 
##         to get a strictly increasing sequence.
## 
##         For sequence = [1, 3, 2], the output should be
##         almostIncreasingSequence(sequence) = true.
## 
##         You can remove 3 from the array to get the strictly increasing 
##         sequence [1, 2]. Alternately, you can remove 2 to get the strictly 
##         increasing sequence [1, 3].
## 
##     Input/Output
##         [execution time limit] 4 seconds (py3)
## 
##         [input] array.integer sequence
##         Guaranteed constraints:
##         2 ≤ sequence.length ≤ 105,
##         -105 ≤ sequence[i] ≤ 105.
## 
##         [output] boolean
##         Return true if it is possible to remove one element from the array 
##         in order to get a strictly increasing sequence, otherwise return 
##         false.

## Solucion propuesta:
## Algoritmo:
## 1. Si la secuencia es menor a 2 regresar verdadero
## 2. Si la secuencia es estrictamente ascendente regresar verdadero y terminar
## el algoritmo
## 3. Realizar un reordenamiento de la secuencia eliminando un elemento
##  3.1 Recorrer el arreglo de numeros desde 0 hasta n -2
##  Analisis:
##   Al remover un caracter para realizar una secuencia estrictamente
##   ascendente tenemos las siguiente posibilidades de ordenamiento
##                  A   B   C       ✓
##                  A   C   B       -       Eliminar C
##                  B   A   C       -       Eliminar B
##                  B   C   A       -       Eliminar A
##                  C   A   B       -       Eliminar C
##                  C   B   A       x       
##                  A   B   A       -       Eliminar A
##                  A   A   B       -       Eliminar A
##                  B   A   A       -       Eliminar A
##                  A   A   A       x
##   de esta forma nos quedamos con 7 posibles casos para cubrir todas las
##   posibilidades, y hacemos un caso para cada una de ellas
##   3.1.1 Si A es mayor que C y C es mayor que B eliminar C
##   3.1.2 Si B es mayor que A y A es mayor que C eliminar B
##   3.1.3 Si B es mayor que C y C es mayor que A eliminar A
##   3.1.4 Si C es mayor que A y A es mayor que B eliminar C
##   3.1.5 Si A(A) es igual a A(C) eliminar A(A)
##   3.1.6 Si A(A) es igual a A(B) eliminar A(B)
##   3.1.7 Si A(B) es igual a A(C) eliminar A(C)
##   3.1.8 Si entro en alguno de los casos anteriores romper el ciclo
##  3.2 Regresar el arreglo modificado
## 4. Si la secuencia es estrictamente ascendente regresar verdadero y terminar
## el algoritmo
## 5. Regresar falso y terminar el algoritmo

def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True
    if(isSorted(sequence)):
        return True;
    else:
        print(len(sequence))
        sequence = refactor(sequence)
        if(isSorted(sequence)):
            return True
        else:
            return False

def refactor(sequence):
    print(len(sequence)-2)
    for i in range(0, len(sequence) - 2):
        if(sequence[i] == sequence[i + 1]):
            print('Caso A')
            sequence.pop(i)
            break
        elif(sequence[i + 1] == sequence[i + 2]):
            print('Caso B')
            sequence.pop(i + 1)
            break
        elif(sequence[i] == sequence[i + 2]):
            print('Caso C')
            print('{} {}'.format(sequence[i], sequence[i + 2]))
            sequence.pop(i + 2)
            break
        elif(sequence[i + 2] > sequence[i] > sequence[i + 1]):
            print('Caso D')
            sequence.pop(i + 1)
            break
        elif(sequence[i + 1] > sequence[i] > sequence[i + 2]):
            print('Caso E')
            sequence.pop(i + 2)
            break
        elif(sequence[i + 1] > sequence[i + 2] > sequence[i]):
            print('Caso F')
            sequence.pop(i + 1)
            break
        elif(sequence[i] > sequence[i + 2] > sequence[i + 1]):
            print('Caso G')
            sequence.pop(i)
            break
    return sequence

def isSorted(sequence):
    for i in range(0, len(sequence) - 1):
        if(sequence[i] >= sequence[i + 1]):
            return False
    return True

if __name__ == '__main__':
    print(almostIncreasingSequence([1, 3, 2, 1]))