"""
Zad. 0
Napisz program, który wyświetli plik zad2.txt. Poznajesz, co to?
"""
"""
Zad. 1
Napisz program, który zsumuje w pliku wszystkie liczby
(każda liczba to nowa linijka). Pamiętaj o dobrym trybie
i zmienieniu tekstu na liczbę, funkcją int().
*Policz średnią. Czy na jej podstawie można stwierdzić,
z jakiego zakresu były losowane liczby?
**Policz, ile liczb jest liczbą pierwszą.
"""
"""
from random import randint
with open('zad1.txt', 'a') as file:
    for i in range(1000):
        file.write(str(randint(1, 1000))+'\n')

with open('zad1.txt', 'r') as file:
    lines = file.readlines()
    suma = 0
    for line in lines:
        suma += int(line)
    print(suma/len(lines))
"""
"""
Zad. 2
Policz, ile razy występuje w pliku zad2 słowo 'panie'.
Użyj też formatu utf8, czyli: with open('nazwa pliku', 'r', encoding='utf8')
Żeby sprawdzić, czy danej linijce jest jakieś słowo,
wystarczy użyć: 'panie' in line
"""
"""
with open('zad2.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()
    suma = 0
    for line in lines:
        if 'panie' in line:
            suma += 1
    print(suma)
"""
"""
Zad. 3
Zrób te które umiesz! Jak masz pytania, zadawaj!
Napisz następujący program:
Jak wciśnie '1', wyświetlą mu się wszystkie wpisane oceny z pliku zad3.txt
Jak użytkownik wciśnie '2', będzie poproszony o wpisanie oceny
do pliku zad3.txt
Jak wciśnie '3', wypisze mu się liczba wprowadzonych ocen i średnia.
Jak wciśnie '0', wyjdzie z programu.
Jak wciśnie '4', wykasuje oceny z pliku.
Użyj pętli while, oraz break żeby wyjść z pętli.
Używaj odpowiednich trybów, w zależności od tego, co chcesz zrobić.
"""
"""
Zad. 4
Serializacja! Zrób klasę gracz. Co ma gracz: położenie, listę itemów.
Czyli dodamy je w klasie __init__(). Co robi? Niech ma metodę wypisz,
która wypisze jego położenie i itemy. Niech ma metodę zapisz(), która
zapisze dane do pliku, i metodę wczytaj(), która wczyta dane z pliku.
"""
"""
Zad. 5 - nie wiadomo czy zrobimy - system walki.
Rozkminiamy razem system walki turowej i piszemy program.

