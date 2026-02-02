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

#list

cities = ["chennai","madurai","trichy"]
val=[3,4,5,6]
cities[2]="tiruchy"
print(cities[2])

#append adding at the end

cities.append("lawspet")

print(cities)


#insert

cities.insert(1,"thanja")
print(cities)

#delete
del cities[2]
print(cities)

#pop
deleted=cities.pop()
print(deleted+"has been deleted")
print(cities)


city_del ="tiruchy"
cities.remove(city_del)
print(cities)

cities.sort()
print(cities)

cities.reverse()
print(cities)

print(len(cities))

cities.append("chennai")
print(cities)

#while loop
letter=' '
while not letter.isalpha():
    letter=input("enter an alphabet ")
    print("you have entered"+letter)

num=1
while num<=100:
    print(num)
    num+=1 #num=num+1



#for loop
for i in range (1,101):
    print(i)
else:
    print("over")

#list ranging
list(range(1,10))
print(list(range(1,10)))


#guess the number game

import random

num = random.randint(1,20)
guess = int(input("guess the number between 1 to 20"))
while num!=guess:
    if num>guess:
        print("high")
    else:
        print("low")
    guess = int(input("guess again"))
print("you won")

#nested loop
for i in range(1,3):
    for j in range(1,11):
        print(j,end="")
    print('')


#break statement

print("list of numbers, to exit press *")
llist=[]
while True:
    inp=input()
    if inp=="*":
        break
    llist.append(int(inp))
print(llist)


#countinue

kite = "N,I,R,M,A,L"
kite2 = ''
for i in kite:
    if i == ',':
        continue
    kite2 += i   # changed variable name here
print(kite2)


#pass do nothing

ite = "N,I,R,M,A,L"
ite2 = ''
for i in ite:
    if i == ',':
        pass
    else:
        ite+=i


#split and join

htr="abc def ghi jkl mno"
split_list=htr.split('')
print(split_list)

htr_joined='-'.join(split_list)


#copy
india=("tn","kl","ka","ap")
#india_states=("pondy","lawspet","bahour","kathirka")
import copy
india_states=copy.deepcopy(india)

#tuples or immutable cant be changed

tup=(2,3,4)
print(tup)

#tup[1]=5

tup=(3,4,5,5)
print(tup)
print(tup[1])
print(tup.count(5))

for i in tup:
    print(i)

if 3 in tup:
    print('yes')



#dictionary

user ={'name':"Ram", 'age':23, 'gender':"male"}
print(user['name'])

user['city']="chennai"
print(user)

user['age']=26
print(user)

del user['gender']
print(user)


 #set

colors={'blue','green','red'}
print(colors)

color_list=list(colors)
print(color_list)


#string formatting

name='hari'
like1='apple'
like2='banana'

text ='{} like {} and {}'
print(text.format(name,like1,like2))












