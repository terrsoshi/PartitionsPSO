from functions import fitFunc

class Particle:
    def __init__(self, posi = [0, 0], vel = [0, 0]):
        self.posi = posi
        self.vel = vel
        self.bestPosi = posi
    def updateBest(self, x, y):
        if fitFunc(self.posi, x, y)>fitFunc( self.bestPosi, x, y):
            self.bestPosi = self.posi
    def updateVel(self, alpha, beta, globBestPosi):
        # x velocity
        self.vel[0] = 0.5*self.vel[0] + (alpha[0] * beta[0] * (self.bestPosi[0] - self.posi[0])) + (alpha[1] * beta[1] * (globBestPosi[0] - self.posi[0]))
        # y velocity
        self.vel[1] = 0.5*self.vel[1] + (alpha[0] * beta[0] * (self.bestPosi[1] - self.posi[1])) + (alpha[1] * beta[1] * (globBestPosi[1] - self.posi[1]))
    def updatePosi(self, lengthLim):
        self.posi = [self.posi[0]+self.vel[0], self.posi[1]+self.vel[1]]
        for x in range(2):
            if self.posi[x]<lengthLim[x][0]:
                self.posi[x] = lengthLim[x][0]
            elif self.posi[x]>lengthLim[x][1]:
                self.posi[x] = lengthLim[x][1]
