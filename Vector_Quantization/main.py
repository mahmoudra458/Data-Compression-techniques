

# Initialize matrix
import math
import numpy as np
Rows = 6
Cols = 6
vector_size = 2*2
image_matrix = ([1, 2, 7, 9, 4, 11], [3, 4, 6, 6, 12, 12], [4, 9, 15, 14, 9, 9],
                [10, 10, 20, 18, 8, 8], [4, 3, 17, 16, 1, 4], [4, 5, 18, 18, 5, 6])
class vectors:
    def __int__(self):
        self.rows = 0
        self.cols = 0
        self.matrix = []

    def __init__(self, arr, rows, cols):
        count = 0
        matrix = []
        self.matrix = matrix
        self.arr = arr
        self.rows = rows
        self.cols = cols
        for i in range(rows):  # A for loop for row entries
            a = []
            for j in range(cols):  # A for loop for column entries
                a.append(arr[count])
                count += 1
            matrix.append(a)

    def nearest_vector_1(self, matrix1, matrix2):
        subtract1 = 0
        subtract2 = 0
        for i in range(self.rows):
            for j in range(self.cols):
                subtract1 = abs(subtract1) + abs(self.matrix[i][j] - matrix1[i][j])
                subtract2 = abs(subtract2) + abs(self.matrix[i][j] - matrix2[i][j])
        return subtract1, subtract2

    def nearest_vector_2(self, m1, m2, m3, m4):
        subtract1 = 0
        subtract2 = 0
        subtract3 = 0
        subtract4 = 0
        for i in range(self.rows):
            for j in range(self.cols):
                subtract1 = abs(subtract1) + abs(self.matrix[i][j] - m1[i][j])
                subtract2 = abs(subtract2) + abs(self.matrix[i][j] - m2[i][j])
                subtract3 = abs(subtract3) + abs(self.matrix[i][j] - m3[i][j])
                subtract4 = abs(subtract4) + abs(self.matrix[i][j] - m4[i][j])
        return subtract1, subtract2, subtract3, subtract4
#Initialize vector size for codebook
def average_matrix(matrix):
    r = 2
    c = 2
    vector_mat = []
    arr = []
    rows = 0
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    while rows < 6:
        cols = 0
        while cols < 6:
            c0 += matrix[rows][cols]
            c1 += matrix[rows][cols + 1]
            cols += 2
        rows += 2
    arr.append(c0)
    arr.append(c1)
    rows = 1
    while rows < 6:
        cols = 0
        while cols < 6:
            c2 += matrix[rows][cols]
            c3 += matrix[rows][cols + 1]
            cols += 2
        rows += 2
    arr.append(c2)
    arr.append(c3)
    counter = 0
    for i in range(r):  # A for loop for row entries
        a = []
        for j in range(c):  # A for loop for column entries
            a.append(arr[counter]/9)
            counter += 1
        vector_mat.append(a)
    return vector_mat
def If_integer(N):
    X = int(N)
    temp = N - X
    if temp == 0:
        return True
    else:
        return False
def splitting_vectors(matrix, rows, cols):
    matrix_1 = []
    matrix_2 = []
    for i in range(rows):
        a = []
        b = []
        for j in range(cols):
            N = matrix[i][j]
            if If_integer(N):
                a.append(N - 1)
                b.append(N + 1)
            else:
                a.append(int(N))
                b.append(math.ceil(N))
        matrix_1.append(a)
        matrix_2.append(b)
    return matrix_1, matrix_2

vector_list = []
def divide_vectors(matrix_image, rows, cols):
    r = 0
    temp_c = 0
    for count in range(9):
        arr = []
        for i in range(rows):
            c = temp_c
            for j in range(cols):
                arr.append(matrix_image[r][c])
                c += 1
            r += 1
        if count < 2:
            r = 0
            temp_c += 2
        elif 2 <= count < 5:
            r = 2
            if count == 2:
                temp_c = 0
            else:
                temp_c += 2
        elif 5 <= count < 8:
            r = 4
            if count == 5:
                temp_c = 0
            else:
                temp_c += 2
        vector_list.append(vectors(arr, 2, 2))
        #print(arr)

