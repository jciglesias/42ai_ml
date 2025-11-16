from matrix import Matrix, Vector

if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8, 9], [10, 11, 12]])
    scalar = 2
    v = Vector([[1], [2], [3]])

    print("Matrix m1:")
    print(m1)
    print("\nMatrix m2:")
    print(m2)

    print("\nAddition of m1 and m2:")
    print(m1 + m2)

    print("\nSubtraction of m2 from m1:")
    print(m1 - m2)

    print("\nDivision of m1 by scalar:")
    print(m1 / scalar)

    print("\nDivision of scalar by m1:")
    print(scalar / m1)

    print("\nMultiplication of m1 by scalar:")
    print(m1 * scalar)

    print("\nMultiplication of m1 by vector v:")
    print(m1 * v)

    print("\nMultiplication of m1 by m2 (after adjusting dimensions):")
    m3 = Matrix([[7, 8], [9, 10], [11, 12]])
    print(m1 * m3)

    print("\nTranspose of m1:")
    print(m1.T())