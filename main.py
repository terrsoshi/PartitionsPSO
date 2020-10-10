import random as rand
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functions import *
from particle import Particle


if __name__ == '__main__':
    alpha = [0.1, 0.1]
    n_particle = 20
    x, y = 9, 3
    lengthLim = [[2*x/5, x], [2*y/11, y]]
    
    iter_ = 0
    maxIter_ = 200
    minAvgFitDiff = 0.05
    minAvgPosiDiff = 0.075
    
    particles = [Particle([rand.uniform(lengthLim[0][0], lengthLim[0][1]), rand.uniform(lengthLim[1][0], lengthLim[1][1])]) for _ in range(n_particle)]
    # initial global best position is position of first particle
    globBestPosi = particles[0].posi
    
    fig = plt.figure()
    plot = fig.add_subplot(111, projection='3d')
    s = plotGraph(plot, particles, x, y, lengthLim)
    
    
    while iter_<maxIter_ and calAvgFitDiff(x, y, particles)>minAvgFitDiff and calAvgPosiDiff(x, y, particles)>minAvgPosiDiff:
        for p in particles:
            p.updateBest(x, y)
            globBestPosi = compFit(globBestPosi, p.posi, x, y)
        beta = [rand.random(), rand.random()]
        for p in particles:
            p.updateVel(alpha, beta, globBestPosi)
            p.updatePosi(lengthLim)
        iter_+=1
        s.remove()
        s = plot.scatter([p.posi[0] for p in particles], [p.posi[1] for p in particles], [fitFunc(p.posi, x, y) for p in particles], c='b')
        plot.title.set_text("Position of particles at iteration {}".format(iter_))
        plt.pause(0.05)
    
    print("Global Best Position/Best Size of Partition: [" + str(round(globBestPosi[0], 2)) + ", " + str(round(globBestPosi[1], 2)) + "] Fitness/Maximum Number of Partitions: " + str(fitFunc(globBestPosi, x, y)))
    print("Iterations: " + str(iter_))
    for particleNum in range (len(particles)):
        if particleNum < 9:
            print("Particle " + str(particleNum+1) + "  | Position/Size of Partition: [" + str(round(particles[particleNum].posi[0], 2)) + ", " + str(round(particles[particleNum].posi[1], 2)) + "] Fitness/Number of Partitions: " + str(fitFunc(particles[particleNum].posi, x, y)))
        else:
            print("Particle " + str(particleNum+1) + " | Position/Size of Partition: [" + str(round(particles[particleNum].posi[0], 2)) + ", " + str(round(particles[particleNum].posi[1], 2)) + "] Fitness/Number of Partitions: " + str(fitFunc(particles[particleNum].posi, x, y)))       
            
    
    