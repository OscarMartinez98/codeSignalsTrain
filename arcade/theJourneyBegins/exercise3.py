## Autor: Oscar Martinez
## Given the string, check if it is a palindrome.
##     Example
##         For inputString = "aabaa", the output should be
##             checkPalindrome(inputString) = true
##         For inputString = "abac", the output should be
##             checkPalindrome(inputString) = false
##         For inputString = "a", the output should be
##             checkPalindrome(inputString) = true
## 
##         Input/Output
##             [execution time limit] 4 seconds (py3)
## 
##             [input] string inputString
##             A non-empty string consisting of lowercase characters.
##             Guaranteed constraints:
##             1 ≤ inputString.length ≤ 105.
## 
##             [output] boolean
##             true if inputString is a palindrome, false otherwise.

## Usamos un for hasta la primera mitad (truncada) del arreglo, en cada 
## iteracion preguntamos si el caracter coincide con su contraparte, si no es
## asi regresamos un falso, en caso contrario regresamos verdadero, si la
## palabra tiene un numero impar de caracteres ignoramos el caracter de en
## medio.

def checkPalindrome(inputString):
    for index in range(0, len(inputString) // 2):
        if inputString[index] != inputString[len(inputString)-index-1]:
            return False;
    return True

if __name__ == '__main__':
    print(checkPalindrome('abcd'))
    print(checkPalindrome('anitalavalatina'))
