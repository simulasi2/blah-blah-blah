nama   = "Muhammad Azzam"
usia   = 19
berat  = 39.9

print("Nama  :", nama, ", tipe data:", type(nama))
print("Usia  :", usia, ", tipe data:", type(usia))
print("Berat :", berat, ", tipe data:", type(berat) ,"\n\n\n")


while True:
    try:
        data_name = str(input("Enter your Name: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid Name")

while True:
    try:
        data_age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number")

while True:
    try:
        data_weight = float(input("Enter your weight in decimal: "))
        break
    except ValueError:
        print("Invalid input! Please enter your valid number")

print("\nThe data_name type is:", type(data_name))
print("The data_age type is:", type(data_age))
print("The data_weight type is:", type(data_weight), "\n")
print("Your name is   :", data_name)
print("Your age is    :", data_age, "years old")
print("Your weight is :", data_weight ,"Kg")
