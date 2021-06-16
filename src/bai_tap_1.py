from common import *
import numpy as np


def user_base(input_data):
    working_data = np.copy(input_data)
    print("Data input:")
    print(working_data)
    print("=================================================================")
    print()
    sim_matrix = np.zeros((15, 15))

    # Tính matrix sim(u, u1)
    for u in range(0, 15):
        for u1 in range(0, 15):
            if sim_matrix[u, u1] != 0:
                continue
            if u == u1:
                sim_matrix[u, u1] = 1
            else:
                sim_matrix[u, u1] = sim_matrix[u1, u] = calculate_sim(working_data, u, u1)

    print("matrix sim(u, u1)")
    print(sim_matrix)
    print("=================================================================")
    print()

    for u in range(0, 15):
        # lấy 3 user tương đông nhất với user u
        similar_users = np.argsort(sim_matrix[u])[-4:-1]
        print("3 user tương đồng nhất với user" + str(u))
        print(similar_users)
        # Tính giá trị đánh giá còn thiếu cho mỗi user
        missing_r_array = np.where(working_data[u] == 0)
        print("các giá trị còn thiếu của user" + str(u) + ":")
        print(missing_r_array[0])
        print("kết quả đánh giá còn thiếu cho user" + str(u) + ":")
        for i in missing_r_array[0]:

            rui_numerator = 0
            rui_denominator = 0
            for u1 in similar_users:
                rui_numerator += sim_matrix[u, u1] * working_data[u1, i]
                rui_denominator += np.absolute(sim_matrix[u, u1])
            # tính rui và gán lại vào vị trí còn thiếu
            working_data[u, i] = rui_numerator / rui_denominator
            print("input_data[" + str(u) + ", " + str(i) + "] = " + str(working_data[u, i]))
        print("=================================================================")
    print("=================================================================")
    print()
    print()

    print("kết quả đánh giá đầy đủ sau khi tính toán")
    print(working_data)
    return working_data


user_base(sample_input_data)
