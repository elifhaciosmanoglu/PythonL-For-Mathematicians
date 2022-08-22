# value1 and value2 should be the same length.
def hamming_distance(value1, value2): 
    distance = 0
    L = len(value1)
    for i in range(L):
        if value1[i] != value2[i]:
            distance += 1
    return distance
example_dist = hamming_distance("11001", "01000")
print(example_dist)
