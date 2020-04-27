#ex7 :012
a = int (input ("insert a number"))
b = int (input ("insert anther number"))
if a > b:
    print (b)
    print (a)
else:
    print (a)
    print (b)

#ex7 :013
c = int (input ("insert a number under 20"))
if c > 20 or c==20 :
    print ("too high")
else:
    print ("thank you")

#ex7 :014
d = int (input ("inter a number between 10 and 20: "))
if d> 10 and d< 20:
    print ("Thank you")
elif d==10:
    print ("Thank you")
else:
    print ("incorrect answer")

#ex7: 015
str1 = input ("insert your favorite color: ")
if str1 == "red" or str1=="Red" or str1=="RED":
    print ("I like red too")
    
else:
    print ("I don't like " + str1 + " , I prefer red")
    
#ex7 :016
str2= str (input ("Is it raining? "))
if str2 == "yes":
    str3= str (input ("Is it windy? "))
    if str3== "yes":
        print ("It is too windy for an umbrella")
    else:
        print ("take an umbrella")
else:
    print ("Enjoy your day")

#ex7 :017
e = int (input ("insert your age: "))
if e > 18 or e == 18:
    print ("you can vote")
elif e == 17:
    print ("you can learn to drive")
elif e == 16:
    print ("you can buy a lottery ticket")
else:
    print ("you can go Trick-or- Treating")

#ex7: 018

f = int (input ( "insert a number: "))
if f < 10:
    print ("Too low")
if f > 9 and f <20:
    print ("correct")
else:
    print ("Too high")
#ex7: 019

g = int (input ("insert 1 or 2 or 3: "))
if g== 1:
    print ("Thank you")
elif g==2:
    print ("well done")
elif g==3:
    print ("correct")
else:
    print ("Error message")

print ("Ex 7 is done by Niloofar Amini")



    

