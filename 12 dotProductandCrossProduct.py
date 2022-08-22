n = 3
def dotProduct(vector_A, vector_B):
 
    product = 0
 
    # Loop for calculate dot product
    for i in range(0, n):
        product = product + vector_A[i] * vector_B[i]
 
    return product
 
# Function to find cross product of two vector array.
def crossProduct(vector_A, vector_B, cross_P):
 
    cross_P.append(vector_A[1] * vector_B[2] - vector_A[2] * vector_B[1])
    cross_P.append(vector_A[2] * vector_B[0] - vector_A[0] * vector_B[2])
    cross_P.append(vector_A[0] * vector_B[1] - vector_A[1] * vector_B[0])
 
 
# Driver function
if __name__=='__main__':
    vector_A = [7, -5, 4]
    vector_B = [2, 6, -3]
    cross_P = []
 
# dotProduct function call
    print("Dot product:", end =" ")
    print(dotProduct(vector_A, vector_B))
 
# crossProduct function call
    print("Cross product:", end =" ")
    crossProduct(vector_A, vector_B, cross_P)
 
# Loop that print cross product of two vector array.
    for i in range(0, n):
        print(cross_P[i], end =" ")
