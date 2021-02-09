'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.'''

class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __add__(self, new_matr):
        self.new_matr = new_matr
        row_list = []
        full_list = []
        try:
            for i in range(len(self.matr)):
                for j in range(len(self.new_matr[i])):
                    row_list.append(self.matr[i][j] + self.new_matr[i][j])
                full_list.append(row_list)
                row_list = []
            self.matr = full_list
            return self.matr
        except IndexError:
            print('матрицы не совпадают по размерам')
        except Exception as e:
            print(f'error')
            print(f'Информация об исключении {e}')

    def __str__(self):
        # print("I'm __str__")
        return '\n'.join([''.join(['%d\t' % i for i in row]) for
                          row in self.matr])


matrix_1 = ([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

matrix_2 =([[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]])

my_matr = Matrix(matrix_1)
my_matr + matrix_2
print(my_matr)























# matr=[[0,0,0,0],
#       [0,0,0,0],
#       [0,0,0,0],
#       [0,0,0,0]]
#
# mt=[]
#
# # print(M.list_1[1][1])
# # print(M.list_1[1])
# # print(len(M.list_2))
# for i in range(len(M.list_1)):
#     # print(i, M.list_1[i])
#     for j in range(len(M.list_2[i])):
#         # print('qwerty', M.list_2[i])
#         matr[i][j] = M.list_1[i][j] + M.list_2[i][j]
# # print(matr)
#
# print(str('\n'.join([' '.join([str(j) for j in i]) for i in matr])))

