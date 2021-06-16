from common import *
from bai_tap_1 import *
from bai_tap_2 import *
import numpy as np


def cold_start_problem(input_data):
    working_data = np.copy(input_data)
    mu = np.average(working_data)

    # Tính giá trị đánh giá còn thiếu cho mỗi user
    for u in range(0, 15):
        missing_r_array = np.where(working_data[u] == 0)
        print("các giá trị còn thiếu của user" + str(u) + ":")
        print(missing_r_array[0])
        print("kết quả đánh giá còn thiếu cho user" + str(u) + ":")
        bu = np.sum(input_data[u, :] - mu)/len(input_data[u, :])
        for i in missing_r_array[0]:
            bi = np.sum(input_data[:, i] - mu)/len(input_data[:, i])
            # tính rui và gán lại vào vị trí còn thiếu
            working_data[u, i] = mu + bu + bi
        print("=================================================================")
    print("=================================================================")
    print()
    print()

    print("kết quả đánh giá đầy đủ sau khi tính toán")
    print(working_data)
    return working_data


cold_start_problem(sample_input_data)
