def check(st) :
    n = len(st)
    # Compute sum of even and odd digit
    oddDigitSum = 0
    evenDigitSum = 0
    for i in range(0,n) :
        # When i is even, position of digit is odd
        if (i % 2 == 0) :
            oddDigitSum = oddDigitSum + ((int)(st[i]))
        else:
            evenDigitSum = evenDigitSum + ((int)(st[i]))
    # Check its difference is divisible by 11 or not
    return ((oddDigitSum - evenDigitSum) % 11 == 0)
# Driver code
st = input("Please write the number:")
if(check(st)) :
    print( "Yes, this number is divisible by 11. ")
else :
    print("No, this number is not divisible by 11.")

