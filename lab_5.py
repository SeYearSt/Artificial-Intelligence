import matplotlib.pyplot as plt
import numpy as np


def init_points(min_x, max_x, min_y, max_y, count = 100):
    X = []
    Y = []
    for i in range(count):
        X.append(np.random.uniform(min_x, max_x))
        Y.append(np.random.uniform(min_y, max_y))

    points = []

    for i in range(len(X)):
        point = dict()
        point['x'] = X[i]
        point['y'] = Y[i]
        points.append(point)

    return (X, Y, points)


def init_clusters(min_x, max_x, min_y, max_y, count = 2):
    clusters = []
    for i in range(count):
        cluster = dict()
        cluster['x'] = np.random.uniform(min_x, max_x)
        cluster['y'] = np.random.uniform(min_x, max_x)
        cluster['points'] = []

        clusters.append(cluster)
    return clusters


def d(point1, point2):
    return np.sqrt(((point1['x'] - point2['x'])**2 + (point1['y'] - point2['y'])**2))


def equal_clusters(clusters1, clusters2):
    sets1 = []
    sets2 = []
    for cluster in clusters1:
        for points in cluster['points']:
            sets1.append(set(points.items()))

    for cluster in clusters2:
        for points in cluster['points']:
            sets2.append(set(points.items()))
    # print(sets1)
    # print(sets2)

    for i in range(len(sets1)):
         if sets1[i] != sets2[i]:
             return False
    return True



def find_nearest_clusters(points, clusters):
    for cluster in clusters:
        del cluster['points'][:]

    for point in points:
        i = 0
        min_distance = d(point, clusters[0])
        for  j in  range(len(clusters)):
            if d(point, clusters[j]) < min_distance:
                i = j
        clusters[i]['points'].append(point)

def figure_new_clusters(clusters):
    for cluster in clusters:
        new_x = 0
        new_y = 0
        for point in cluster['points']:
            new_x += point['x']
            new_y += point['y']
       # от тут при діленні на нуль пропадають кластери
            if len(cluster['points']) == 0:
                cluster['x'] = new_x
                cluster['y'] = new_y
            else:
                cluster['x'] = new_x / len(cluster['points'])
                cluster['y'] = new_y / len(cluster['points'])


def plot_points_clusters(points, clusters, sub = 211):
    points_x = []
    points_y = []
    clusters_x = []
    clusters_y = []
    for point in points:
        points_x.append(point['x'])
        points_y.append(point['y'])
    for cluster in clusters:
        clusters_x.append((cluster['x']))
        clusters_y.append((cluster['y']))

    fig = plt.subplot(sub)
    fig.scatter(X, Y)
    fig.scatter(clusters_x, clusters_y)


X, Y, points = init_points(-10, 10, -10 ,10,400)

clusters = init_clusters(-10, 10, -10, 10, 10)

plot_points_clusters(points, clusters)

while True:
    find_nearest_clusters(points, clusters)
    old_clusters = clusters[:]
    figure_new_clusters(clusters)

    if equal_clusters(old_clusters, clusters):
        break
plot_points_clusters(points, clusters, 212)

plt.show()

print(clusters)