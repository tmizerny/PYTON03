roman_dict = {
    1000: 'M', 900: 'XM', 500: 'D', 400: 'XD', 100: 'C', 90: 'XC', 50: 'L',
    10: 'X', 5: 'V', 4: 'IV', 1: 'I'
}
roman_number = ''
ara_number = int(input("Podaj liczbę arabską w przedziale 1-3999: "))

while ara_number not in range(1, 4000):
    print('Podaj poprawną liczbę!')
    ara_number = int(input("Podaj liczbę arabską w przedziale 1-3999: "))

for key in roman_dict.keys():
    while ara_number >= key:
        ara_number -= key
        roman_number += roman_dict[key]
    if ara_number == 0:
        break
print(roman_number)