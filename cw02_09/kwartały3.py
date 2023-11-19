import numpy
dane = (
    'styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
    'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad',
    'grudzień')

liczba_elementów = len(dane)
liczba_wieszy = 4
liczba_kolumn = liczba_elementów // liczba_wieszy

tabela = numpy.array(dane).reshape(liczba_wieszy, liczba_kolumn).tolist()
print(tabela)

