import numpy as np
import math

sample_input_data = np.array([
    [4, 0, 3, 0, 4, 1, 3, 1, 0, 2, 4, 1, 5, 0, 1],
    [1, 2, 1, 0, 1, 4, 2, 5, 3, 2, 4, 2, 5, 5, 4],
    [0, 5, 0, 3, 1, 1, 2, 5, 2, 0, 3, 2, 5, 0, 1],
    [4, 4, 3, 3, 3, 5, 2, 3, 1, 1, 2, 1, 0, 3, 0],
    [3, 5, 5, 2, 5, 4, 1, 3, 3, 0, 4, 3, 4, 3, 4],
    [2, 2, 1, 3, 2, 1, 4, 0, 2, 1, 0, 3, 4, 4, 0],
    [4, 3, 3, 0, 2, 1, 2, 0, 1, 2, 1, 4, 4, 1, 3],
    [1, 4, 1, 1, 0, 5, 5, 2, 5, 3, 5, 0, 3, 4, 1],
    [0, 5, 1, 0, 0, 4, 5, 5, 4, 2, 5, 5, 2, 4, 5],
    [4, 5, 2, 3, 5, 1, 1, 4, 3, 1, 0, 4, 1, 0, 1],
    [0, 3, 5, 0, 2, 0, 1, 0, 4, 3, 3, 5, 3, 2, 4],
    [1, 3, 2, 5, 2, 1, 0, 5, 1, 2, 2, 2, 4, 1, 4],
    [0, 2, 1, 5, 1, 4, 5, 0, 0, 0, 3, 0, 5, 1, 4],
    [2, 3, 2, 1, 3, 4, 0, 1, 4, 1, 5, 4, 2, 3, 4],
    [0, 2, 2, 1, 3, 2, 1, 3, 2, 5, 1, 4, 4, 1, 2]
])


# Tính Sim(u, u1)
def calculate_sim(input_data, u, u1):
    if u >= 15 or u1 >= 15:
        return None
    tmp = []
    numerator = 0
    denominator_1 = 0
    denominator_2 = 0
    for i in range(0, 14):
        if input_data[u, i] != 0 and input_data[u1, i] != 0:
            tmp.append(i)
    for i in tmp:
        numerator += input_data[u, i] * input_data[u1, i]
        denominator_1 += math.pow(input_data[u, i], 2)
        denominator_2 += math.pow(input_data[u1, i], 2)

    denominator = math.sqrt(denominator_1) * math.sqrt(denominator_2)
    return round(numerator / denominator, 4)


calculate_sim(sample_input_data, 1, 1)
