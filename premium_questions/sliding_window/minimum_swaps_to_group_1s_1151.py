def maximum_swaps(data):
    k = data.count(1)
    if k == 0 or k == len(data) - 1:
        return 0
    
    l = 0
    n = len(data)
    swaps = 0
    min_swaps = float("inf")

    for  r in range(n):
        if data[r] != 1:
            swaps += 1
        if r - l + 1 > k:
            if data[l] != 1:
                swaps -= 1
            l +=  1 
        if r - l + 1 == k:
            min_swaps = min(min_swaps, swaps)
    return min_swaps

print(maximum_swaps([0,0,0,1,0,1,1,0]))
print(maximum_swaps([1,0,1,0,1]))
print(maximum_swaps([0,0,0,1,0]))
print(maximum_swaps([1,0,1,0,1,0,0,1,1,0,1]))
