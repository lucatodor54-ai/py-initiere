# //suma cifrelor pare


def suma_cifrelor(n:int)->int:
    suma=0
    while n>0:
        cifra=n%10
        suma=suma+cifra
        n=n//10
    return suma

def suma_cifrelor_pare(n:int)->int:
    suma = 0

    while n>0:
        cifra = n%10
        if cifra % 2 == 0:
           suma = suma+cifra
        n = n//10
    return suma

def ultima_cifra(n:int)->int:
    ultima = n % 10
    return ultima

def numar_cifre(n:int)->int:
    contor = 1
    while n >= 10:
        contor += 1
        n = n // 10
    return contor

def prima_cifra(n:int)->int:
    while n >= 10:
        n = n // 10
    return n

def cifra_maxima(n:int)->int:
    maxim = 0
    while n > 0:
        cifra = n % 10
        if cifra > maxim:
            maxim = cifra
        n = n // 10
    return maxim

def cate_cifre_pare(n:int)->int:
    if(n==0):
        return 1
    contor = 0
    while n >0:
        cifra = n % 10
        if cifra%2==0:
          contor = contor+1
        n = n // 10
    return contor
            








        
    
    

