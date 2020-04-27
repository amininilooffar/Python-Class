
# ex.9: 045
b= int (input ("add a number"))

if b > 50:
    print (b)
else:
    t = 0
    while t < 51:
            a= int(input ("add another number: "))
            t = t + a +b
            j= str (t)
            print ("the total is" + j)


# ex.9 : 046

b = int (input ("enter a number: "))
while b < 6:
    b = int (input ('add another number: '))

b = str (b)
print ("the last number you entered was a " + b)

#ex.9 047

d= int (input ("enter a number: "))
e= int (input ("enter another number"))
f= d+e

str1 = str (input ("do you want to add another number? (insert y for yes)"))
if str1 != 'y':
    print(str(f))
else:
    while str1 == 'y':
        g = int (input("enter your number"))
        h= f+g
        str1 = str (input ("do you want to add another number? (insert y for yes)"))
    str3 = str(h)
    print ("the total is: " + str3)

#ex.9 048

compnum=50
a = int(input("enter a number: "))
i=1    
while a!= compnum:
    if a > compnum:
        i+=1
        a=int(input("insert a lower number"))
    else:
        i+=1
        a=int(input("insert a higher number"))

i= str(i)
print("Well done, you took "+i+ " attemps")

#ex.9 049


str1 = str(input ("invite some body to your party: "))
dict1= {1:str1}

print(str1 + " has been invited")

str5= str (input ("do you want to add some one else? "))
while str5 == "yes":
    str6= str (input("insert his/her name: "))
    dict1.setdefault(str6)
    str5= str (input ("do you want to add some one else? "))

print ("your party has: ")
print (len (dict1))

#ex.9 050
a = int(input("enter a number between10 and 20: "))
    
while a>20 or a<10:
    if a > 20:
        a=int(input("Too high, please try again: "))
    elif a<10:
        a=int(input("Too low, please try again: "))

print("Thank you")

#ex.9 051



print ("there are 10 green bottles hanging on the wall, 10 green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")

a=int(input("how many green bottles will be hanging on the wall?: "))

if a>0:
    d=1
    while a!= (10-d):
        a= int (input ("No, try again: "))
    while a == (10-d):
        print ("There will be " + str(a) + "green bottles hanging on the wall")
        print ("there are "+ str(a)+ " green bottles hanging on the wall, "+ str(a)+ "green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")
        d+=1
        a= int (input( "how many green bottles will be hanging on the wall?: "))
        if a ==0:
            break
        while a != (10-d):
            a= int (input ("No, try again: "))

    print("there are no more bottles hanging on the wall")
    


    

    
