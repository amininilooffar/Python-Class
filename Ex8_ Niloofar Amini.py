
#Ex.8   069
tuple1= ("Turkey", "Germany", "Poland", "Canada", "Britain")
a = input ("insert one of the countries: Turkey, Germany, Poland, Canada, Britain: ")
print (tuple1.index(a))


#Ex.8  070
tuple1= ("Turkey", "Germany", "Poland", "Canada", "Britain")
a = input ("insert one of the countries: Turkey, Germany, Poland, Canada, Britain: ")
print (tuple1.index(a))
b = int (input ("insert the number of country: "))
print (tuple1[b-1])

#Ex.8   071
list1= ["swimming" , "tennis"]
str1 = str(input ("insert your favorite sport: "))
list1.append(str1)
print(list1)

#Ex.8   072
list1= ["mathematics" , "physics", "chemistry", "algebra", "bilology", "history"]
print (list1)
str2= input("which subject you do not like? ")
list1.remove(str2)
print(list1)

#Ex.8   073
dict1= {}
str1= str(input ("insert your favorite food: 1: "))
dict1.setdefault(1,str1)
str2= str(input ("insert your favorite food: 2: "))
dict1.setdefault(2,str2)
str3= str(input ("insert your favorite food: 3: "))
dict1.setdefault(3,str3)
str4= str(input ("insert your favorite food: 4: "))
dict1.setdefault(4,str4)
print(dict1)
a= int (input("which one you want get rid of? "))
dict1.pop(a)
print (dict1.items())

#Ex.8   074

list1= ["green", "blue", "yellow", "red", "orange", "violet", "pink", "white", "black", "grey"]
a= int (input("enter a number between 0 and 4: "))
b= int (input("enter a number between 5 and 9: "))
print (list1[a:b+1])

#Ex.8   075
list2= [118, 115, 125, 110]
print (list2[0])
print (list2[1])
print (list2[3])
print (list2[2])
a= int (input("insert a number: "))
if a in list2:
    print (list2.index(a))
else:
    print("That is not in the list")


#Ex.8  076

str1 = str(input("insert name of first friend for your party: "))
str2 = str(input("insert name of second friend for your party: "))
str3 = str(input("insert name of third friend for your party: "))
list3= [str1, str2, str3]

str4= input("do you want to add some one else? ")
while str4=="yes":
    str5= input("insert his name: ")
    list3.append(str5)
    str4= input("do you want to add some one else? ")
if str4== "no":
    print (len(list3))

#Ex.8 077

str1 = str(input("insert name of first friend for your party: "))
str2 = str(input("insert name of second friend for your party: "))
str3 = str(input("insert name of third friend for your party: "))
list3= [str1, str2, str3]

str4= input("do you want to add some one else? ")
while str4=="yes":
    str5= input("insert his name: ")
    list3.append(str5)
    str4= input("do you want to add some one else? ")
if str4== "no":
    print (list3)

a = input("type one of the names of the list: ")
print (list3.index(a))
b= input ("do you still want to have him in party? ")
if b== "no":
       list3.remove(a)

print (list3)

#Ex.8  078

listtv= ["american got talent", "dr. Oz", "news", "american idles"]
print(listtv[0])
print(listtv[1])
print(listtv[2])
print(listtv[3])
a= str (input('add another show: '))
b= int (input('where the position? '))
listtv.insert(b,a)
print (listtv)

#Ex.8 079

nums=[]
a= int (input("insert a number: "))
nums.append(a)
print (nums)
b= int (input("insert a number: "))
nums.append(b)
print (nums)
c= int (input("insert a number: "))
nums.append(c)
print (nums)
d= input("do you still want to save the last one to save?")
if d== "no":
    del(nums[2])
    print (nums)

