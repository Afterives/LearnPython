# Dzień 3 z pythonem
# Tuple

# Tupli nie da się modyfikować, np nie możemy usuwać z niej elementów
# Przykład tupli
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

# Dostęp do wartości tupli
print(thisTuple[1]) # banana
print(thisTuple[2]) # cherry
print(thisTuple[-1]) # cherry

# Nie można zmieniać wartości, ale można to obejść takim trickiem

y = list(thisTuple)
y[1] = "kiwi"
thisTuple = tuple(y)
print(thisTuple)

# Pętla for i tuple
for x in thisTuple:
    print(x, end=', ')

# Sprawdzanie czy element tupli jest w niej
if "apple" in thisTuple:
    print("Tak, w tupli jest jabłko")

# Długość tupli
print(len(thisTuple))

# Nie można usunąć elementu z tupli, ale całą tuple można
tupla = ("heheh", "usuwamy")
del tupla
# print(tupla)

# Dodawanie tupli
tupla1 = ("banana", "apple")
tupla2 = ("owoce", "owoc")
tupla3 = tupla1 + tupla2
print(tupla3)

# Metody tupli
print(thisTuple.count("apple")) # zlicza ile jest elementów w tupli