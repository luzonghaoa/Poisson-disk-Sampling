#import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import queue
import numpy as np
import random


class Grid:
    dimension = 3
    cellsize = 0
    r = 0
    length = 0
    width = 0
    height = 0

    def __init__(self, r, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.r = r
        self.cellsize = r / math.sqrt(self.dimension)
        self.x = math.ceil(self.length / self.cellsize)
        self.y = math.ceil(self.width / self.cellsize)
        self.z = math.ceil(self.height / self.cellsize)

    def generate_grid(self):
        dt = np.dtype([('is_point', np.int32), ('position', np.float64, (3,))])
        size = [self.x, self.y, self.z]
        return np.zeros(size, dtype=dt)

    def generate_point(self):
        list = []
        list.append(random.uniform(-self.length / 2, self.length / 2))
        list.append(random.uniform(-self.width / 2, self.width / 2))
        list.append(random.uniform(-self.height / 2, self.height / 2))
        return list

    def getcoordinate(self, point):
        x = math.floor((point[0] + self.length / 2) / self.cellsize)
        y = math.floor((point[1] + self.width / 2) / self.cellsize)
        z = math.floor((point[2] + self.height / 2) / self.cellsize)
        list = [x, y, z]
        return list

    def generateRandomPointAround(self, point):
        a1 = random.uniform(0, 1)
        a2 = random.uniform(0, 1)
        a3 = random.uniform(0, 1)
        angle1 = 2 * math.pi * a1
        angle2 = 2 * math.pi * a2
        radius = self.r * (1 + a3)
        tmp = radius * math.sin(angle2)
        res = np.array([0,0,0], dtype=float)
        res[0] += point[0] + tmp * math.cos(angle1)
        res[1] += point[1] + tmp * math.sin(angle1)
        res[2] += point[2] + radius * math.cos(angle2)
        return res

    def distance(self, point1, point2):
        for i in range(self.dimension):
            squsum = (point1[i] - point2[i]) ** 2
        return math.sqrt(squsum)

    def inGrid(self, point):
        if point[0] < -self.length / 2 or point[0] > self.length / 2:
            return False
        if point[1] < -self.width / 2 or point[1] > self.width / 2:
            return False
        if point[2] < -self.height / 2 or point[2] > self.height / 2:
            return False
        return True
    def inGrid_co(self, p_co):
        if p_co[0] < 0 or p_co[0] >= self.x:
            return False
        if p_co[1] < 0 or p_co[1] >= self.y:
            return False
        if p_co[2] < 0 or p_co[2] >= self.z:
            return False
        return True

    def inNeighbourhood(self, grid, point):
        p_co = self.getcoordinate(point)
        for i in range(-2, 3):
            for j in range(-2, 3):
                for k in range(-2, 3):
                    if self.inGrid_co([p_co[0]+i, p_co[1]+j, p_co[2]+k]):
                        if grid[p_co[0]+i, p_co[1]+j, p_co[2]+k][0] == 1:
                            if self.distance(grid[p_co[0]+i, p_co[1]+j, p_co[2]+k][1], point) < self.r:
                                return True
                    else:
                        continue
        return  False



def generate_poisson(r, k, length, width, heiht):
    # create the 3 dimension grid
    sample_space = Grid(r, length, width, heiht)
    grid = sample_space.generate_grid()

    # create the queque
    processlist = queue.Queue()
    samplepoints = []

    # generate the first point
    #random.seed(5)
    firstpoint = sample_space.generate_point()
    coordinate = sample_space.getcoordinate(firstpoint)
    grid[coordinate[0], coordinate[1], coordinate[2]] = (1, firstpoint)

    processlist.put(firstpoint)
    samplepoints.append(firstpoint)

    # generate other points
    while not processlist.empty():
        current_point = processlist.get()
        for i in range(0, k):
            newPoint = sample_space.generateRandomPointAround(current_point)
            new_co = sample_space.getcoordinate(newPoint)
            #check
            if sample_space.inGrid(newPoint) and (not sample_space.inNeighbourhood(grid, newPoint)):
                #update
                processlist.put(newPoint)
                samplepoints.append(newPoint)
                #print("1")
                grid[new_co[0], new_co[1], new_co[2]] = (1, newPoint)

    return samplepoints

def draw(point_list):
    ax = plt.subplot(111, projection='3d')
    for item in point_list:
        ax.scatter(item[0], item[1], item[2], c='r')
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

if __name__ == "__main__":
    points = generate_poisson(1, 30, 10, 10, 10)
    print(points)
    print(len(points))
    draw(points)



