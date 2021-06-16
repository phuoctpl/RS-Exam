from common import *
import numpy as np


def matrix_factorization(input_data, k=2, beta=0.1, lam=0.1, max_loop=1000):
    print(k)
    print(beta)
    print(lam)
    print(max_loop)
    # khởi tạo giá trị cho W và H
    input_data_shape = input_data.shape
    w = np.random.randn(input_data_shape[1], k)
    h = np.random.randn(k, input_data_shape[0])

    print("giá trị ban đầu w:")
    print(w)
    print("giá trị ban đầu h:")
    print(h)

    for _ in range(max_loop):
        # chọn một vị trí rui
        rui = 0
        u = 0
        i = 0
        while rui == 0:
            # Draw random (u, i, r) from D train
            u = np.random.randint(0, input_data_shape[1] - 1)
            i = np.random.randint(0, input_data_shape[0] - 1)
            rui = input_data[u, i]
        print("input_data[" + str(u) + ", " + str(i) + "] = " + str(rui))
        print("=================================================================")

        # tính r3ui theo w và h
        r3ui = np.dot(w[u, :], h[:, i])
        print("r3ui = " + str(r3ui))
        print("=================================================================")
        e = rui - r3ui
        for j in range(0, k):
            wuk = w[u, j]
            hik = h[j, i]
            w[u, j] = round(wuk + beta * (e * hik - lam * wuk), 2)
            h[j, i] = round(hik + beta * (e * wuk - lam * hik), 2)
    print("Kết quả của w:")
    print(w)
    print("Kết quả của h:")
    print(h)
    print("=================================================================")

    print(w.dot(h))


matrix_factorization(sample_input_data)
