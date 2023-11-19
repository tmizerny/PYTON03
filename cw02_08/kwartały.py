rok = (
    'styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
    'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad',
    'grudzień')

liczba_miesięcy = len(rok)
liczba_kwartałów = 4
długość_kwartału = liczba_miesięcy // liczba_kwartałów

print(początki_kwartałów := rok[::długość_kwartału])