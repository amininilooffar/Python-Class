#exercise 5

#kabise:

def Julian_date (d, m , y):
	days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
	passed = 0
	if y%4==0 or (y%4==0 and y%100!=0):
		days[1]=29
	for months in days [:m-1]:
		passed+= months
	passed += d
	return passed

#pos(n)

def pos(n):
    for i in range(n+1):
            print (i)
        

#do adad bakhshpazir

def div (num1 , num2):
   if num2%num1==0 or num1%num2==0:
       return "bakhsh pazir"
   else:
         return "bakhsh pazir nist"

#adade aval
"tamrin 4"

def prime (num):
    limit = int(num**0.5)
    for i in range(limit):
            if num %i == 0:
             return "aval nist"
    return "aval ast"

    

    
