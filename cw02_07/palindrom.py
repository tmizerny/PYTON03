text = 'Co mi dał duch? Cud, ład i moc'

palindrom_list = [character.lower() for character in text if character.isalpha()]

if palindrom_list == palindrom_list[::-1]:
    print('Podany tekst jest palindromem')
else:
    print('Podany tekst nie jest palindromem')