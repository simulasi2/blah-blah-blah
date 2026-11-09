from sys import version_info


num_data = [1,2,5,9,10]
print(num_data)

str_data = ["azm","bim","roy","croot"]
print(str_data)

bool_data = [True,False,True,True]
print(bool_data)

mix_data = [1,2,"azm","bim",5,False,10,True,"aaaaaaa",False]
print(mix_data)

range_data = range(1,15,2)
print(range_data)

list_data = list(range_data)
print(list_data)

list_for = [i **2 for i in range(1,11)]
print(list_for)

list_for_if = [i for i in range(1,10) if i != 5]
print(list_for_if)

listLoopCondition = [a **2 for a in range(-5,6) if a != 0] # Skip number 0
print(listLoopCondition)
listLoopCondition = [a **2 for a in range(-5,6) if a == 0]  # Only Show number 0
print(listLoopCondition)
listLoopCondition = [a **2 for a in range(-5,6) if a % 2 != 0]  # Only Show odd number
print(listLoopCondition)
listLoopCondition = [a **2 for a in range(-5,6) if a % 2 == 0]  # Only Show even number
print(listLoopCondition)

# List manipulation
data = ["azm","bim","croot"]

print(f"data pertama (index 0) = {data[0]}")
print(f"data terahir adalah    = {data[-1]}")

data_length = len(data)
print(f"length of data is: {data_length}")
print(f"data sebelum ditambah = {data}")

data.insert(1,"roy")
print(f"data setelah ditambah: {data}")

new_data = ["alfi", "vin", "kevin"]
print(f"Data nama dari = {new_data}\n")
print(f"Index nama dari alfi: {new_data.index("alfi")}")
print(f"Index nama dari vin : {new_data.index("vin")}")

data.extend(new_data)
dataSplit = ''.join(letter for s in data for letter in s)
print(dataSplit)
print(f"How many i(s) on data and new_data: {dataSplit.count("i")}")
print(data)

dataSplitSort = sorted(dataSplit)
print(f"\ndataVar setelah sortir: \n {dataSplitSort}")

dataSplitSortRev = sorted(dataSplit, reverse=True)
print(f"\ndataVar setelah sortir dan di balikan: \n {dataSplitSortRev}")

#change data 
data[2] = "bima"
print(data)

# remove data 
data.remove("croot")
print(data)

# remove last data
data.pop()
print(data)

dataVar = ["azm","bim","croot"]
newData = ["alfi", "vin", "kevin"]
dataVar.extend(newData)

print(f"Typical data: {dataVar}")
nestedData = ["azm","bim","croot",newData]
print(f"The nested one: {nestedData}")

p1 = ["azzam",19,"Laki - Laki"]
p2 = ["alfi",18,"Laki - Laki"]
p3 = ["bim",18,"Laki - Laki"]

listPerserta = [p1,p2,p3]

print(listPerserta, "\n")

for i in listPerserta:
    print(f"Nama\t: {i[0]}")
    print(f"Usia\t: {i[1]}")
    print(f"Gender\t: {i[2]}\n")

vehicle =  ["motorcycle", "car", "Bicycle", "Bus"]
print(vehicle, "\n")
vehicle.append("Truck")
print(f"question a:\n {vehicle}")
vehicle.insert(1,"Tricycle")
print(f"question b:\n {vehicle}")
vehicle.pop()
print(f"question c:\n {vehicle}")
vehicle[vehicle.index("Bicycle")] = "Scooter"
print(f"question d:\n {vehicle}")
print(f"Total of the vehicles is: {len(vehicle)}")

number = [75, 80, 90, 75, 85, 100, 65]

print(f"number 100 is located on index {number.index(100)}")
print(f"The colege student who has grade of 75 is: {number.count(75)} peoples")
number.sort()
print(f"number that the value is smallest to largest: {number}")
number.reverse()
print(f"number that the value is largest to smallest: {number}")

mainCourse = ["Nasi Goreng", "Mie ayam"]
addCourse  = ["Kerupuk", "Ice Tea"]
print(f"The main menu are: {mainCourse}")
print(f"The additional menu are: {addCourse}")
mainCourse.extend(addCourse)
print(f"The menu that'll serve are: {mainCourse}")

items0 = ["Book","5000"]
items1 = ["Pencil","2000"]
items2 = ["Ruler","3000"]

itemsData = [items0,items1,items2]

print(itemsData, "\n")
for i in itemsData:
    print(f"Name\t: {i[0]}")
    print(f"Price\t: {i[1]} IDR\n")    
