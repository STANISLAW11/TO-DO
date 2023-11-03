from datetime import datetime

# %Y - rok
# %m - miesiac
# %d - dzien
# %H - godzina
# %M - minuta
# %S - sekunda

data_usera1 = input("Podaj date w formacie M;D;Y: ")
data_usera2 = input("Podaj date w formacie Y.D.M: ")

data1 = datetime.strptime(data_usera1, "%m;%d;%Y")
data2 = datetime.strptime(data_usera2, "%Y.%d.%m")

if data1 > data2:
    print("Data 1 jest pozniejsza")
else:
    print("Data 2 jest pozniejsza")
