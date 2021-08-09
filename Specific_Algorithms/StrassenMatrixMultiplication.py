import numpy as np

matrix1 = np.array([[2,1], 
            [4,9]])
matrix2 = np.array([[16,7], 
            [54,8]])

def Split(matrix, dimension):
    # split the matrix into 4 equal quadrants with n/2 dimension
    mid = dimension // 2
    Quadrant1 = matrix[0][:mid]
    Quadrant2 = matrix[0][mid:]
    Quadrant3 = matrix[mid][:mid]
    Quadrant4 = matrix[mid][mid:]
    return Quadrant1, Quadrant2, Quadrant3, Quadrant4
    
def Strassen(matrix1, matrix2, dimension):
    if len(matrix1) == 1 and len(matrix2) == 1:
        return matrix1 * matrix2
    else:
        mid = dimension//2

        # get the quadrants for each matrix recursively
        Quadrant1, Quadrant2, Quadrant3, Quadrant4  = Split(matrix1, dimension)
        Quadrant5, Quadrant6, Quadrant7, Quadrant8 = Split(matrix2, dimension)
        
        # recursive calls on each quadrant until we get to 1x1 matrix => find 7 key products
        Product1 = Strassen(Quadrant1, (Quadrant6 - Quadrant8), mid)
        Product2 = Strassen(Quadrant8, (Quadrant1 + Quadrant2), mid)
        Product3 = Strassen(Quadrant5, (Quadrant3 + Quadrant4), mid)
        Product4 = Strassen(Quadrant4, (Quadrant7 - Quadrant5), mid)
        Product5 = Strassen((Quadrant5 +Quadrant8), (Quadrant1 + Quadrant4), mid)
        Product6 = Strassen((Quadrant2 - Quadrant4), (Quadrant7 + Quadrant8), mid)
        Product7 = Strassen((Quadrant1 - Quadrant3), (Quadrant5 + Quadrant6), mid) 

        # final calculation
        Q1 = Product5 + Product4 - Product2 + Product6
        Q2 = Product1 + Product2
        Q3 = Product3 + Product4
        Q4 = Product1 + Product5 - Product3 - Product7

        result = np.vstack((np.hstack((Q1, Q2)), np.hstack((Q3, Q4)))) 
        return result

print(Strassen(matrix1, matrix2, 2))