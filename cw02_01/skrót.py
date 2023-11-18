
nazwa = "United Nations Educational, \nScientific and Cultural Organization"
skrot = ' '

for slowo in nazwa.split():
    if slowo[0].isupper():
        skrot += slowo[0]
print(f"Skrót orgaznizacji {nazwa}"
      f" to:{skrot}")