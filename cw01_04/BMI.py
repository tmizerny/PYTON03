# Program wyliczający BMI dla podanych parametrów wzrostu i wagi

wzrost = float(input('Podaj wzrost(w metrach): '))
waga = float(input('Podaj wagę w (kg dokładność 0.1kg): '))
body_mass_index = waga/(wzrost**2)
body_mass_index = round(body_mass_index, 2)

if body_mass_index < 16.00:
    print(f'Twoje BMI {body_mass_index} wskazuje na wygłodzenie')
elif body_mass_index <= 16.99:
    print(f'Twoje BMI {body_mass_index} wskazuje na wychudzenie')
elif body_mass_index <= 18.49:
    print(f'Twoje BMI {body_mass_index} wskazuje na niedowagę')
elif body_mass_index <= 24.99:
    print(f'Twoje BMI {body_mass_index} wskazuje na wartość prawidłową')
elif body_mass_index <= 29.99:
    print(f'Twoje BMI {body_mass_index} wskazuje na nadwagę')
elif body_mass_index <= 34.99:
    print(f'Twoje BMI {body_mass_index} wskazuje na I stopień otyłości')
elif body_mass_index <= 39.99:
    print(f'Twoje BMI {body_mass_index} wskazuje na II stopień otyłości')
else:
    print(f'Twoje BMI {body_mass_index} wskazuje na III stopień otyłości')

print(f"Prawidłowy zakres wagi dla twojego wzrostu {wzrost}m to\n"
      f"od {round(18.50*wzrost**2,1)} kg do {round(24.99*wzrost**2,1)} kg")
