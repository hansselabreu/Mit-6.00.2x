import pylab
import random

def montyChoose(guessDoor, prizeDoors):
    doors = set([1,2,3,4])
    prizeDoors = set(prizeDoors)
    guessDoor = set([guessDoor])
    doors_available = doors - prizeDoors
    
    doors_to_choose = list(doors_available - guessDoor)
    return random.choice(doors_to_choose)
##    if guessDoor in prizeDoors:
##    if 1 != guessDoor and 1 != prizeDoor:
##        return 1
##    if 2 != guessDoor and 2 != prizeDoor:
##        return 2
##    return 3

##def randomChoose(guessDoor, prizeDoor):
##    if guessDoor == 1:
##        return random.choice([2,3])
##    if guessDoor == 2:
##        return random.choice([1,3])
##    return random.choice([1,2])
    
def simMontyHall(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoorChoices = [1,2,3,4]
    guessChoices = [1,2,3,4]
    for t in range(numTrials):
        prizeDoorChoices = [1,2,3,4]
        prizeDoors = []
        for i in range(2):
            choised_door = random.choice(prizeDoorChoices)
            prizeDoors.append(choised_door)
            prizeDoorChoices.remove(choised_door)
        guess = random.choice([1, 2, 3, 4])
        toOpen = chooseFcn(guess, prizeDoors)
        if toOpen in prizeDoors:
            noWin += 1
        elif guess in prizeDoors:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)

def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

simResults = simMontyHall(1000000, montyChoose)
displayMHSim(simResults, 'Monty Chooses a Door')
##pylab.figure()
##simResults = simMontyHall(100000, randomChoose)
##displayMHSim(simResults, 'Door Chosen at Random')
pylab.show()
