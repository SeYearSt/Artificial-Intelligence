import matplotlib.pyplot as plt
import numpy as np
import random

'''MINX = 0
MAXX = 3 #2*math.pi
'''

N = 300


def f(x):
    return np.exp(x)**2

def def_integral(f,MINX, MAXX, seg = 300):
    S = 0

    X = np.linspace(MINX, MAXX, seg)

    for i in range(len(X) - 1):
        S += f((X[i] + X[i+1])/2)*(X[i+1] - X[i])
    return S


def integral_montecarlo(f, MINX, MAXX):

    def get_min_and_max(f,X):
        min = max = f(X[0])
        for x in X:
            if f(x) > max:
                max = f(x)
            elif f(x) < min:
                min = f(x)
        return (min, max)


    def create_random_points(min, max, count = N):
        x_points = []
        y_points = []
        x_points.append(np.random.uniform(MINX, MAXX, count))
        y_points.append(np.random.uniform(min, max, count))
        return (x_points, y_points)


    def count_points_under_chart(f, x_points, y_points, count = N):
        points_count_under_chart = 0
        points_count_out_chart = 0
        for i in range(count):
            if y_points[0][i] <= f(x_points[0][i]):
                points_count_under_chart += 1
        return points_count_under_chart


    X = np.linspace(MINX, MAXX, N)

    min, max = get_min_and_max(f,X)

    points_x, points_y = create_random_points(0, max, N)

    #print(points_x)
    #print(points_y)

    K = count_points_under_chart(f, points_x, points_y, N)

    print("Points under figure:", K)
    print("All points points:", N)

    print("Square rectangle:", np.abs(max - min)*np.abs(MAXX - MINX))
    print("Square figure:", K/N * np.abs(max - min)*np.abs(MAXX - MINX))



    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.plot(X, f(X))
    plt.scatter(points_x, points_y)
    plt.show()

integral_montecarlo(np.sin, 0, np.pi)

print("Square using definite integral:",def_integral(np.sin,0, np.pi))

#get_square(f,1 , 2)