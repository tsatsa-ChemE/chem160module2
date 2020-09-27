from random import choices
Nrolls = 100
ndice = 5
Sum = 0
for i in range(Nrolls):
    dice = choices(range(1, 7), k=ndice)
    dice.sort(reverse=True)
    Sum = Sum + dice[0] + dice[1]
print("Average roll =", Sum/Nrolls)