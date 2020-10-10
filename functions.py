import random as rand
import matplotlib.pyplot as plt
from math import sqrt

#x = 9, y = 3
#posi = [m, n]
#range of m = [(2/5 * x) - x]; n = [(2/11 * y) - y]
def fitFunc(posi, x, y):
    fitness = (x * y) // (posi[0] * posi[1])
    return fitness

def compFit(posi1, posi2, x, y):
    fit1 = fitFunc(posi1, x, y)
    fit2 = fitFunc(posi2, x, y)
    if fit1>fit2:
        return posi1
    else:
        return posi2

def calAvgFitDiff(x, y, particles):
    meanFit = sum([fitFunc(p.posi, x, y) for p in particles]) / len(particles)
    fitDiff = [abs(fitFunc(p.posi, x, y) - meanFit) for p in particles]
    avgFitDiff = sum(fitDiff) / len(particles)
    return avgFitDiff

def calAvgPosiDiff(x, y, particles):
    meanPosi = [sum([p.posi[0] for p in particles]) / len(particles), sum([p.posi[1] for p in particles]) / len(particles)]
    posiDiff = [sqrt((p.posi[0] - meanPosi[0])**2 + (p.posi[1] - meanPosi[1])**2) for p in particles]
    avgPosiDiff = sum(posiDiff) / len(particles)
    return avgPosiDiff

def plotGraph(plot, particles, x, y, lengthLim):
    s = plot.scatter([p.posi[0] for p in particles], [p.posi[1] for p in particles], [fitFunc(p.posi, x, y) for p in particles], c='b')
    plot.set_xlim(lengthLim[0][0], lengthLim[0][1])
    plot.set_ylim(lengthLim[1][0], lengthLim[1][1])
    plot.set_zlim(fitFunc([lengthLim[0][1], lengthLim[1][1]], x, y), fitFunc([lengthLim[0][0], lengthLim[1][0]], x, y)+1)
    plot.set_title("Position of particles at iteration 0")
    plot.set_xlabel("m length")
    plot.set_ylabel("n length")
    plot.set_zlabel("Number of partitions (Fitness)")
    return s