import math

k = int(input('Ile liczb chcesz skreślić: '))
n = int(input('Spośród ilu liczb: '))
# szansa = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
szansa = math.comb(n, k)
print(f"Szansa trafienia {k} liczb spośród {n} wynosi 1:{szansa}")
