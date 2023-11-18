
d = 13
y = int(input('Podaj rok daty: '))
count = 0
# Pętla do sprawdzenia każdego miesiąca
for m in range(1, 13):
    if m < 3:
        z = y - 1
        c = 0
    else:
        z = y
        c = 2
    wynik = (int(23 * m / 9) + d + 4 + y + int(z/4) - int(z/100) + int(z/400) - c) % 7
    # Instrukcja warunkowa do sprawdzenia czy dzien był piątkiem oraz zwiększenie licznika
    if wynik == 5:
        count += 1
        print(f"Numer miesiąca z piątkem trzynastego to: {m}")

print(f"Liczba piątków trzynastego w roku {y} to: {count}")




