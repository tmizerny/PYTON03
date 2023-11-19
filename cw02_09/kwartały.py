dane = (
    'styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
    'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad',
    'grudzień')

liczba_elementów = len(dane)
liczba_wieszy = 4
liczba_kolumn = liczba_elementów // liczba_wieszy

kwartały = [[dane[indeks] for indeks in range(liczba_elementów) if indeks//liczba_kolumn == wiersza]
            for wiersza in range(liczba_wieszy)]
print(*kwartały, sep='\n')