print("Introduceti un numar!","\n\n")
numar = input()
print("Hmm...",numar,"... Sigur",'\n')
numar_v1 = input("Nr = ")
print("Text sau numar =", numar_v1,"\n")
print(type(numar_v1))

a = 5
b = 8
if a < b:
    print("True",'\n')
else:
    print("False",'\n') 
    
x = 5 
y = 10 
z = 8 
print(x > y) 
print(y > z)


x, y, z = 5, 10, 8 

print(x > z,'\n') 
print((y - 5) == x)


x, y, z = 5, 10, 8
x, y, z = z, y, x
print(x > z,'\n')
print((y - 5) == x)



x = 10
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else: print("else"),"\n"




x = "1"

if x == 1:
	print("one")
elif x == "1":
	if int(x) > 1:
        	print("two")
	elif int(x) < 1:
        	print("three")
	else:
        	print("four")
if int(x) == 1:
	print("five")
else:
	print("six"),'\n12'






