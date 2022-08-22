Number = int(input("Please Enter the Fibonacci Numbers Range = "))
print("Fibonnacci Series:")
first_number = 0
second_number = 1
Sum = 0
i = 0
while(i <  Number):
    print(first_number, end = '  ')
    Sum = Sum + first_number
    Next = first_number + second_number
    first_number = second_number
    second_number = Next
    i = i + 1
print("\nThe Sum of Fibonacci Series Numbers = %d" %Sum)
