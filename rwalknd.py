from random import choice
trials = 1000
steps = 1000
HOME = 0
dim = 3
for i in range(trials):
    point = [0]*dim
    for step in range(steps):
        for j in range(dim):
            point[j]+=choice((-1, 1))
        if point.count(0) == dim:
            HOME+=1
            break
print("Fraction that got home = ", HOME/trials),