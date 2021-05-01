import math
import re

#ER generales para identificar código, números y secuencias alfanuméricas
codigo = r'bcd|gry|ed3|jsn|par|pbt|ham'
numerico = r'[0-9]+'
alfanumerico = r'[a-zA-Z0-9?+]+'
nro_binario = r'(0|1)+'

def base_to_dec(N, b):      # Donde N es el número a convertir y b es la base (0 a 63)
    D = 0                   # Decinal que será entregado
    i = 0                   # Contador que recorre N de manera ascendente
    pos = ( len(N) - 1 )    # Contador que recorre los índices de N, de manera descendente.
    while i < len(N):
        if N[i] in Bd:
            D = D + Bd[N[i]] * pow(Bd[b] , pos)
            i = i + 1
            pos = pos - 1
    return D #(int)


def dec_to_base(D, t):      # Sea D un número decimal y t la base a la cual convertir D
    X = []                  # Sea X una lista que almacenará los dígitos en base b
    R =''                   # R será el string de salida
    while D != 0:
        X.insert(0, ( D % Bd[t] ))
        D = math.trunc( D / Bd[t] )
    R = "".join([str(_) for _ in X])
    return R  #(str)


def bin_to_dec(X):          # Sea X un número binario entregado como str
    D = 0                   # Sea D un número decimal
    i = 0                   # Sea i un contador, posición
    while i < len(X):
        if X[i] == '1':
            D = (D + pow(2,i))
        i = i+1
    return D  #(int)


def dec_to_bin(D):          # Sea D un número decimal
    X = []                  # Sea X una lista que almacenará los dígitos en binario
    R =''                   # R será el string de salida
    while D != 0:
        X.insert(0, (D%2))
        D = math.trunc(D/2)
    R = "".join([str(_) for _ in X])
    return R #(str)


def base_to_bin(N, b)
    return dec_to_bin( base_to_dec(N, b) )


def bin_to_base(N, t)
    return dec_to_base( bin_to_dec(N) , t)


def bcd_algoritm(binary)
    while (len(binary)%4) != 0:
        binary = '0' + binary
    i = 0                       # Contador
    largo = 0                   # Contador para saber cuando terminé de recorrer el binario
    digit = ''                  # String que contendrá grupos de 4 bits
    dec_final = []              # Lista que almacenará el decimal final
    while largo < len[binary]
        while i < 4:
            digit = digit + binary[i]
            i += 1
            largo += 1
        d = bin_to_dec(digit)   # Combertir el grupo de 4 bits en un dígito decimal
        if d > 9:
            return "Entrada invalida"
        else:
            dec_final.append(d)     # Agregar el decimal a la lista
            digit = ''              # Setear el grupo de 4 bits en "0 bits"
            i = 0                   # setear el contador en 0
    D = "".join([str(_) for _ in dec_final])
    return D #(str)



#!OJO ESTE ALG SIRVE CUANDO b ES 2, 10 O BASE HASTA 64 NO PARA CODIGOS!!"!!!!!!!!!"
def apply_bcd(N, b):  # N numero (str) y b actual (current) base of number (str)
    result = ''
    if re.fullmatch(nro_binario, N) and b == '2':
        result = bcd_algoritm(N)
        if result == "Entrada invalida"
            return result
        elif re.fullmatch(numerico, result) and int(result) > 1000:
            return "Entrada invalida"
        else:
            return result
    elif re.fullmatch(numerico, N) and b == '10':
        result = bcd_algoritm( dec_to_bin(N) )
        if result == "Entrada invalida"
            return result
        elif re.fullmatch(numerico, result) and int(result) > 1000:
            return "Entrada invalida"
        else:
            return result
    elif re.fullmatch(alfanumerico, N) and int(b) > 10 and int(b) <= 64:
        result = bcd_algoritm( base_to_bin(N, b) )
        if result == "Entrada invalida"
            return result
        elif re.fullmatch(numerico, result) and int(result) > 1000:
            return "Entrada invalida"
        else:
            return result
    else:
        return "Entrada invalida"


def cod_filter(line):
    num, currbase, endbase = line.split()
    if re.fullmatch(codigo, currbase):
        if re.fullmatch(alfanumerico, num): # Si el número es un alfanumérico y sólo se entrega un código, no sabemos su base
            return "Entrada invalida"
        elif re.fullmatch(numerico, num): # Se entrega un código y el número de entrada es sólo numérico
            if (num[0] == 0):
                if re.fullmatch(nro_binario, num):
                    #!tiene base 2
            else:
                #!tiene base 10
    #todo en cada caso se llama  auna fun distinta. Evaluar casos



######### Main #########
print("\nBienvenido al procesador de codigo de la consola Abyss\n\n")
while True:
    line = input("Ingresar numero valido, base actual y base de destino separados por un solo espacio:\n")
    if '-' == line:
        break
    data = line.split()
    if len(data) != 3:
        print("Entrada invalida")
    elif len(data) == 3:
        Numero, bactual, bfinal = data
        if re.fullmatch(bactual, numerico):
            
    


