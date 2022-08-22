# A[] represents coefficients of first polynomial
# B[] represents coefficients of second polynomial
# m and n are sizes of A[] and B[] respectively
def multiply(A, B, m, n):
 
    prod = [0] * (m + n - 1);
     
    # Multiply two polynomials term by term
     
    # Take every term of first polynomial
    for k in range(m):
         
        # Multiply the current term of first polynomial with every term of second polynomial.
        for j in range(n):
            prod[k + j] += A[k] * B[j];
 
    return prod;
 
# A utility function to print a polynomial
def printPoly(poly, n):
 
    for k in range(n):
        print(poly[k], end = "");
        if (k != 0):
            print("x^", k, end = "");
        if (k != n - 1):
            print(" + ", end = "");
 
# The following array represents polynomial 5 + 10x^2 + 6x^3
A = [5, 0, 5, 6];
 
# The following array represents polynomial 1 + 2x + 4x^2
B = [1, 3, 4];
m = len(A);
n = len(B);
 
print("First polynomial is ");
printPoly(A, m);
print("\nSecond polynomial is ");
printPoly(B, n);
 
prod = multiply(A, B, m, n);
 
print("\nProduct polynomial is ");
printPoly(prod, m+n-1);
