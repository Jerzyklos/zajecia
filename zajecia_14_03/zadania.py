"""
with open('zad2.txt', 'r', encoding='utf8') as file: #otwieramy plik
    lines = file.readlines() #wrzucacie wszystkie linijki z pliku file do zmiennej lines
    for line in lines: 
        print(line)


Zad. 1
Napisz program, który zsumuje w pliku zad1.txt wszystkie liczby
(każda liczba to nowa linijka). Pamiętaj o dobrym trybie
i zmienieniu tekstu na liczbę, funkcją int().
*Policz średnią. Czy na jej podstawie można stwierdzić,
z jakiego zakresu były losowane liczby?
**Policz, ile liczb jest liczbą pierwszą.
"""
"""
with open('zad1.txt', 'r', encoding='utf8') as file: #otwieramy plik
    lines = file.readlines() #wrzucacie wszystkie linijki z pliku file do zmiennej lines
    suma = 0
    for line in lines: 
        suma += int(line)
    print(suma) #suma
    print(suma/len(lines)) #srednia
"""
"""
#znajdowanie liczby pierwszej
with open('zad1.txt', 'r', encoding='utf8') as file: #otwieramy plik
    lines = file.readlines() #wrzucacie wszystkie linijki z pliku file do zmiennej lines
    for line in lines: 
        liczba = int(line) #czy zmienna liczba jest liczbą pierwszą
        pierwsza = True
        if liczba == 1 or liczba == 2:
            pierwsza = False
        licznik = 2
        while licznik < liczba/2: 
            if liczba%licznik == 0:
                pierwsza = False
            licznik += 1
        if pierwsza == True: #if pierwsza
            print(liczba)
"""
"""
Zad. 2
Policz, ile razy występuje w pliku zad2 słowo 'panie'.
Użyj też formatu utf8, czyli: with open('nazwa pliku', 'r', encoding='utf8')
Żeby sprawdzić, czy danej linijce jest jakieś słowo,
wystarczy użyć: 'panie' in line
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

while True:
    komenda = input()
    if komenda == '1':
        with open('oceny.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    elif komenda == '2': 
        with open('oceny.txt', 'a') as file: 
            nowa_ocena = input('Podaj ocenę: ')
            file.write(nowa_ocena)
            file.write('\n')
    elif komenda == '3': 
        with open('oceny.txt', 'r') as file:
            lines = file.readlines()
            suma = 0
            for line in lines:
                if line != '':
                    suma += int(line)
            print(len(lines))
            print(suma/len(lines))
    elif komenda == '4':
        with open('oceny.txt', 'w+') as file:
            file.write('')
    elif komenda == '0':
        break
"""
Zad. 4
Serializacja! Zrób klasę gracz. Co ma gracz: położenie, listę itemów.
Czyli dodamy je w klasie __init__(). Co robi? Niech ma metodę wypisz,
która wypisze jego położenie i itemy. Niech ma metodę zapisz(), która
zapisze dane do pliku, i metodę wczytaj(), która wczyta dane z pliku.
"""
