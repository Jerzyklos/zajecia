# przypomnienie, jak się robiło funkcje:

#ta zwraca wynik:
def dodaj(a, b): #tutaj w nawiasie są ARGUMENTY funkcji
    wynik = a+b
    return wynik 

#wywołujemy:
wynik = dodaj(2, 3)
print(wynik)

#ta nic nie zwraca:
def wyswietl_czy_dodatnia(a): #tutaj w nawiasie są ARGUMENTY funkcji
    if a >= 0:
        print('dodatnia')
    else:
        print('ujemna')

#wywołujemy:
wyswietl_czy_dodatnia(25)

#przypomnienie pętli w pętli: PRZYDATNE DO ZAD 4 i 5 !
def petla_w_petli():
    for i in range(5):
        print('i = '+str(i))
        for j in range(5):
            print('   j = '+str(j))

#wywolujemy
petla_w_petli()

###########
# ZADANIA
###########

# Zakomentuj wywołania funkcji u góry, jak już je zrozumiesz.

# Zad. 1. Napisz funkcję, która wyświetli listę (każdy element w osobnej linii).
# Użyj indeksów! (czyli nawiasów kwadratowych) i nowej pętli for.
# Funkcja jako argument przyjmuje listę i nic nie zwraca (tylko wyświetla).

# Zad. 2. Napisz funkcję, która zwróci listę, ale do każdego elementu doda 5.
# Użyj indeksów! (czyli nawiasów kwadratowych) i nowej pętli for.
# Funkcja jako argument przyjmuje listę i zwraca listę.

# Zad. 3. Napisz funkcję, która podmieni ze sobą dwa elementy w liście (tzw. swap).
# Czyli np. mamy listę [1, 2, 3, 4] i chcemy podmienić element pierwszy z trzecim,
# czyli element o indeksie 0 i 2. Funkcja je podmieni i zwróci listę [3, 2, 1, 4].
# Wtedy damy tej funkcji w argumentach listę, pierwszy indeks i drugi indeks.
# Funkcja zwróci listę z podmienionymi wartościami.

# Zad. 4. Napisz funkcję, która wyświetli info o tym, czy liczba jest liczbą pierwszą.
# Użyj do tego pętli w pętli. Trzeba zobaczyć dla danej liczby czy ma jakiś dzielnik,
# czyli czy reszta z dzielenia jest równa 0: liczba % i == 0. Robiliście już kiedyś to zadanie :P

# Zad. 5. Napisz funkcję, która jako argument przyjmuje listę, np. [1, 2, 3, 4, 5]
# i wyświetli ją w następujący sposób:
# ---
# 1
# 2
# 3
# 4
# 5
# ---
# 2
# 3
# 4
# 5
# ---
# 3
# 4
# 5
# ---
# 4
# 5
# ---
# 5
#
# Czyli za każdym razem wyświetla o jeden element mniej! Użyj do tego pętli w pętli.




















