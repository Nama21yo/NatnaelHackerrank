# 1 2 3 4 5
#     ^
#   3 - 1 + 4
def diet_plan(calories, k, lower, upper):
    l = 0
    n = len(calories)
    current_calorie = 0
    point = 0

    for r in range(n):
        current_calorie += calories[r]
        if r - l + 1 > k:
            current_calorie -= calories[l]
            l += 1
        if r - l + 1 == k:
            if current_calorie < lower:
                point -= 1
            elif current_calorie > upper:
                point += 1
    return point
        

print(diet_plan([1,2,3,4,5], 1, 3,3))
print(diet_plan([3,2], 2, 0,1))
print(diet_plan([6,5,0,0], 2, 1,5))