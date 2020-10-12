# Dzień 10 z pythonem
# Moduły, jak się nimi posługiwać

# Czym jest moduł?
# Moduł traktujemy jak bibliotekę kodów. Plik zawierający zestaw funkcji, które chcesz włączyć do swojej aplikacji

# Tworzenie modułu i uzywanie go
# W celu pokazania tworzę plik pomocniczy mymodule.py. W celu zaimportowania modułu do kodu używamy słowa kluczowego "import".

import mymodule
mymodule.greeting("Przemek")

# Wartości w module
# Moduł może zawierać funkcje jak to było wyżej pokazane, ale może zawierać w sobie zmienne wszystkich typów (tablice, słowniki itp.)
print(mymodule.person1)

# Zmiana nazwa modułu
# Aby zmienić nazwę modułu, aby np skrócić jego nazwę używamy słowa kluczowego "as"
import mymodule as mx
a = mx.person1["age"]
print(a)

# Moduły wbudowane
# W pythonie jest wiele modułów wbudowanych, które możesz importować kiedy tylko chcesz, np. moduł "platform"
import platform
x = platform.system()
print(x)

# Używanie funkcji dir()
# Istnieje funkcja wbudowana, która wyświetla listę wszyskitch nazw funkcji (lub nazw zmiennych) w danym module
x = dir(platform)
print(x)

# Import z modułu
# Z modułu możemy importować tylko tą część, co nas interesuje, w tym celu użyjemy słowa kluczowego "from"
from mymodule import person1
print(person1["age"])
