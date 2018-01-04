import math
import numpy as np
import poisson_disk_sampling_3D as po
import matplotlib.pyplot as plt
import lly
import matplotlib
from PIL import Image

L = 10
points = po.generate_poisson(1, 30, L, L, L)
#po.draw(points)
#points = lly.PoissonSampling3D(1 ,L, L, L, 30)
G = len(points)
N = 200
M = 4
rate = M * 2 / 200
p = np.zeros([N, N])
print(G)
print(N * N * G * 10)
#print(points)
a=input()
cnt = 0
'''
for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            tmp1 = 0
            tmp2 = 0
            for item in points:
                q = 2 * math.pi * (i * item[0] + j * item[1] + k * item[2])
                tmp1 += math.cos(q)
                tmp2 += math.sin(q)
            p[i, j, k] = 1 / G * (tmp1 ** 2) + 1 / G * (tmp2 ** 2)
            print(cnt)
            cnt += 1
'''
'''
for i in range(0, N):
    for j in range(0, N):
        tmp1 = 0
        tmp2 = 0
        for item in points:
            q = 2 * math.pi * ((i * rate - M) * item[0] + (M - rate * j) * item[1])
            tmp1 += math.cos(q)
            tmp2 += math.sin(q)
            print(cnt)
            cnt += 1
        p[i][j] = (tmp1 ** 2)/G + (tmp2 ** 2)/G
'''
for _ in range(10):
    for i in range(0, N):
        for j in range(0, N):
            tmp1 = 0
            tmp2 = 0
            for item in points:
                q = 2 * math.pi * ((i * rate - M) * item[0] + (M - rate * j) * item[1])
                tmp1 += math.cos(q)
                tmp2 += math.sin(q)
                print(cnt)
                cnt += 1
            p[i][j] += (tmp1 ** 2)/G + (tmp2 ** 2)/G

for i in range(0, N):
    for j in range(0, N):
        p[i][j] /= 10

#print(p)
#p[0][0] = 0.2

#test  = p[15]
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.imshow(p, cmap = plt.cm.gray)
plt.show()
print("complete")
'''
for i in range(p.shape[0]):
    for j in range(p.shape[1]):
        if p[i][j] >= 3:
            p[i][j] = 255
# 将矩阵mat_z以image的形式显示出来，双线性插值，灰度图，原点在下方，坐标范围定义为extent
#plt.imshow(p, interpolation='bilinear', cmap=matplotlib.cm.gray, origin='lower')
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.imshow(p, cmap = plt.cm.gray)
plt.show()
'''