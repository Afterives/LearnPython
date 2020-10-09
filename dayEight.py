# Dzień 8 z pythonem
# Klasy i obiekty

# Python jest językiem programowania obiektowego, prawie wszystko jest obiektem z jego właściwościami
# i metodami. Klasa jest jako konstruktor lub "plan" do tworzenia obiektów

# Tworzenie klasy
class MyClass:
    x = 5

# Towrzenie obiektu
p1 = MyClass()
print(p1.x)

# funkcja __init__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is {}".format(self.name))

p2 = Person("Przemek", 18)
print(p2.name)
print(p2.age)

# Metody obiektu
# Obiekty w sobie mogą przechowywać metody. Metody w obiektach to funkcje, które należą do obiektu
# Przykład wyżej i wywołanie niżej
p2.myfunc()

# Parametr self
# Jest odniesieniem do bieżącej instancji klasy i jest używany do dostępu do zmiennych należących do klasy.
# Nie musi nazywać się "self", możemy nazwać ją jak chcemy
class Person1:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello, my name is {}".format(abc.name))

p3 = Person1("Jarek", 18)
p3.myfunc()

# Modyfikowanie wartości obiektu
# Zmienie wartość x obiektu p1
p1.x = 10
print(p1.x)