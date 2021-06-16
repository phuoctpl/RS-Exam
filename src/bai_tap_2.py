from common import *
import numpy as np


def item_base(input_data):
    working_data = np.copy(input_data)
    print("Data input:")
    print(working_data)
    print("=================================================================")
    print()
    sim_matrix = np.zeros((15, 15))

    # chuyển vị ma trận:
    transposed_input_data = np.transpose(working_data)

    # Tính matrix sim(i, i1)
    for i in range(0, 15):
        for i1 in range(0, 15):
            if sim_matrix[i, i1] != 0:
                continue
            if i == i1:
                sim_matrix[i, i1] = 1
            else:
                sim_matrix[i, i1] = sim_matrix[i1, i] = calculate_sim(transposed_input_data, i, i1)

    print("matrix sim(i, i1)")
    print(sim_matrix)
    print("=================================================================")
    print()

    for i in range(0, 15):
        # lấy 3 item tương đông nhất với item 1
        similar_users = np.argsort(sim_matrix[i])[-4:-1]
        print("3 item tương đồng nhất với item" + str(i))
        print(similar_users)
        # Tính giá trị đánh giá còn thiếu cho mỗi item
        missing_r_array = np.where(transposed_input_data[i] == 0)
        print("các giá trị còn thiếu của item" + str(i) + ":")
        print(missing_r_array[0])
        print("kết quả đánh giá còn thiếu cho item" + str(i) + ":")
        for index in missing_r_array[0]:

            rui_numerator = 0
            rui_denominator = 0
            for i1 in similar_users:
                rui_numerator += sim_matrix[i, i1]*transposed_input_data[i1, index]
                rui_denominator += np.absolute(sim_matrix[i, i1])
            # tính rui và gán lại vào vị trí còn thiếu
            transposed_input_data[i, index] = rui_numerator/rui_denominator
            print("input_data[" + str(i) + ", " + str(index) + "] = " + str(transposed_input_data[i, index]))
        print("=================================================================")
    print("=================================================================")
    print()
    print()

    result_data = np.transpose(transposed_input_data)
    print("kết quả đánh giá đầy đủ sau khi tính toán")
    print(result_data)
    return result_data


item_base(sample_input_data)
