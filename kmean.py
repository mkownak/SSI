import matplotlib
import matplotlib.pyplot as plt
import numpy.random
import pandas as pd
import math
import numpy as np
matplotlib.use('TkAgg')

df = pd.read_csv('spiralka.csv', skipinitialspace=True, names=["x1", "x2"])

x = list(df["x1"])
y = list(df["x2"])


def euclidean_distance(point_a, point_b):
    return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

def minimum_distance_idx(distances):
    min_value = min(distances)
    for i in range(len(distances)):
        if distances[i] == min_value:
            return i

    return 0

def plotter(groups, iteration_count):
    colors = ["b", "g", "c", "m"]
    center_list = list(groups.keys())

    plt.figure(figsize=(10,5))
    for center_idx in range(len(center_list)):
        for point in groups[center_list[center_idx]]:
            plt.plot(point[0], point[1], 's', color=f"{colors[center_idx]}", markeredgecolor='k')
        plt.plot(center_list[center_idx][0], center_list[center_idx][1], 's', color='red', markeredgecolor='k',
                 label=f"{center_list[center_idx][0]}, {center_list[center_idx][1]}, color: {colors[center_idx]}")

    plt.legend()
    plt.title(f"groups after {iteration_count} iteration")
    plt.show()

def recalculate_centroid(groups_dict):
    updated_v_list = []
    updated_groups_dict = {}

    center_list = list(groups_dict.keys())

    for center_idx in range(len(center_list)):
        sum_x = 0
        sum_y = 0
        for point_i in range(len(groups_dict[center_list[center_idx]])):
            sum_x += groups_dict[center_list[center_idx]][point_i][0]
            sum_y += groups_dict[center_list[center_idx]][point_i][1]

        centroid = (sum_x/len(groups_dict[center_list[center_idx]]), sum_y/len(groups_dict[center_list[center_idx]]))

        updated_v_list.append(centroid)
        updated_groups_dict[centroid] = []

    return updated_v_list, updated_groups_dict

print("length of x: ",len(x))

m = 4
iters = 10

V = []
for i in range(m):
    index = np.random.randint(0, len(x))
    V.append((x[index],y[index]))

dict_centroid = {}
for v in V:
    dict_centroid[v] = []

print(V)
print(dict_centroid)

plt.plot(x, y, "s", markerfacecolor='none', markeredgecolor='k')
for point in V:
    plt.plot(point[0], point[1], marker="s", color="red")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Initial selection of middle points")
plt.show()

iteration = 0
while iteration < iters:
    for s in range(len(x)):
        distances = []
        for v_point in V:
            current_point = (x[s],y[s])
            distance = euclidean_distance(current_point, v_point)

            distances.append(distance)

        min_point_idx = minimum_distance_idx(distances)
        dict_centroid[V[min_point_idx]].append((x[s], y[s]))
    plotter(dict_centroid, iteration)
    V, dict_centroid = recalculate_centroid(dict_centroid)
    iteration += 1
