type = input('Jeżeli chcesz wyjść wprowadź "q". Jeżeli chcesz przeliczyć z formatu amerykańskiego na europejski - wprowadź "1". '
      'Jeżeli chcesz przeliczyć z formatu europejskiego na amerykański - wprowadź "2": \n')

def us_to_eu():
    print('Przeliczasz spalanie paliwa z formatu amerykańskiego (mpg) na format europejski (l/100km).')
    mpg = float(input("Podaj spalanie w milach na galon: "))
    km = (((100 / mpg) * 3.78) / 1.6)
    print(f"Twoje spalanie w l/100km wynosi: {km}.")

def eu_to_us():
    print('Przeliczasz spalanie paliwa z europejskiego (l/100km) na format amerykański (mpg).')
    km = float(input('Podaj spalanie w litrach na 100 km: '))
    mpg = ((378) / (1.6 * km))
    print(f'Twoje spalanie w milach na galon wynosi: {mpg}')


if type == "1":
    us_to_eu()
if type == '2':
    eu_to_us()
elif type == 'q':
    print('KONIEC')