def average_vectors(list_obj, rows, cols, cond):
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    matrix_1 = []
    matrix_2 = []
    matrix_3 = []
    matrix_4 = []
    length1 = 0
    length2 = 0
    length3 = 0
    length4 = 0
    for r in range(rows):
        for c in range(cols):
            c0 = 0
            c1 = 0
            c2 = 0
            c3 = 0
            for i in range(len(list_obj)):
                if list_obj[i][0] == 1:
                    matrix = list_obj[i][1]
                    c0 += matrix[r][c]
                elif list_obj[i][0] == 2:
                    matrix = list_obj[i][1]
                    c1 += matrix[r][c]
                elif list_obj[i][0] == 3:
                    matrix = list_obj[i][1]
                    c2 += matrix[r][c]
                elif list_obj[i][0] == 4:
                    matrix = list_obj[i][1]
                    c3 += matrix[r][c]
            arr1.append(c0)
            arr2.append(c1)
            arr3.append(c2)
            arr4.append(c3)
    for i in range(len(list_obj)):
        if list_obj[i][0] == 1:
            length1 += 1
        elif list_obj[i][0] == 2:
            length2 += 1
        elif list_obj[i][0] == 3:
            length3 += 1
        elif list_obj[i][0] == 4:
            length4 += 1
    count = 0
    for i in range(rows):  # A for loop for row entries
        a = []
        b = []
        c = []
        d = []
        for j in range(cols):  # A for loop for column entries
            a.append(arr1[count]/length1)
            b.append(arr2[count]/length2)
            if cond == 2:
                c.append(arr3[count]/length3)
                d.append(arr4[count]/length4)
            count += 1
        matrix_1.append(a)
        matrix_2.append(b)
        matrix_3.append(c)
        matrix_4.append(d)
    if cond == 1:
        return matrix_1, matrix_2
    elif cond == 2:
        return matrix_1, matrix_2, matrix_3, matrix_4

def associate_matrices(original_matrix, list_objects, m1, m2, m3, m4, condition):
    if condition == 1:
        for ele in range(len(vector_list)):
            near1, near2 = vector_list[ele].nearest_vector_1(m1, m2)
            if near1 <= near2:
                list_objects.append((1, vector_list[ele].matrix))
            else:
                list_objects.append((2, vector_list[ele].matrix))
        return list_objects
    elif condition == 2:
        for ele in range(len(vector_list)):
            near1, near2, near3, near4 = vector_list[ele].nearest_vector_2(m1, m2, m3, m4)
            if near1 <= near2 and near1 <= near3 and near1 <= near4:
                list_objects.append((1, vector_list[ele].matrix))
            elif near2 < near1 and near2 <= near3 and near2 <= near4:
                list_objects.append((2, vector_list[ele].matrix))
            elif near3 < near1 and near3 < near2 and near3 <= near4:
                list_objects.append((3, vector_list[ele].matrix))
            elif near4 < near1 and near4 < near3 and near4 < near2:
                list_objects.append((4, vector_list[ele].matrix))
        return list_objects


def next_layer(original_matrix):
    divide_vectors(original_matrix, 2, 2)
    array_of_objects = []
    m3 = []
    m4 = []
    matrix_1, matrix_2 = splitting_vectors(average_matrix(original_matrix), 2, 2)
    list_objects = associate_matrices(original_matrix, array_of_objects, matrix_1, matrix_2, m3, m4, 1)
    matrix1, matrix2 = average_vectors(list_objects, 2, 2, 1)
    left_matrix_1, left_matrix_2 = splitting_vectors(matrix1, 2, 2)
    right_matrix_1, right_matrix_2 = splitting_vectors(matrix2, 2, 2)
    list_return = []
    over_all_list = associate_matrices(original_matrix, list_return, left_matrix_1, left_matrix_2, right_matrix_1, right_matrix_2, 2)
    m1, m2, m3, m4 = average_vectors(over_all_list, 2, 2, 2)
    array_of_objects = []
    over_all_list = associate_matrices(original_matrix, array_of_objects, m1, m2, m3, m4, 2)
    m1, m2, m3, m4 = average_vectors(over_all_list, 2, 2, 2)
    array_of_objects = []
    over_all_list = associate_matrices(original_matrix, array_of_objects, m1, m2, m3, m4, 2)
    m1, m2, m3, m4 = average_vectors(over_all_list, 2, 2, 2)
    return over_all_list, m1, m2, m3, m4

list_objects_1, m_1, m_2, m_3, m_4 = next_layer(image_matrix)
print(m_1)
print(m_2)
print(m_3)
print(m_4)
for i in range(len(list_objects_1)):
    print("ID: ", list_objects_1[i][0], "Vector: ", list_objects_1[i][1])
