# Dzień 5 z pythonem
# Dictionaries, czyli słowniki
# W słownikach używa się kluczy i wartości

# Tworzenie słownika
thisDictionaries = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(thisDictionaries)

# Dostęp do elementów
# Dostęp do elementów możemy sobie zapewnić używająć klucza
x = thisDictionaries["key2"]
print(x)

y = thisDictionaries.get("key2") # Da ten sam efekt co wyżej
print(y)

# Zmiana wartości
thisDictionaries["key2"] = "another_value"
print(thisDictionaries["key2"])

# Wypisanie wartości pętlą for
for x in thisDictionaries:
    print(thisDictionaries[x])

# Jeśli użyjemy metody values() zwróci nam wartośi kluczy słownika
for x in thisDictionaries.values():
    print(x)

# Jeśli użyjemy metody items() wypisze nam i klucz i wartość wszysktich elemetów
for x, y in thisDictionaries.items():
    print(x, y)

# Długość słownika
print(len(thisDictionaries))

# Dodawanie elementów do słownika
thisDictionaries["key4"] = "value4"
thisDictionaries["key5"] = "key5"
print(thisDictionaries)

# Usuwanie elementów z słownika
thisDictionaries.pop("key4")
print(thisDictionaries)