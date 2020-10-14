# Dzień 12 z pythonem
# Try Excpet
# Try blok pozwala przetestować kod pod błędów
# Excpet blok pozwala poradzić sobie jakoś z błędem
# Ostatni blok pozwala na wykonanie kodu, niezależnie od wyniku próby i z wyjątkiem bloków

# Obsługa wyjątków
# Gdy wystąpi błąd lub wyjątek, jak go nazywamy, Python zwykle zatrzyma się i wygeneruje komunikat o błędzie.
# Wyjątki te mogą być obsługiwane za pomocą instrukcji próbnej "try":

try:
    print(x) # Próba wypisania nieistniejącego x
except:
    print("An exception occurred") # Jeśli nie ma go to wypisze ten komunikat w "except"

# Jeśli byśmy próbowali wypisać x bez bloku testowego to pojawiłby się komunikat i program w tym miejscu by
# przestał działać. On dalej się wykona dzięki temu

# Wiele wyjątków
# Można zdefiniować tyle wyjątków ile chcemy, np jeśli chcesz wykonać specjalny blok dla specjalnego rodzaju błędu:
# Przykład
# Wydrukuj jedną wiadomość, jeśli w bloku testowym pojawi się błąd NameError, a drugą w przypadku innych błędów:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else w except
# Możemy użyć słowa kluczowego "else", aby zdefiniować blok kodu, który ma być wykonany, jeśli nie pojawiły się żadne błędy:

try:
    print("Hello")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")

# Finally
# Blok finally, jeśli został określony, zostanie wykonany niezależnie od tego, czy blok testowy spowoduje wystąpienie błędu czy też nie:
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Jest to przydatne do zamykania obiektów i czyszczeniu zasobów:
try:
    f = open("demofile.txt")
    f.write("Lorem Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# Program może być kontynuowany, bez pozostawienia otwartego obiektu pliku

# Raise - zgłaszenie wujątku
# Jako deweloper języka python można zgłosić (raise) wyjątek, jeśli wystąpi warunek. Aby zgłosić (lub podnieść)
# wyjątek , użyj słowa kluczowego "raise".

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Słowo kluczowe "raise" jest używane do podniesienia wukątku. Możesz określić, jaki rodzaj błędu należy podnieść, a
# jaki wydrukować tekst dla do użytkownika

x = "hello"

if not type(x) is int:
    raise  TypeError("Only integers are allowed")