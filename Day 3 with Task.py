txt = "which language is easy"
with open ('sample.txt','a') as file:
    #print(file.read())
     file.write(txt)
print(file.closed)

'''players = {
    "virat": [6, 2, 4, 0, 6, 1],
    "rohit": [6, 1, 0, 2, 6, 4],
    "dhoni": [6, 6, 2, 4, 6, 6]
}

virat = sum(players["virat"])
rohit = sum(players["rohit"])
dhoni = sum(players["dhoni"])

if virat >= rohit and virat >= dhoni:
    highest = "virat"
elif rohit >= virat and rohit >= dhoni:
    highest = "rohit"
else:
    highest = "dhoni"

##

if virat <= rohit and virat <= dhoni:
    lowest = "virat"
elif rohit <= virat and rohit <= dhoni:
    lowest = "rohit"
else:
    lowest = "dhoni"

virat_avg = virat / 6
rohit_avg = rohit / 6
dhoni_avg = dhoni / 6

print("The highest score is", highest)
print("The lowest score is", lowest)

print("virat average:", virat_avg)
print("rohit average:", rohit_avg)
print("dhoni average:", dhoni_avg)
'''


#######


'''players = {
    "virat": [6, 2, 4, 0, 6, 1],
    "rohit": [6, 1, 0, 2, 6, 4],
    "dhoni": [6, 6, 2, 4, 6, 6]
}


for player,scores in players.items():
    print(player)
    players[player] = sum(scores)

print(players)

high_scorer = max(players, key=players.get)
low_scorer = min(players, key=players.get)

print("Highest scorer:", high_scorer, "with", players[high_scorer])
print("Lowest scorer:", low_scorer, "with", players[low_scorer])

#average=scores/6

#print(average)'''


players = {
    "virat": [6, 2, 4, 0, 6, 1],
    "rohit": [0, 1, 0, 2, 6, 4],
    "dhoni": [6, 6, 2, 4, 6, 6],
    "sachin":[6, 4, 2, 0, 1, 2]
}

averages = {}
totals = {}

for player, scores in players.items():
    total = sum(scores)
    average = total / len(scores)

    totals[player] = total
    averages[player] = average

    print(f"{player} Average= {average}")

high_s = max(totals, key=totals.get)
low_s = min(totals, key=totals.get)

print("\nhigh score:", high_s, "with", totals[high_s])
print("low score:", low_s, "with", totals[low_s])


def sum(num):
    sum_result = num*(num+1)/2
    return sum_result

result = sum(11)
print(result)
print(sum(20))

def total(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(total(1,2,3,4,5))


#returning ditionary
def get_user_info():
    user={'name':'vishnu', 'age':42}
    return user

user=get_user_info()
print(user)



#recurion factorial of 5

def fact(num):
    if num ==0:
        return 1
    return num*fact(num-1)

print(fact(6))


#generators

def sq_num(num):
    sq = [ ]
    for i in range(1,num+1):
        sq.append(i*i)
    return sq
print(sq_num(10))

##

def sq_num_gen(num):
    sq = [ ]
    for i in range(1,num+1):
        yield i*i

print(sq_num(10))
sq_gen = sq_num_gen(10)
print(sq_gen)

for i in sq_gen:
    print(i)


#exception handling

'''num = int (input("enter numer"))
den = int (input("enter denom"))

result = num/den
print(result)
print("bye")'''


#try catch method
#print(4/0)
'''try:
    num = int (input("enter numer"))
    den = int (input("enter denom"))
    result = num / den
    print(result)
except ZeroDivisionError:
    print("you cant divide by 0")
except Exception:
     print("some error occu")

print("bye")
'''

try:
    num = int(input("enter number: "))
    den = int(input("enter denom: "))
    result = num / den
    print(result)

except ZeroDivisionError:
    print("you cant divide by 0")

except ValueError:
    print("alphabets are not allowed")

except Exception as e:
    print("some error occurred:", e)

else:
    print(result)

finally:
    print("this always excutes")

print("bye")





 





