rok = (
    'styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
    'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad',
    'grudzień')

liczba_miesięcy = len(rok)
liczba_kwartałów = 4
długość_kwartału = liczba_miesięcy // liczba_kwartałów

kwartały = [[miesiąc for nr_miesiąca,miesiąc in enumerate(rok) if nr_miesiąca//długość_kwartału == nr_kwartału]for nr_kwartału in range(liczba_kwartałów)]
print(kwartały)