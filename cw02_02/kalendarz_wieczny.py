# Program do sprawdzania dnia tygodnia dla podanej daty wg algorytmu
# Mike'a Keith'a

d = int(input('Podaj dzień daty: '))
m = int(input('Podaj miesiąc daty: '))
y = int(input('Podaj rok daty: '))

if m < 3:
    z = y - 1
    c = 0
else:
    z = y
    c = 2

wynik = (int(23 * m / 9) + d + 4 + y + int(z/4) - int(z/100) + int(z/400) - c) % 7

dni_tygodnia = ('niedziela', 'poniedziałek', 'wtorek' ,'środa','czwartek', 'piatek' ,'sobota')

print(f'Data {d:2d}/{m:02d}/{y} to {dni_tygodnia[wynik]}')

# match wynik:
#     case 0:
#         print(f'Data {d}/{m}/{y} to niedziela')
#     case 1:
#         print(f'Data {d}/{m}/{y} to poniedziałek')
#     case 2:
#         print(f'Data {d}/{m}/{y} to wtorek')
#     case 3:
#         print(f'Data {d}/{m}/{y} to środa')
#     case 4:
#         print(f'Data {d}/{m}/{y} to czwartek')
#     case 5:
#         print(f'Data {d}/{m}/{y} to piatek')
#     case 6:
#         print(f'Data {d}/{m}/{y} to sobota')
