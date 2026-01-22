import numpy as np

# wzorce
znaki_wz_1 = np.matrix([
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
])

znaki_wz_2 = np.matrix([
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
])

znaki_wz_3 = np.matrix([
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]
])

# test
znaki_test_1 = np.matrix([
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
])

znaki_test_2 = np.matrix([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
])

znaki_test_3 = np.matrix([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
])


def euclidean_distance(point_a, point_b):
    return np.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)


def chebyshev_distance(point_a, point_b):
    return max(abs(point_b[0] - point_a[0]), abs(point_b[1] - point_a[1]))


def manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def dot_finder(matrix):
    rows, cols = matrix.shape
    dots = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                dots.append((i, j))

    return dots


def miara_niepodobienstwa(matrix_BA, matrix_BB, miary_odl):
    dots_BA = dot_finder(matrix_BA)
    dots_BB = dot_finder(matrix_BB)

    miara = 0

    for point_BA in dots_BA:
        odl_min = np.inf
        for point_BB in dots_BB:
            if miary_odl == "man":
                odl_akt = manhattan_distance(point_BA, point_BB)
            elif miary_odl == "chebyshev":
                odl_akt = chebyshev_distance(point_BA, point_BB)
            elif miary_odl == "eucldean":
                odl_akt = euclidean_distance(point_BA, point_BB)
            odl_min = min(odl_min, odl_akt)
        miara += odl_min

    return miara


def miara_niepodobienstwa_obu(matrix_BA, matrix_BB, miara):
    miara_BA_BB = miara_niepodobienstwa(matrix_BA, matrix_BB, miara)
    miara_BB_BA = miara_niepodobienstwa(matrix_BB, matrix_BA, miara)
    return (miara_BA_BB + miara_BB_BA) * -1

def raport_1():
    print("Raport 1")
    wzorce = (znaki_wz_1, znaki_wz_2, znaki_wz_3)
    wzorce_str = ("znaki_wz_1", "znaki_wz_2", "znaki_wz_3")
    miary = ("man", "chebyshev", "eucldean")

    for wzor_i in range(len(wzorce)):
        for miara in miary:
            print(f"Dla wzoru: {wzorce_str[wzor_i]}, dla miary: {miara} = "
                  f"{miara_niepodobienstwa_obu(znaki_test_1, wzorce[wzor_i], miara)}")

def raport_2():
    print("Raport 2")
    print("Znak testowy 1")
    print(znaki_test_1)
    print("---")
    print("Znak testowy 1 przesuniety w lewo o jeden")
    znaki_test_1_shifted = np.roll(znaki_test_1, -1, axis=1)
    print(znaki_test_1_shifted)

    wzorce = (znaki_wz_1, znaki_wz_2, znaki_wz_3)
    wzorce_str = ("znaki_wz_1", "znaki_wz_2", "znaki_wz_3")

    for wzor_i in range(len(wzorce)):
        print(f"Dla wzoru: {wzorce_str[wzor_i]} miara = "
              f"{miara_niepodobienstwa_obu(znaki_test_1_shifted, wzorce[wzor_i], 'eucldean')}")

def raport_3():
    print("Raport 3")
    wzorce = (znaki_wz_1, znaki_wz_2, znaki_wz_3)
    testowe = (znaki_test_2, znaki_test_3)
    testowe_str = ("znaki_test_2", "znaki_test_3")
    wzorce_str = ("znaki_wz_1", "znaki_wz_2", "znaki_wz_3")

    for test_i in range(len(testowe)):
        for wzor_i in range(len(wzorce)):
            print(f"Dla znaku testowego: {testowe_str[test_i]} i wzoru: {wzorce_str[wzor_i]} "
                  f"miara wynosi: {miara_niepodobienstwa_obu(testowe[test_i], wzorce[wzor_i], 'eucldean')}")


raport_1()
raport_2()
raport_3()










