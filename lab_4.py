import matplotlib.pyplot as plt
import random
import math


MIN_X = 0
MAX_X = math.pi #2*math.pi
INTERVAL = 100

N = 300

def f(x):
    #return x
    return math.sin(x)


def create_points(count = N):
    x_points = []
    y_points = []
    for i in range(count):
        x_points.append(random.uniform(MIN_X, MAX_X*INTERVAL))
        y_points.append(random.uniform(0, 1))
    return (x_points, y_points)


def count_points_under_line(f, x_points, y_points):
    points_count_under_line = 0
    points_count_out_line = 0
    for i in range(N):
        if y_points[i] <= f(x_points[i]):
            points_count_under_line += 1
        else:
            points_count_out_line += 1
    return (points_count_under_line, points_count_out_line)


def get_min_and_max(f,X):
    min = max = X[0]
    for x in X:
        if f(x) > max:
            max = f(x)
        elif f(x) < min:
            min = f(x)
    return (min, max)


X = [x/INTERVAL for x in range(MIN_X, int(MAX_X * INTERVAL))]
Y = [f(x) for x in X]

x_points, y_points = create_points(N)

K, Z = count_points_under_line(f,x_points, y_points)

#print(MAX_X - MIN_X)
#print(K)
#print(Z)
print(get_min_and_max(f, X))
print("Area of figure", K/N*(MAX_X - MIN_X))      


plt.plot(Y)
plt.plot()
plt.scatter(x_points, y_points, color = 'lightblue')
plt.show()
