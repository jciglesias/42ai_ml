class Matrix:
    data: list[list]
    shape: tuple[int, int]
    
    def __init__(self, attr):
        if isinstance(attr, list):
            self.data = attr
            self.shape = (len(attr), len(attr[0]) if attr else 0)
        elif isinstance(attr, tuple) and len(attr) == 2:
            self.shape = attr
            self.data = [[0 for _ in range(attr[1])] for _ in range(attr[0])]
        else:
            raise ValueError("Invalid attribute for Matrix initialization")
    
    def __add__(self, rmatrix):
        if not isinstance(rmatrix, Matrix):
            raise ValueError("Can only add another Matrix")
        if self.shape != rmatrix.shape:
            raise ValueError("Matrices must have the same shape for addition")
        result_data = operation_matrix(self, rmatrix, op['+'])
        return type(self)(result_data)
    
    def __radd__(self, lmatrix):
        return self.__add__(lmatrix)

    def __sub__(self, rmatrix):
        if not isinstance(rmatrix, Matrix):
            raise ValueError("Can only subtract another Matrix")
        if self.shape != rmatrix.shape:
            raise ValueError("Matrices must have the same shape for subtraction")
        result_data = operation_matrix(self, rmatrix, op['-'])
        return type(self)(result_data)

    def __rsub__(self, lmatrix):
        if not isinstance(lmatrix, Matrix):
            raise ValueError("Can only subtract another Matrix")
        if self.shape != lmatrix.shape:
            raise ValueError("Matrices must have the same shape for subtraction")
        result_data = operation_matrix(lmatrix, self, op['-'])
        return type(self)(result_data)

    def __truediv__(self, scalar):
        pass

    def __rtruediv__(self, scalar):
        pass

    def __mul__(self, scalar):
        pass

    def __rmul__(self, scalar):
        pass

    def __str__(self):  
        return '\n'.join(['[' + ' '.join(map(str, row)) + ']' for row in self.data])

    def __repr__(self):
        pass

    def T(self):
        pass

op = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

def operation_matrix(matrix_a, matrix_b, op_func):
    return [[op_func(matrix_a.data[i][j], matrix_b.data[i][j]) for j in range(matrix_a.shape[1])] for i in range(matrix_a.shape[0])]

def check_vector_shape(l: list):
    if len(l) == 1 or all(len(row) == 1 for row in l):
        return True
    return False

class Vector(Matrix):
    def __init__(self, attr):
        if isinstance(attr, list) and check_vector_shape(attr):
            super().__init__(attr)
        elif isinstance(attr, tuple) and len(attr) == 2:
            if attr[0] == 1 or attr[1] == 1:
                super().__init__(attr)
        else:
            raise ValueError("Invalid attribute for Vector initialization")
    
    def dot(self, vec):
        if not isinstance(vec, Vector):
            raise ValueError("Dot product requires another Vector")
        if self.shape[0] != vec.shape[0] or self.shape[1] != vec.shape[1]:
            raise ValueError("Vectors must be of the same shape for dot product")
        result = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result += self.data[i][j] * vec.data[i][j]
        return result
            
