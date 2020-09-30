# Dzień 4 z pythonem
# Sety, czyli zbiory

# Zbiór to lista, w której nie ma dwóch identycznch elementów
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Nie możemy uzyskać dostępu poprzez odwołanie się do indeksu setu, za to możemy wypisać elementy dzięki pętli for
for x in thisset:
    print(x)

# Dodawanie elementu do setu
thisset.add("orange")
print(thisset)

# Żeby dodać więcej elemetów do setu używamy update()
thisset.update(["mango", "grapes"])
print(thisset)

# Długość setu
print(len(thisset))

# Usuwanie elementów
thisset.remove("banana")
print(thisset)
thisset.discard("apple") # discard robi to samo co remove, ale nie wywoła błędu, jeśli już nie istnieje element
thisset.discard("apple")
print(thisset)

# Pop
print(thisset)
x = thisset.pop() # usuwa ostatni element setu i zapisuje do zmiennej, możemy wtedy go wywołać
print(thisset)
print(x)