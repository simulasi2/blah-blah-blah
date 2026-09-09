# operasi aritmatika

x = 12
y = 11

result = x + y
print("the sum of", x ,"and", y, "is:", result)

result_sub = x - y
print("the substract of", x ,"and", y, "is:", result_sub)

result_multi = x*y
print(x, "multiply by", y, "is:", result_multi)

result_div = x/y
print(x, "divided by", y, "is:", result_div)

result_pow = x**y
print(x, "to the power of", y, "is:", result_pow)

result_modulus = x % y
print(x,'%',y,'=',result_modulus)

result_floor_div = x // y
print(x, '//', y, '=', result_floor_div)

# Temperarture Unit Conversion

print("\n\tUnit Conversion Program\n")

#C = float(input("Insert the temperature in Celcius: "))
C = 29.999
print("The temperature is:", C ,"°C")

R = (4/5) * C
print("The temperature is",R, "°R")

F = ((9/5) * C) + 32 
print("The temperature is",F, "°F")

K = C + 273
print("The temperature is",K, "°K")

# Comparison operation
print("\n\tComparison program\n")
a = 88
b = 11

# greater than >
print("=============== greater than (>)")
res_a = a > 87
res_b = b > 12
print(a, '>', 87, res_a)
print(b, '>', 12, res_b)
res_b = b > 10
print(b, '>', 10, res_b)

# less than <
print("=============== less than (<)")
res_a = a < 87
res_b = b < 12
print(a, '<', 87, res_a)
print(b, '<', 12, res_b)
res_b = b < 10
print(b, '<', 10, res_b)

# greater than or equal ≥
print("=============== greater than or equal (≥)")
res_a = a >= 87
res_b = b >= 11
print(a, '≥', 87, res_a)
print(b, '≥', 11, res_b)
res_b = b >= 12
print(b, '≥', 12, res_b)

# less than or equal ≤
print("=============== less than or equal (≤)")
res_a = a <= 87
res_b = b <= 11
print(a, '≤', 87, res_a)
print(b, '≤', 11, res_b)
res_b = b <= 12
print(b, '≤', 12, res_b)

# equal ==
print("=============== equal (==)")
res_a = a == 88
res_b = b == 11
print(a, '==', 88, res_a)
print(b, '==', 11, res_b)

# not equal !=
print("=============== not equal (!=)")
res_a = a != 88
res_b = b != 11
print(a, '!=', 88, res_a)
print(b, '!=', 11, res_b)

# 'is' sebagai komparasi obj identity (bukan literal)
x = 5
y = 5
res_ls = x is y
print("\nx is y =", res_ls)

# ‘is not’ sebagai komparasi obj identity (bukan literal) 
x = 5 # ini adalah assignment membuat object 
y = 6 
hasil = x is not y 
print("x is not y =",hasil)

# kalulasi luas, volume dan keliling balok
p = 12
l = 5
t = 8

print("\n\tbangunan balok\n")

result_luas_alas  = p*l 
result_luas_permu = 2 * (p*l + p*t + l*t)
result_volume     = p * l * t
result_keliling   = 4 * (p + l + t)

print("luas alas balok: ", result_luas_alas)
print("luas permukaan balok: ", result_luas_permu)
print("volume balok: ", result_volume)
print("keliling balok: ", result_keliling)




comp_vol = result_volume == 480
comp_luas_alas = result_luas_alas > 50

print("vol balok 480? ", comp_vol)
print("luas alas balok > 50? ", comp_luas_alas)


