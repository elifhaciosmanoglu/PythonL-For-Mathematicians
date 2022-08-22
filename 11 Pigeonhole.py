def pigeonhole_sort(n):
    minimum = min(n)
    maximum = max(n)
    size = maximum - minimum + 1
    pigeonholes = [0] * size
    for i in n:
        pigeonholes[i - minimum] += 1
    j = 0
    for count in range(size):
        while pigeonholes[count] > 0:
            pigeonholes[count] -= 1
            n[j] = count + minimum
            j += 1
              
  
n = [11, 17, 19, 10,  9]
print("The array is :")
print(n)
print("Sorted array is :")
pigeonhole_sort(n)
print(n)
