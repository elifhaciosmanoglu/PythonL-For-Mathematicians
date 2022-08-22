def form_series(coef_a, coef_b, n):
    """
    This method creates the Binomial Theorem Series.
    coef_a: coefficient of a
    coef_b: coefficient of b
    n: power of the equation
    """
    def formatting(nextTerm, coeffs):
        """
        This is an inner function which formats the terms of the binomial series.
        next_term: coefficient of next term powers of a and b
        """
        if nextTerm == 1:
            coeffs.insert(0, "")
        else:
            coeffs.insert(0, nextTerm)
        if coeffs[1] == "^0" and coeffs[2] == "^0":
            return coeffs[0]
        elif coeffs[1] == "^0":
            return "{}b{}".format(coeffs[0], coeffs[2])
        elif coeffs[2] == "^0":
            return "{}a{}".format(coeffs[0], coeffs[1])
        elif coeffs[1] == "^1" and coeffs[2] == "^1":
            return "{}ab".format(coeffs[0])
        elif coeffs[1] == "^1":
            return "{}ab{}".format(coeffs[0], coeffs[2])
        elif coeffs[2] == "^1":
            return "a{}b".format(coeffs[0], coeffs[1])
        return "{}a{}b{}".format(coeffs[0], coeffs[1], coeffs[2])
    # Initializing a list named as `series`
    series = list()
    # Calculating the First Term, Formatting it and Appending it to our Series
    firstTerm = pow(coef_a, n)
    coeffs = ["^" + str(n), "^0"]
    series.append(formatting(firstTerm, coeffs) + "  +  ")
    nextTerm = firstTerm
    # Calculating, Formatting and Appending the remaining terms.
    for i in range(1, n + 1):
        # We can find next term using the previous term and the formula mentioned below.
        nextTerm = int(nextTerm * coef_b * (n - i + 1) / (i * coef_a))
        # Pre-formatted list creation
        coeffs = ["" if x == 1 else "^" + str(x) for x in [n - i, i]]
        # Append till last term is not reached
        if i != n:
            series.append(formatting(nextTerm, coeffs) + "  +  ")
        # Append the last term.
        else:
            series.append(formatting(nextTerm, coeffs))
    # Joining the series as a string and printing it.
    print("".join(series))
if __name__ == "__main__":
    # Taking inputs
    print("( a + b ) ^ n")
    coef_a = int(input("Enter the coefficient of a: "))
    coef_b = int(input("Enter the coefficient of b: "))
    n = int(input("Enter n: "))
    print("({}a+{}b)^{}  =  ".format(coef_a, coef_b, n),end=" ")
    
    form_series(coef_a, coef_b, n)
