import random, math
inside = 0
Ntrials = 100000
R = 1
for i in range(Ntrials):
    x = random.random()
    y = random.random()
    if x*x + y*y <= R*R:
        inside = inside + 1
pi = 4*inside/Ntrials
print("Probability to hit inside circle is", inside/Ntrials)
print("Pi is 4 times probability, so", pi)
print("Error = %f" %(pi - math.pi))