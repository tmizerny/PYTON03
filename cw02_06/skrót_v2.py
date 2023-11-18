
name = "United Nations Educational, \nScientific and Cultural Organization"

abbrev = [first for word in name.split() if (first := word[0]).isupper()]
abbrev = ''.join(abbrev)
print(f"Skrót orgaznizacji {name}"
      f" to: {abbrev}")