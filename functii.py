# //suma cifrelor pare


def suma_cifrelor(n:int)->int:
    suma=0
    while n>0:
        cifra=n%10
        suma=suma+cifra
        n=n//10
    return suma
