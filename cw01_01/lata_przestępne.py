# Program sprawdza czy podany przez użytkownika rok jest przestępny

rok = int(input('Podaj rok do sprawdzenia: '))

czy_rok_przestepny = (rok % 400 == 0) or (rok % 100 != 0 and rok % 4 == 0)
print('Czy rok jest przestępny?', 'Tak' if czy_rok_przestepny else 'Nie')
