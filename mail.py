lista_zadan = []
zrobione = []
niezrobione = []
print("""MENU
1 - Wcisnij 1 aby dodc zadanie!
2 - Wcisnij aby zobaczyc swoje zadania!""")
def  add_a_task():
  #  zad = input("Tu wpisz zadanie jakie masz wykonac")
    zad = input("Tu wpisz zadanie jakie masz wykonac")  
    slownik_czyzrobione = {'tresc_zadania' : zad, 'czyzrobione' : False}
    lista_zadan.append(slownik_czyzrobione)

def ifchecked():
    status = int(input("Jezeli wykonales zadanie wpisz 1. oznaczone zostanie jako zrobione, jesli natomiast zadania nie wykonales wpisz 0 oznaczymy je jako niezrobione")) 
    if status == 0:
        niezrobione.append(zad)
        print(niezrobione)
    elif status == 1:
        zrobione.append(zad)
        print(zrobione)
            

def pokaz_zadan():
    for i in range(len(lista_zadan)):
        print(f"{i+1} - {lista_zadan[i]} ")
          

def operowanie_menu():
    operator = int(input("Co chcesz zrobic?"))
    if operator == 1:
        add_a_task()
    if operator == 2:
        pokaz_zadan()
    #ifchecked()  
   

while True:
    operowanie_menu()


#praca domowa - poprawic wypisywanie zadan. Maja sie wyswietlac -  1, zadanie 2. zadanie 3. zadanie w nowych linijkach, ss na kanale generalnym dc

