import pylab
def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')

##plotData('springData.txt')
##pylab.show()

import random
def testErrors(ntrials = 10000, npts = 100, distribution = random.triangular):
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0 #sum of random points
        for j in xrange(npts):
            s += distribution(-1, 1)
        results[i] = s
    #plot results in a histogram
    pylab.hist(results, bins = 50)
    pylab.title('Sum')
    pylab.ylabel('Number of trials')

pylab.figure(1)
testErrors(ntrials=100000)
pylab.figure(2)
testErrors(ntrials = 100000, distribution = random.triangular)

pylab.show()
