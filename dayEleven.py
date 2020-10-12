# Dzień 11 z pythonem
# Data w Pythonie

# Data w Pythonie nie jest typem danych własnym, ale możemy zaimportować moduł o nazwie "datetime" do pracy z datami jako obiekami daty.
import datetime
x = datetime.datetime.now()
print(x)

# Dane wyjściowe
# Kiedy wykonamy kod wyżej pokaże nam się to: 2020-10-12 11:26:37.464483, to pokazuje nam dokładnie rok, miesiąc, dzień, godzine,
# minuty, sekundy i mikrosekundy. Jest wiele metod zwracania informacji o obiekcie daty. Oto kilka przykładów.

print(x.year) # zwraca nam rok
print(x.strftime("%A")) # zwraca nam dzień tygodnia