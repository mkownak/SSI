import numpy as np
import matplotlib.pyplot as plt

znaki_wz_1 = np.matrix( '1 1 0 0 0; '
                        '0 1 0 0 0; '
                        '0 1 0 0 0; '
                        '0 1 0 0 0; '
                        '0 1 0 0 0')

znaki_wz_2 = np.matrix( '1 0 0 0 1; '
                        '0 1 0 1 0; '
                        '0 0 1 0 0; '
                        '0 1 0 1 0; '
                        '1 0 0 0 1')

znaki_wz_3 = np.matrix( '0 0 1 0 0; '
                        '0 0 1 0 0; '
                        '1 1 1 1 1; '
                        '0 0 1 0 0; '
                        '0 0 1 0 0')

znaki_test_1 = np.matrix( '0 1 0 0 0; '
                          '0 1 0 0 0; '
                          '0 1 0 0 0; '
                          '0 1 0 0 0; '
                          '0 1 0 0 0')

znaki_test_2 = np.matrix( '1 1 0 0 1; '
                          '0 1 0 1 0; '
                          '0 1 1 1 0; '
                          '0 1 0 1 0; '
                          '1 1 0 0 1')

znaki_test_3 = np.matrix( '0 0 0 0 0; '
                          '0 0 1 0 0; '
                          '1 1 1 1 1; '
                          '0 0 0 0 0; '
                          '0 0 1 0 0')

znaki_test_4 = np.matrix( '0 1 1 1 1; '
                          '1 0 1 1 1; '
                          '1 0 1 1 1; '
                          '1 0 1 1 1; '
                          '1 0 1 1 1')

znaki_test_1_neg = np.matrix( '1 0 1 1 1; '
                              '1 0 1 1 1; '
                              '1 0 1 1 1; '
                              '1 0 1 1 1; '
                              '1 0 1 1 1')

znaki_custom = np.matrix( '0 0 0 0 0; '
                          '0 0 0 0 0; '
                          '0 0 0 0 0; '
                          '0 0 0 0 0; '
                          '0 0 0 0 0')




def show_5x5(sample, title=None, ax=None):
    """
    sample: 5x5 macierz z wartościami 0/1 albo wektor 25 z wartościami -1/1
    - dla macierzy: 1 -> czarny, 0 -> biały
    - dla wektora:  1 -> czarny, -1 -> biały
    """
    a = np.asarray(sample).reshape(-1)

    if a.size != 25:
        raise ValueError(f"Expected 5x5 matrix or vector of length 25, got {a.size} elements")

    m = a.reshape(5, 5)

    # mapowanie na obraz (0=czarny, 1=biały w cmap='gray')
    # jeśli masz 0/1: czarny=1 -> 0, biały=0 -> 1  => img = 1 - m
    # jeśli masz -1/1: czarny=1 -> 0, biały=-1 -> 1 => img = (1 - m)/2
    if np.min(m) >= 0:      # 0/1
        img = 1 - m
    else:                   # -1/1
        img = (1 - m) / 2

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.imshow(img, cmap="gray", interpolation="nearest", vmin=0, vmax=1)

    ax.set_xticks(np.arange(-0.5, 5, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 5, 1), minor=True)
    ax.grid(which="minor", linestyle="-", linewidth=1)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

    if title:
        ax.set_title(title)

    #plt.savefig(title + ".png")
    plt.show()
    return fig, ax



#Config
weights = np.zeros((25, 25), dtype=float)

def convert_matrix(matrix):

    if type(matrix) == list:
        return matrix

    vector = matrix.flatten().tolist()[0]

    for i in range(len(vector)):
        if vector[i] == 0:
            vector[i] = -1

    return vector

def adjust_weights(sample):
    global weights
    temp_weights = np.copy(weights)
    sample = convert_matrix(sample)

    for i in range(len(weights)):
        for j in range(len(weights[i])):
            if i == j:
                continue
            else:
                temp_weights[i][j] = weights[i][j] + (1/len(weights[0]) * sample[i] * sample[j])

    weights = temp_weights

def run(sample):

    sample = convert_matrix(sample)

    temp = []
    for i in range(len(sample)):
        sum = 0
        for j in range(len(sample)):
            if i == j:
                continue
            else:
                sum += weights[i][j] * sample[j]

        if sum >= 0:
            temp.append(1)
        else:
            temp.append(-1)

    return temp


def raport_1():
    adjust_weights(znaki_wz_1)
    adjust_weights(znaki_wz_2)
    adjust_weights(znaki_wz_3)

    v_rec_1 = run(znaki_test_1)
    v_rec_2 = run(znaki_test_2)
    v_rec_3 = run(znaki_test_3)
    v_rec_4 = run(znaki_test_4)

    show_5x5(v_rec_1, "REC 1")
    show_5x5(v_rec_2, "REC 2")
    show_5x5(v_rec_3, "REC 3")
    show_5x5(v_rec_4, "REC 4")

def raport_2():
    adjust_weights(znaki_wz_1)
    adjust_weights(znaki_wz_2)
    adjust_weights(znaki_wz_3)

    tmp = []
    for i in range(len(weights)):
        tmp.append(float(weights[0][i]))
        if (i+1) % 5 == 0:
            print(tmp)
            tmp = []

def raport_3():
    adjust_weights(znaki_wz_1)
    adjust_weights(znaki_wz_2)
    adjust_weights(znaki_wz_3)

    v_rec_1_neg = run(znaki_test_1_neg)

    show_5x5(znaki_test_1_neg, "TEST 1 NEG")
    show_5x5(v_rec_1_neg, "REC 1 NEG")

def raport_4():
    adjust_weights(znaki_wz_1)
    adjust_weights(znaki_wz_2)
    adjust_weights(znaki_wz_3)

    show_5x5(znaki_custom, "TEST CUSTOM")

    v_rec_1_custom = run(znaki_custom)
    show_5x5(v_rec_1_custom, "REC 1 CUSTOM")

    v_rec_2_custom = run(v_rec_1_custom)
    show_5x5(v_rec_2_custom, "REC 2 CUSTOM")

raport_4()