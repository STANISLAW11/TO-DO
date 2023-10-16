lista_zadan = []
zrobione = []
niezrobione = []
print("""MENU
1 - Wcisnij 1 aby dodc zadanie!
2 - Wcisnij aby zobaczyc swoje zadania!
3 - Wcsnij aby oznaczc zadania jako zrobione lub niezrpbione!""")
def  add_a_task():
  #  zad = input("Tu wpisz zadanie jakie masz wykonac")
    zad = input("Tu wpisz zadanie jakie masz wykonac")  
    slownik_czyzrobione = {'tresc_zadania' : zad, 'czyzrobione' : False}
    lista_zadan.append(slownik_czyzrobione)

def zaznacz_zrobione():
    ktorezad =  int(input("Ktore zasadanie chcesz oznaczyc?"))
  #  input("wpisz True jesli jest ono zrobione i false jesli nie. ")
    zadanie = lista_zadan[ktorezad-1]
    zadanie['czyzrobione'] = True
  #  print(zadanie)
    print("done")
    

    
            

def pokaz_zadan():
    for i in range(len(lista_zadan)):
        print(f"{i+1} - {lista_zadan[i]['tresc_zadania']} {lista_zadan[i]['czyzrobione']}")

def operowanie_menu():
    operator = int(input("Co chcesz zrobic?"))
    if operator == 1:
        add_a_task()
    if operator == 2:
        pokaz_zadan()
    #ifchecked()  
    if operator == 3:
        zaznacz_zrobione()
   

while True:
    operowanie_menu()

#praca domowa - dodaj status czyzrobione zadania jak jesty falsz dodac niezrobione a jak prawda dodaac niezrobione 

