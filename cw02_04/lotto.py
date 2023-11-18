import math

k = int(input('Ile liczb chcesz skreślić: '))
n = int(input('Spośród ilu liczb: '))
# szansa = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
#szansa = math.comb(n, k)
#print(f"Szansa trafienia {k} liczb spośród {n} wynosi 1:{szansa}")

wynik1 = 1
wynik2 = 1
# Różnica n i k jest stała
DELTA = n - k

for index in range(1, k+1):
    wynik1 *= index
    wynik2 *= index + DELTA

print(wynik2//wynik1)