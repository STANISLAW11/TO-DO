from datetime import datetime

# %Y - rok
# %m - miesiac
# %d - dzien
# %H - godzina
# %M - minuta
# %S - sekunda

data1 = datetime.strptime("2024-01-01", "%Y-%m-%d")
data2 = datetime.strptime("01.12.2023", "%d.%m.%Y")

# timestamp - to jest po prostu data w postaci numerku

# 2024-01-01 - 1704063600 1704063600.0
# 01.12.2023 - 1701385200 1701385200.0

print(data1 > data2)

print(int(data1.timestamp()))
print(data2.timestamp())
# print(data1.)
