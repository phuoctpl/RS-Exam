import numpy as np


def AHP(attributes_plans_matrix, attributes_matrix):
    # Tính trọng số cho ma trận tiêu chí
    attributes_eigenvectors = weight(attributes_matrix)
    # Tính chỉ số nhất quán của ma trận tiêu chí
    CR = consistent_ratio(attributes_matrix, attributes_eigenvectors)
    if CR >= 0.1:
        print("Ma trận đánh giá tiêu chí không chính xác, đề nghị đánh giá lại")
        return

    # Tính trọng số cho mỗi ma trận đánh giá phương án trên tiêu chí
    attributes_plans_eigenvectors = []
    for i in range(attributes_plans_matrix.shape[0]):
        eigenvectors = weight(attributes_plans_matrix[i, :])
        attributes_plans_eigenvectors.append(eigenvectors)
        CR = consistent_ratio(attributes_plans_matrix[i, :], eigenvectors)
        if CR >= 0.1:
            print("Ma trận đánh giá Phương án " + str(i) + " không chính xác, đề nghị đánh giá lại")
            return
    attributes_plans_eigenvectors = np.array(attributes_plans_eigenvectors)
    # Tính độ ưu tiên cho từng phương án
    plan_priorities = []
    for i in range(attributes_plans_eigenvectors.shape[1]):
        plan_priorities.append({"Plan" + str(i): attributes_eigenvectors.dot(attributes_plans_eigenvectors[:, i])})

    print("Kết quản đánh giá độ ưu tiên:")
    print(plan_priorities)


def consistent_ratio(matrix, eigenvectors):
    size = len(eigenvectors)
    lam_max = np.average(matrix.dot(eigenvectors))
    CI = (lam_max - size) / (size - 1)
    CR = CI / random_index[size]
    return CR


def weight(matrix):
    size = len(matrix)
    eigenvectors = np.zeros((size,))
    # Tính trọng số của tiêu chí bằng phương pháp vector riêng
    while True:
        work_matrix = matrix
        # Bình phương ma trận
        work_matrix = work_matrix.dot(work_matrix)
        attribute_eigenvectors_old = np.copy(eigenvectors)
        for i in range(0, size):
            # Tính từng trọng số cho mỗi tiêu chí/phương án
            eigenvectors[i] = np.sum(work_matrix[i, :]) / np.sum(work_matrix)
        # kết thúc tính toán khi giá trị trọng số không thay đổi cho đến chữ số thập phân thứ 2
        if (np.around(attribute_eigenvectors_old, decimals=2) == np.around(eigenvectors, decimals=2)).all():
            break
    return eigenvectors


# Thang chỉ số ngẫu nhiên
random_index = {
    1: 0,
    2: 0,
    3: 0.52,
    4: 0.89,
    5: 1.11,
    6: 1.25,
    7: 1.35,
    8: 1.40,
    9: 1.45,
    10: 1.49,
    11: 1.52,
    12: 1.54,
    13: 1.56,
    14: 1.58,
    15: 1.59,
}
# Áp dụng với dữ liệu từ bài tập 1 về AHP:
price = np.array([
    [1, 3, 2],
    [1 / 3, 1, 1 / 5],
    [1 / 2, 5, 1]
])
distance = np.array([
    [1, 6, 1 / 3],
    [1 / 6, 1, 1 / 9],
    [3, 9, 1]
])
labor = np.array([
    [1, 1 / 3, 1],
    [3, 1, 7],
    [1, 1 / 7, 1]
])
wage = np.array([
    [1, 1 / 3, 1 / 2],
    [3, 1, 4],
    [2, 1 / 4, 1]
])
attribute = np.array([
    [1, 1 / 5, 3, 4],
    [5, 1, 9, 7],
    [1 / 3, 1 / 9, 1, 2],
    [1 / 4, 1 / 7, 1 / 2, 1]
])

AHP(np.array([price, distance, labor, wage]), attribute)
