# Dzień 7 z pythonem
# Funckje

# Tworzenie funkcji - używamy słowa kluczowego def

def my_function():
    print("Hello from a function")

my_function() # tak wywołujemy funckje

# Argumenty funkcji
# Argumenty podaje w nawiasach przy tworzeniu funkcji

def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Przemek")
my_function1("Jarek")

# Parametry a argumenty
# Z perspektywy funkcji: Parametr jest zmienną wymienioną wewnątrz nawiasów w definicji funkcji.
# Argument jest wartością, która jest wysyłana do funkcji podczas jej wywołania.

# Liczba argumentów
# Domyślnie jest tak, że jeśli mamy 2 argumenty musi prz wywołaniu funkcji podać te 2 argumenty,
# w przeciwnym razie wyskoczy nam błąd

def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("Przemek", "Refsnes")

# *args
# Jeśli nie wiem, ile argumentów zostanie przekazanych do funkcji, dodaje * przed nazwą parametru w definicji funkcji.

def my_function3(*kids):
    print("The youngest child is " + kids[1])

my_function3("Emil", "Tobias", "Linus")

# Przekazanie listy jako argumentu

def my_function4(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function4(fruits)

# Zwracanie wartości przez funckje

def my_funciton5(x):
    return x * 5
print(my_funciton5(3))
print(my_funciton5(5))

# Rekurencja
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

print(factorial(5))