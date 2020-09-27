from random import choices
Ntrials = 1000000
limit = 1000
counter = 0
for i in range(Ntrials):
    rand = choices(range(1, limit+1), k=3)
    if rand[0] + rand[1] <= rand[2]:
        counter = counter + 1

print("Fraction =", counter/Ntrials)