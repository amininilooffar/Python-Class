a = int(input("first matrix: insert column1 and row 1: "))
b = int(input("first matrix: insert column2 and row 1: "))
c = int(input("first matrix: insert column1 and row 2: "))
d = int(input("first matrix: insert column2 and row 2: "))
print ("matrix 1 is:")
print(a ,b)
print(c, d)

e = int(input("second matrix: insert column1 and row 1: "))
f = int(input("second matrix: insert column2 and row 1: "))
g = int(input("second matrix: insert column1 and row 2: "))
h = int(input("second matrix: insert column2 and row 2: "))
print ("matrix 2 is:")
print(e ,f)
print(g, h)


m11=(a*e)+(b*g)
m12=(a*f)+(b*h)
m21=(c*e)+(d*g)
m22=(c*f)+(d*h)


print("matrix1 * matrix 2 is:")

print (m11 , m12)
print (m21 , m22)


print ("Exercise 3 is done by Niloofar Amini")
