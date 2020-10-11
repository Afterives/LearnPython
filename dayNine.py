# Dzień 9 z pythonem
# Dziedziczenie

# Dziedziczenie pozwala nam na zdefiniowanie klasy, która dziedziczy wszystkie metody i właściwości z innej klasy.
# Klasa rodzic jest klasą odziedziczoną, nazywamy ją również klasą podstawową.
# Klasa dziecko jest klasą, która dziedziczy po innej klasie, zwanej również klasą pochodną.

# Tworzenie klasy rodzica
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)
# Używam klasy Person, aby utworzyć obiekt, a następnie wykonaj metodę:

p1 = Person("Przemek", "Eeeee")
p1.printname()

# Tworzenie klasy dziecko
#class Student(Person):
#    def __init__(self, fname, lname):
#       Person.__init__(fname, lname)

# Dodawanie funckji __init__ do klasy dziecko
# Po dodaniu funkcji __init__ do klasy dziecka nie będzie dłużej dziedziczyć funkcje __init__ klasy rodzica
# Aby zachować dziedziczenie funkcji rodzica __init__ należy dodać wywołanie funkcji rodzica __init__ (przykład wyżej)

# Używanie funkcji super()
# W Pythonie posiada również funckję super(), która sprawi, że klasa dzieci odziedziczy wszsyskie metody i właściwości po swoich rodzicach.

#class Student(Person):
#    def __init__(self, fname, lname):
#        super().__init__(fname, lname)

# Dodawanie właściwości
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year