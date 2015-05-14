def throwNeedles(numNeedles):
    inCircle = 0
    for needles in xrange(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**5 < 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))
