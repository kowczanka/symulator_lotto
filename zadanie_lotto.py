import random

def lotek():

# losowanie i lista z wynikiem losowania:

    lista = list(range(1,50))
    random.shuffle(lista)
    wynik_losowania = [x for x in lista[:6]]

# prosimy gracza o 6 liczb i tworzymy z nich listę liczb:

    liczba_1 = int(input("Podaj liczbę od 1 do 49: "))
    liczba_2 = int(input("Podaj liczbę od 1 do 49: "))
    liczba_3 = int(input("Podaj liczbę od 1 do 49: "))
    liczba_4 = int(input("Podaj liczbę od 1 do 49: "))
    liczba_5 = int(input("Podaj liczbę od 1 do 49: "))
    liczba_6 = int(input("Podaj liczbę od 1 do 49: "))

    skreslenia_na_kuponie = [liczba_1, liczba_2, liczba_3, liczba_4, liczba_5, liczba_6]
    print("Twoje liczby: ", skreslenia_na_kuponie)
    print("Wynik losowania: ", wynik_losowania)

# sprawdenie trafień:

    for liczba in skreslenia_na_kuponie:
        if liczba in wynik_losowania:
            print(f"Twoje trafienia to: {liczba}")

lotek()
