# Dzień 2 z pythonem
# Tablice (bądź inaczej listy)

tablica = []
tablica.append(1)
tablica.append(2)
tablica.append(3)
print(tablica[0]) # wypisze 1
print(tablica[1]) # wypisze 2
print(tablica[2]) # wypisze 3

# wypisze kolejno 1, 2, 3, w szereg
print(tablica)
print(tablica[0] + tablica[2])

tupla = input("Podaj liczby odzielone przecinkami: ")
lista = [] # deklaracja pustej listy

for x in range(len(tupla)):
    lista.append(tupla[x])

print("Elementy i ich indeksy: ")
for i, v in enumerate(lista):
    print(v + " [",i,"]")

# lista odwrócona
print("Elementy w odwróconym porządku")
for x in reversed(lista):
    print(x, end=', ')
print()
# lista posortowana rosnąco
print("Elementy posortowane")
for x in sorted(lista):
    print(x, end=", ")

# usuwanie elementu z listy
u = input("Którą element usunąć?: ")
lista.remove(u)
print(lista, end=", ")

# dodawanie elementu do listy i wstawianie go przed indeksem
a, i = input("Podaj element do dodania i indeks, przed którym ma się znaleźć: ")
lista.insert(i, a)
print(lista)