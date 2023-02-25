liczba_elem_do_wys = int(input("Ile elementów chcesz wysłać? "))
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = None
liczba_paczek_wyslanych = 0
waga_aktualnej_paczki = 0
waga_wyslanych_paczek = 0
suma_pustych_kilogramow = 0

for i in range(liczba_elem_do_wys):
    waga_elem = int(input(f"Podaj wagę elementu {i+1}: "))
    if waga_elem < 1 or waga_elem > 10:
        print("Podano nieprawidłową wagę elementu. Koniec dodawania paczek.")
        break
    waga_aktualnej_paczki += waga_elem
    waga_wyslanych_paczek += waga_elem

    if waga_aktualnej_paczki > 20:
        waga_aktualnej_paczki -= waga_elem
        liczba_paczek_wyslanych += 1
        print(liczba_paczek_wyslanych)

        if waga_aktualnej_paczki < waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_aktualnej_paczki
            numer_najlzejszej_paczki = liczba_paczek_wyslanych
            waga_paczki_wyslanej = waga_aktualnej_paczki
        waga_aktualnej_paczki = waga_elem

    elif waga_aktualnej_paczki == 20:
        liczba_paczek_wyslanych += 1
        waga_aktualnej_paczki = 0


        if waga_aktualnej_paczki < waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_aktualnej_paczki
            numer_najlzejszej_paczki = liczba_paczek_wyslanych
            waga_paczki_wyslanej = waga_aktualnej_paczki
            waga_aktualnej_paczki = 0

if waga_aktualnej_paczki > 0:
    liczba_paczek_wyslanych += 1

    if waga_aktualnej_paczki < waga_najlzejszej_paczki:
        waga_najlzejszej_paczki = waga_aktualnej_paczki
        numer_najlzejszej_paczki = liczba_paczek_wyslanych

suma_pustych_kilogramow = 20* liczba_paczek_wyslanych - waga_wyslanych_paczek

if liczba_paczek_wyslanych == 0:
    print("Nie wysłano żadnych paczek.")
else:
    print(f"Wysłano {liczba_paczek_wyslanych} paczek.")
    print(f"Wysłano {waga_wyslanych_paczek} kg.")
    print(f'Suma pustych kilogramów wynosi {suma_pustych_kilogramow} kg')
    print(f"Najlżejsza paczka: paczka nr {numer_najlzejszej_paczki} o wadze {waga_najlzejszej_paczki} kg.")
