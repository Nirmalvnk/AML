#print statement
#line by line execution
print("Hello!")

#variables
#string
name ="nirmal"
print("Hii" + name.upper())

#num
price = 12
#float
amount= 33.3
print(price*amount)

#bool
Child=True
print(Child)


'''
multiline comment
Hello!
Hiinirmal
399.59999999999997
True
'''

#methods

name="tena"
message="happybirthday"
quote="peace"
print(name.upper())
print(name.lower())
print(name.title())

#concadinate
print(message +" " + name)

print("hello \n world") #split the line
print("hello \t world") #tab space

print(len(message))
print(message.find("y"))
print(message.count("a"))
print(message.replace("a","r"))
print(message.isalpha())
print(message.isdigit())
print(message * 10)

#mulitiple assignment

name,age,height="nirmal", 26, 176
print(height)

like = dislike = 100
print(like)

#casting
otp = 978767
otp=str(otp)
print("your otp is" + otp)
print(type(otp))

count ="20"
print(int(count)+1)



#assignment 1

per="Anand,"
leave=15
year = 2021

print("Dear"+ per + "\n" 
      "You have"+str(leave)+ "days of leave balance for this \n" 
      "Year" + str(year))

#output
'''Enter the nameniurmal
Enter the age26
name is nirmal
age is 26'''


#input
peyar = (input("Enter the name"))
vayasu =(input("Enter the age"))

print("name is " +peyar)
print("age is " + vayasu)


#assignment 2

username=input("Enter your name")
email=input("Enter your email")
phone=input("Enter your phone number")

print("UserName:"+username)
print("Email:"+email)
print("Phone:"+phone)

#output
'''Enter your name nirmal kumar
Enter your email nirmalkumar261126@gmail.com
Enter your phone number9994454271
UserName:nirmal kumar
Email:nirmalkumar@gmail.com
Phone:8804454271'''

#math functions

#paw
#max
#min
#round
#abs

#math.ceil
#math.floor
#math.factorial(9))


import math
n = float(input("Enter a number: "))

log2_n = math.log2(n)
cos_n = math.cos(n)
e_power_n = math.exp(n)

print("Log2(n) =", log2_n)
print("Cos(n)  =", cos_n)
print("e^n     =", e_power_n)

#output
'''Enter a number: 2
Log2(n) = 1.0
Cos(n)  = -0.4161468365471424
e^n     = 7.38905609893065
'''