import random


class ExceptionType(Exception):
    pass


class Matrix:
    def __init__(self, list_1: list):
        if isinstance(list_1, (list, tuple)):
            for i in list_1:
                if not all(isinstance(k, (int, float)) for k in i):
                    raise ExceptionType("Error:should have only number values ")
        else:
            raise ExceptionType("Error: not list or tuple")

        row = len(list_1[0])
        for i in list_1[1:]:
            if row != len(i):
                raise ExceptionType("Error: lengths are not equal")

        self.list_1 = list_1

    def __add__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise ExceptionType(
                "Error: excepted type Matrix found {}".format(type(other_matrix))
            )

        if not self.same_dimension_with(other_matrix):
            raise ExceptionType("Error: dimensions are not the same")

        return [
            [
                self.list_1[i][j] + other_matrix.list_1[i][j]
                for j in range(len(self.list_1[0]))
            ]
            for i in range(len(self.list_1))
        ]

    def __sub__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise ExceptionType(
                "Error: excepted type Matrix found {}".format(type(other_matrix))
            )

        if not self.same_dimension_with(other_matrix):
            raise ExceptionType("Error: dimensions are not the same")

        return [
            [
                self.list_1[i][j] - other_matrix.list_1[i][j]
                for j in range(len(self.list_1[0]))
            ]
            for i in range(len(self.list_1))
        ]

    def __mul__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise ExceptionType(
                "Error: excepted type Matrix found {}".format(type(other_matrix))
            )

        if not len(self.list_1[0]) == len(other_matrix.list_1):
            raise ExceptionType("Error: dimensions are not the same")

        return [
            [
                sum(a * b for a, b in zip(self_row, other_column))
                for other_column in zip(*other_matrix.list_1)
            ]
            for self_row in self.list_1
        ]

        # return np.dot(self.list_1, other_matrix.list_1)

    def __str__(self):

        str1 = ""
        count = 0
        for i in self.list_1:
            line = " ".join(map(str, i))

            if count == 0:
                str1 += "".join(["⌈", str(line), "⌉\n"])
            elif count == len(self.list_1) - 1:
                str1 += "".join(["⌊", str(line), "⌋\n"])
            else:
                str1 += "".join(["|", str(line), "|\n"])

            count += 1

        return str1

    # def determinant(self):
    def __minor(self, i, j):
        return [
            row[:j] + row[j + 1:] for row in (self.list_1[:i] + self.list_1[i + 1:])
        ]

    def determinant(self):

        if not self.is_square():
            raise ExceptionType("ERROR: Matrix should be square to have determinant")

        if len(self.list_1) == 2:
            return (
                self.list_1[0][0] * self.list_1[1][1]
                - self.list_1[0][1] * self.list_1[1][0]
            )

        determinant = 0
        for element in range(len(self.list_1)):

            matrix_det = Matrix(self.__minor(0, element))
            determinant += (
                ((-1) ** element) * self.list_1[0][element] * matrix_det.determinant()
            )
        return determinant

    def inverse(self):
        if not self.is_square():
            raise ExceptionType("ERROR: Matrix should be square to have inverse")
        det = self.determinant()
        if det == 0:
            raise ExceptionType(
                "ERROR: Matrix does not have an inverse, determinant of matrix is 0"
            )
        if len(self.list_1) == 2:
            return [
                [self.list_1[1][1] / det, -1 * self.list_1[0][1] / det],
                [-1 * self.list_1[1][0] / det, self.list_1[0][0] / det],
            ]

        cofactors = []

        for row in range(len(self.list_1)):
            cofactor_row = []
            for column in range(len(self.list_1)):
                minor_matrix = Matrix(self.__minor(row, column))
                cofactor_row.append(
                    ((-1) ** (row + column)) * minor_matrix.determinant(),
                )
            cofactors.append(cofactor_row)
        cof = Matrix(cofactors)
        cof = list(map(list, zip(*cof.list_1)))
        for row in range(len(cof)):
            for column in range(len(cof)):
                cof[row][column] = round(cof[row][column] / det, 2)
        return cof

    def same_dimension_with(self, other_matrix):
        if len(self.list_1) == len(other_matrix.list_1) and len(self.list_1[0]) == len(
            other_matrix.list_1[0]
        ):
            return True
        else:
            return False

    def is_square(self):
        if len(self.list_1) == len(self.list_1[0]):
            return True
        else:
            return False

    @staticmethod
    def random_matrix(row: int, column: int) -> object:
        return Matrix(
            [
                [round(10 * random.random(), 1) for _ in range(column)]
                for _ in range(row)
            ]
        )


if __name__ == "__main__":
    pass
