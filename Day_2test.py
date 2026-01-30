#if else
'''pwd=input("password:")

if pwd == "Nirmal":
    print("password is corrrect")
else:
    print("password  is wrong")'''

#relational operators
#>
#<
#>=
#<=
#==
#!=

#assignment
num =35
if num%10==0:
    print(str(num)+"is multiple of ten")
else :
    print(str(num)+"is not multiple ten")


#elif ladder

'''ind_score=int(input())

if ind_score >=350:
    print("india will win")
elif ind_score >=250:
    print("doubt to win")
elif ind_score >=150:
    print("doubt to win")
else:
    print("aus win")'''


#nestedif
num=int(input("enter the number"))

if num>99 and num<1000:
    if num%2==0:
        print(str(num)+"is three digit even")
else:
    print(str(num) + "is not three digit even")


#logical operator
name = "Nirmal"
if name[0]=="n" or name[0]=="N":
    print("name starts with N")

#bitwise operator
'''
& and
| or
~ not
^ exor
<< left shift
>> right shift'''

#string Slicing
#str[start:stop:step]
cname="Logic First"

print(cname[3])
print(cname[1:4])
print(cname[0:7:2])
print(cname[-2:-5:-1])
print(cname[::-1])

x=slice(2,-2)
print(cname[x])


#assignment

fun = "Happy"

print(fun[0])
print(fun[0:2])
print(fun[0:3])
print(fun[0:4])
print(fun[0:5])
print(fun[-1])
print(fun[-2:])
print(fun[-3:])
print(fun[-4:])
print(fun[-5:])







