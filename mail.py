# %Y - rok
# %m - miesiac
# %d - dzien
# %H - godzina
# %M - minuta
# %S - sekunda

from datetime import datetime


lista_zadan = []
zrobione = []
niezrobione = []

print("""MENU
1 - Wcisnij 1 aby dodac zadanie!
2 - Wcisnij aby zobaczyc swoje zadania!
3 - Wcsnij aby oznaczc zadania jako zrobione lub niezrpbione!
4 - Sprawdz czy zadania sa po terminie
5 - Wyswietl wszystkie zadania po terminie
      """)
def  add_a_task():
  #  zad = input("Tu wpisz zadanie jakie masz wykonac")
    zad = input("Tu wpisz zadanie jakie masz wykonac\n")  
    data_user1 = input("Podaj date wykonania zadania (DZIEN.MIESIAC.ROK): ")
    data1 = datetime.strptime(data_user1, "%d.%m.%Y")
    slownik_czyzrobione = {'tresc_zadania' : zad, 'czyzrobione' : False, 'datawykonania': data1 }
    lista_zadan.append(slownik_czyzrobione)

def zaznacz_zrobione():
    ktorezad =  int(input("Ktore zasadanie chcesz oznaczyc?"))
  #  input("wpisz True jesli jest ono zrobione i false jesli nie. ")
    zadanie = lista_zadan[ktorezad-1]
    zadanie['czyzrobione'] = True
  #  print(zadanie)
    print("done")
    
def pokaz_zadan():
    if lista_zadan == []:
        print("Nie dodałeś jeszcze zadnego zadania do swojej listy, kliknij 1, aby to zmienić.")
    for i in range(len(lista_zadan)):
        doneornotdone = ""
        if lista_zadan[i]['czyzrobione'] == True:
            doneornotdone = "done"
        else: 
            doneornotdone = "not done"
        print(f"{i+1} - {lista_zadan[i]['tresc_zadania']} {lista_zadan[i]['datawykonania'].strftime('%d.%m.%Y')}  {doneornotdone}")
#lista_zadan[i]['czyzrobione'] zastepujemy doneornotdone

def zadania_poterminie():
    numer_zad1 = int(input("O ktore zadanie pytasz:"))
    data1 = lista_zadan[numer_zad1-1]['datawykonania']
    data2 = datetime.now()
    if data2>data1:
        print("Zadanie nie zostało wykonane w wyznaczonym terminie")
    elif data2<data1:
        diff = (data1 - data2)
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        print(f"Masz jeszcze {hours} godzin,{minutes} minut,{seconds} sekund czasu na wykonanie zadania")

def wszystkiezad_poterminie(zaznacz_zrobione):
    #zadania_poterminie()
    #range zwraca od 0 
    if zaznacz_zrobione == False:
        print('Zadania po terminie:')
        for index in range(len(lista_zadan)):
            data1 = lista_zadan[index]['datawykonania']
            data2 = datetime.now()
        if data1<data2:
            print(lista_zadan[index]['tresc_zadania'])


#print(lista_zadan[0]['datawykonania']<data5)

def operowanie_menu():
    operator = None
    try:
        operator = int(input("Co chcesz zrobic?"))
    except Exception:
        print("Musza pojawic sie cyfry od 1 do 5, a litery i znaki specjalne nie sa dopuszczane!")
    if operator == 1:
        add_a_task()
    if operator == 2:
        pokaz_zadan()
    #ifchecked()  
    if operator == 3:
        zaznacz_zrobione()
    if operator == 4:
        zadania_poterminie()
    if operator == 5:
        wszystkiezad_poterminie(zaznacz_zrobione=False)

while True:
    operowanie_menu()

#praca domowa - dodaj status czyzrobione zadania jak jesty falsz dodac niezrobione a jak prawda dodaac niezrobione 


# dokonczyc poniedzialek zadanie zamiast daty
# 5 opcja wyswwietlenie wszystkich zadan po terminie zrobic to z uzyciem petli for