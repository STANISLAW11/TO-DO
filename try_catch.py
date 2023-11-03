

try:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = a / b # 10 / 0
    print(c)
except Exception:
    print("Nie dziel przez zero!")
