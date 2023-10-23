# Program do obliczania kapitalizacji odsetek
# po podaniu przez użytkownika stanu konta i długości kapitalizacji odsetek (w latach)

stan_konta = int(input('Podaj początkowy stan konta: '))
lata_kapitalizacji = int(input('Przez ile lat będziesz kapitalizował odsetki?: '))
roczna_stopa_zwrotu = float(input('Podaj roczną stopę zwrotu (w procentach): '))

stan_konta = round(stan_konta * (1+roczna_stopa_zwrotu/100)**lata_kapitalizacji, 2)
print(f'Stan konta po {lata_kapitalizacji} latach kapitalizacji: {stan_konta}')
