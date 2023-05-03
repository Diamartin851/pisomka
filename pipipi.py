"""
#abs hodnota
def a(cislo):
    if cislo<0:
        cislo =-1*cislo
    return cislo
print(a(20))
print(a(-20))

#delitele
def pd(cislo):
    vysl=0
    for i in range(1,cislo+1):
        if cislo % i ==0:
            vysl += 1
    return vysl

print(pd(20))



"""
"""
#retazec pocet pismen
def dlzka (retazec):
    pocet = 0
    for i in retazec:
        pocet += 1
    return pocet
print(dlzka("gdig"))

"""
"""
#normal do binarne
cislo=int(input("Zadaj cislo"))                 
binarne=' '
while cislo>0 :
    cifra=cislo%2
    cislo=cislo//2
    binarne=str (cifra) +binarne
print (binarne)
"""

"""
cislo = int(input("Zadaj CISLO:"))
sestnastkove=' '
while cislo>0:
    zvysok=cislo%16
    if zvysok<10:
        cifra=str(zvysok)
    elif zvysok==10:
        cifra="A"
    elif zvysok ==11:
        cifra="B"
    elif zvysok==12:
        cifra="C"
    elif zvysok==13 :
        cifra='D'
    elif zvysok==14:
        cifra="E"
    else:
        cifra="F"
      

    cislo=cislo// 16
    sestnastkove=cifra+sestnastkove
print (sestnastkove)
"""
"""
#milionar
def milionar():
    # Načítanie počiatočného vkladu a ročného úroku
    vklad = float(input("Zadajte počiatočný vklad: "))
    rocny_urok = float(input("Zadajte ročný úrok v percentách: "))
    
    # Výpočet počtu rokov potrebných na to, aby sa stal vkladateľ milionárom
    ciel_castka = 1000000
    roky = 0
    while vklad < ciel_castka:
        vklad *= (1 + rocny_urok/100)
        roky += 1
    
    # Výpis výsledku
    print(f"Vkladateľ bude musieť čakať {roky} rokov, aby sa stal milionárom.")

milionar()
"""
"""
def vypocet_ciferneho_suctu_a_poctu_cifier():
    # Načítanie čísla zo vstupu
    cislo = int(input("Zadajte číslo: "))
    
    # Inicializácia premenných pre ciferný súčet a počet cifier
    ciferny_sucet = 0
    pocet_cifier = 0
    
    # Cyklus pre výpočet ciferného súčtu a počtu cifier
    while cislo > 0:
        # Získanie poslednej cifry
        cifra = cislo % 10
        # Pridanie cifry k cifernému súčtu
        ciferny_sucet += cifra
        # Inkrementácia počtu cifier
        pocet_cifier += 1
        # Odstránenie poslednej cifry z čísla
        cislo //= 10
    
    # Výpis výsledkov
    print(f"Ciferný súčet: {ciferny_sucet}")
    print(f"Počet cifier: {pocet_cifier}")

vypocet_ciferneho_suctu_a_poctu_cifier()
"""
