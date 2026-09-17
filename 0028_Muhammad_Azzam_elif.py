# logical / boolean Operation
# not, or, xor

print("===NOT===")
a = True
b = not a
print("val a is", a)
print("------------ NOT") 
print("val b is", b)

# OR (jika salah satu true, maka hasilnya adalah true) 
print("===OR===")
a = False
b = False
c = a or b
print("val c is", c)
a = True
b = False
c = a or b
print("val c is", c)
a = False
b = True
c = a or b
print("val c is", c)
a = True
b = True
c = a or b
print("val c is", c)

# AND (jika dua buah nilai true, maka hasil true)
print("===AND===")
a = False
b = False
c = a and b
print("val c is", c)
a = True
b = False
c = a and b
print("val c is", c)
a = False
b = True
c = a and b
print("val c is", c)
a = True
b = True
c = a and b
print("val c is", c)
# XOR (akan true jika salah satu berbeda, sisanya false) 
print("===XOR===")
a = False
b = False
c = a ^ b
print("val c is", c)
a = True
b = False
c = a ^ b
print("val c is", c)
a = False
b = True
c = a ^ b
print("val c is", c)
a = True
b = True
c = a ^ b
print("val c is", c)



# Define the variable by user's input
x = float(
    input("insert a number Less than or Equal of 0\nOR More than or equal to 10: ")
)

# Define another variable with comparative logic
less_or_equal = x <= 0
more_or_equal = x >= 10

# print the thing for verbose
print("Less than or equal to 0?", less_or_equal)
print("More than or equal to 10?", more_or_equal, "\n")

# finalize the calculation and print the result
y = less_or_equal or more_or_equal
print("The number is: ", y)

name = input("Please insert your name: ")

# Kondisi
if name == "Azzam": print("Hello!", name)

# User's input
name = input("Please insert your name: ")

# Kondisi
if name == "Azzam": 
    print("Hello!", name)                          # Fungsi 1
    print("And you looks, alright... I think so.") # Fungsi 2
else:
    print("I do not recognize you!", name)  # Fungsi Else 1
    print("Hence you are ugly nigger!")     # Fungsi Else 2

# Define a Variable
name = input("\nWhat's your name? ")

if name == "Azzam":                             # Statement 1
    print("Heelloooo!", name)
elif name == "Rayyan" or name == "Orca":        # Statement 2
    print(f"Aw Hiii! {name}. my favorite cousin! OwO")              # Mengunakan f-string untuk merapikan outputnya
elif name == "Bima" or name == "Kuronishi":     # Statement 3
    print(f"Hola! {name}. Can we play Palworld again? my friend!")  # Same thing
else:
    print(f"I do not recognize you {name}. GTFO here!")             # Also this



name = input("\nWho's your name? ")
age  = int(input("What's your age? "))

if age <= 12:
    print("your name is:", name, "and you too young for this kiddo")
elif 13 <= age <= 17:
    print("your name is:", name, "and you're currenly a teenager")
elif 18 <= age <= 59:
    print("your name is:", name, "and you're currenly an adult + can legaly vote")
else:
    print("your name is:", name, "and you're currenly a elderly person. also you're probably retired already")

