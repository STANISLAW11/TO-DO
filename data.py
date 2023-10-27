from datetime import datetime

# %Y - rok
# %m - miesiac
# %d - dzien
# %H - godzina
# %M - minuta
# %S - sekunda

data_usera1 = input("Podaj date w formacie YYYY-MM-DD: ")
data_usera2 = input("Podaj date w formacie DD.MM.YYYY: ")

data1 = datetime.strptime(data_usera1, "%Y-%m-%d")
data2 = datetime.strptime(data_usera2, "%d.%m.%Y")

if data1 > data2:
    print("Data 1 jest pozniejsza")
else:
    print("Data 2 jest pozniejsza")
