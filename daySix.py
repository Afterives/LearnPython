# Dzień 6 z pythonem
# if, else, while i for

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# Example
a = 33
b = 200
# if i else
if b > a:
    print("Yes, b is greater than a")
else:
    print("a is greater than b")

#elif
b = 33

if b > a:
    print("Yes, b is greater than a")
elif a == b:
    print("a and b are equal")

# "And" keyword
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# "Or" keyword
if a > b or a > c:
    print("At least one of the conditions is True")

# pętla for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# pętla for w stringach
for x in "banana":
    print(x)

# break
for x in fruits:
    print(x)
    if x == "banana":
        break

# continue
for x in fruits:
    if x == "banana":
        continue
    print(x)

# funkcja range

for x in range(6):
    print(x) # wypisze od 0 do 5

for x in range(2, 6):
    print(x) # wypisze od 2 do 5

for x in range(2, 30, 3):
    print(x) # wypisze po kolei 2, 5, 8 itd. do 30

# else w pętli for
for x in range(6):
    print(x)
else:
    print("Finished!")

# pętla for w pętli for
fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for x in fruits:
    for y in adj:
        print(x, y)