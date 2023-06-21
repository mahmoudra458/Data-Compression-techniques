import math

from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt

imgPath = 'Lenna256.png'
img = Image.open(imgPath).convert("L")
imgArr = np.asarray(img)
matrix = np.array(imgArr)


def divide_vectors(mat_array):
    j = 0
    vectors = []
    while j < 256:
        i = 0
        while i < 256:
            vectors.append(mat_array[i:i+4, j:j+4])
            i += 4
        j += 4
    return vectors

def get_average(vectors):
    values_arr = []
    for r in range(4):
        for j in range(4):
            sum_0 = 0
            for i in range(len(vectors)):
                sub_matrix = vectors[i]
                sum_0 += sub_matrix[r][j]
            values_arr.append(sum_0/len(vectors))

    I = 0
    matrix_re = []
    for R in range(4):
        a = []
        for C in range(4):
            a.append(values_arr[I])
            I += 1
        matrix_re.append(a)
    matrix_re = np.array(matrix_re)
    return matrix_re

def If_integer(N):
    X = int(N)
    temp = N - X
    if temp == 0:
        return True
    else:
        return False

def split_average(matrix_average):
    matrix_split1 = []
    matrix_split2 = []
    for i in range(4):
        a = []
        b = []
        for j in range(4):
            N = matrix_average[i][j]
            if If_integer(N):
                a.append(N - 1)
                b.append(N + 1)
            else:
                a.append(int(N))
                b.append(math.ceil(N))
        matrix_split1.append(a)
        matrix_split2.append(b)
    matrix_split1 = np.array(matrix_split1)
    matrix_split2 = np.array(matrix_split2)
    return matrix_split1, matrix_split2

def get_nearest(mat_1, mat_2, mat_3):
    sub1 = 0
    sub2 = 0
    for i in range(4):
        for j in range(4):
            sub1 += abs(mat_1[i][j] - mat_2[i][j])
            sub2 += abs(mat_1[i][j] - mat_3[i][j])
    return sub1, sub2

def associate_vectors(list_return1, list_return2, vectors, m1, m2):
    for i in range(len(vectors)):
        n1, n2 = get_nearest(vectors[i], m1, m2)
        if n1 <= n2:
            list_return1.append(vectors[i])
        else:
            list_return2.append(vectors[i])
    return list_return1, list_return2


def get_round(list_asso1, list_asso2):
    list_associate_ave1 = get_average(list_asso1)
    list_associate_ave2 = get_average(list_asso2)
    sp_left1, sp_left2 = split_average(list_associate_ave1)
    sp_right1, sp_right2 = split_average(list_associate_ave2)
    left_assoc1 = []
    left_assoc2 = []
    right_assoc1 = []
    right_assoc2 = []
    left_assoc1, left_assoc2 = associate_vectors(left_assoc1, left_assoc2, list_asso1, sp_left1, sp_left2)
    right_assoc1, right_assoc2 = associate_vectors(right_assoc1, right_assoc2, list_asso2, sp_right1, sp_right2)
    return left_assoc1, left_assoc2, right_assoc1, right_assoc2
def compress():
    divide_mat = divide_vectors(matrix)
    get_ave = get_average(divide_mat)
    mat1, mat2 = split_average(get_ave)
    list_associate1 = []
    list_associate2 = []
    list_associate1, list_associate2 = associate_vectors(list_associate1, list_associate2, divide_mat, mat1, mat2)
    L1, R1, L2, R2 = get_round(list_associate1, list_associate2)
    L_left1, L_right1, R_left1, R_right1 = get_round(L1, R1)
    R_left_11, R_right_11, RR_left, RR_right = get_round(L2, R2)
    L1, L2, L3, L4 = get_round(L_left1, L_right1)
    L5, L6, L7, L8 = get_round(R_right1, R_right1)
    L9, L10, L11, L12 = get_round(R_left_11, R_right_11)
    L13, L14, L15, L16 = get_round(RR_left, RR_right)
    return (ceil_up_matrix(get_average(L1)), L1, ceil_up_matrix(get_average(L2)), L2, ceil_up_matrix(get_average(L3)), L3,
           ceil_up_matrix(get_average(L4)), L4, ceil_up_matrix(get_average(L5)), L5, ceil_up_matrix(get_average(L6)), L6,
           ceil_up_matrix(get_average(L7)), L7, ceil_up_matrix(get_average(L8)), L8, ceil_up_matrix(get_average(L9)), L9,
           ceil_up_matrix(get_average(L10)), L10, ceil_up_matrix(get_average(L11)), L11, ceil_up_matrix(get_average(L12)), L12,
           ceil_up_matrix(get_average(L13)), L13, ceil_up_matrix(get_average(L14)), L14, ceil_up_matrix(get_average(L15)), L15,
           ceil_up_matrix(get_average(L16)), L6)
def ceil_up_matrix(ave_mat):
    for i in range(4):
        for j in range(4):
            ave_mat[i][j] = math.ceil(ave_mat[i][j])
    return ave_mat
ave_t = []
ave1, L1, ave2, L2, ave3, L3, ave4, L4, ave5, L5, ave6, L6, ave7, L7, ave8, L8, ave9, L9, ave10, L10, ave11, L11, ave12, L12, ave13, L13, ave14, L14, ave15, L15, ave16, L16 = compress()
ave_t.append((ave1, L1))
ave_t.append((ave2, L2))
ave_t.append((ave3, L3))
ave_t.append((ave4, L4))
ave_t.append((ave5, L5))
ave_t.append((ave6, L6))
ave_t.append((ave7, L7))
ave_t.append((ave8, L8))
ave_t.append((ave9, L9))
ave_t.append((ave10, L10))
ave_t.append((ave11, L11))
ave_t.append((ave12, L12))
ave_t.append((ave13, L13))
ave_t.append((ave14, L14))
ave_t.append((ave15, L15))
ave_t.append((ave16, L16))
def decompress():
    vec = divide_vectors(matrix)
    for i in range(len(ave_t)):
        for l in range(len(ave_t[i][1])):
            c = 0
            m_vectors = ave_t[i][1]
            m = m_vectors[l]
            for j in range(len(vec)):
                if areSame(m, vec[j]) == 1:
                    c = j
                    break
                else:
                    continue
            vec[j] = swap_matrix(vec[j], ave_t[i][0])
    return vec

def swap_matrix(m1, m2):
    for i in range(4):
        for j in range(4):
            m1[i][j] = m2[i][j]
    return m1

def areSame(A, B):
    for i in range(4):
        for j in range(4):
            if A[i][j] != B[i][j]:
                return 0
    return 1
vec = decompress()
full_matrix = []
for i in range(256):
    a = []
    for j in range(256):
        a.append(0)
    full_matrix.append(a)
full_matrix = np.array(full_matrix)
count = 0
i = 0
j = 0
while j in range(256):
    i = 0
    while i in range(256):
        full_matrix[i:i+4, j:j+4] = vec[count]
        count += 1
        i += 4
    j += 4

print(full_matrix.shape)
print(imgArr)
print(np.min(imgArr), np.max(imgArr))
savePath = 'Something.png'
decoded_image = Image.fromarray(full_matrix)
decoded_image.save(savePath)