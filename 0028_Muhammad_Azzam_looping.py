# LOOOOPING

num = [0,1,2,3,4,5,6]
print(num)

for i in num:
    print(f"i currenly in {i}")
print("Done")

# Or use range() function
num1 = range(6)
for i in num1:
    print(f"i currenly in {i}")
print("End of line")

num2 = range(1,10)
for i in num2:
    print(f"i currenly in {i}")
print("End of line")

var_str = "awkjdiaw"

for i in var_str:
    print(i)
else:
    print("done executing\n")

for i in var_str:
    print(i)
    if i == "d":
        break
else:
    print("done executing\n")

print("\nExample 1\n")

num = 5
while num > 0:
    print("nigger")
    num = num - 1

# Pass
num = 0
while num < 5:
    num = num + 1
    if (num == 3):
        pass
    print(num)


# Continue 
num = 0
print(f"Current number is: {num}")

while num < 5:
    num += 1
    print(f"now the number is: {num}")

    if (num == 3):
        continue
    print("hi")

print("done\n\n")


# Break 
num = 0
print(f"Current number is: {num}")

while num < 5:
    num += 1
    print(f"now the number is: {num}")

    if (num == 3):
        print("n00b")
        break
    print("hi")

print("\ndone")

side  = 100
count = 2

while True:
    print("*" * count)
    count = count * 2
    if count >= side:
           break

num = range(51)

for i in num:
    # Just some fallback
    if (i == 0): continue

    # The main func
    if (i % 2 == 0):
        print(f"The {i} is even number")
    else:
        print(f"The {i} is odd number")

num = range(100)

for a in num:
    # define a default value 
    prime = True

    # some fallback
    if a < 2:
        prime = False

    for b in range(2, int(a**0.5) + 1):
        # real condition
        if a % b == 0:
            prime = False
            break

    if prime: 
        print(f"The {a} is prime number")
else:
    print("Done")
