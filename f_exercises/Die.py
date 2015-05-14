import random

def rollDie():
    return random.randint(1, 6)
def simulateDie(trials):
    done = 0
    second_passed = False
    for trial in range(trials):
        if not second_passed:
            a = rollDie()
            b = rollDie()
            if a == b:
                done += 1
        else:
            continue
    return done/float(trials)
import pylab
r = []
for i in range(10000):
    r.append(simulateDie(1000))
pylab.hist(r)
pylab.show()
    
