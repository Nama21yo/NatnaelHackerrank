def sort_transformed_array(nums, a, b, c):
    def quadratic(num):
        return a * (num ** 2) + b * (num) + c
    n = len(nums)
    l = 0
    r = n - 1
    k = 0 if a < 0 else n - 1
    result = [0] * n
    
    while l <= r:
        lsolve = quadratic(nums[l])
        rsolve = quadratic(nums[r])
        if a < 0:
            if lsolve <= rsolve:
                result[k] = lsolve
                l += 1
            else:
                result[k] = rsolve
                r -= 1
            k += 1
        else:
            # k = n - 1
            if lsolve >= rsolve:
                result[k] = lsolve
                l += 1
            else:
                result[k] = rsolve
                r -= 1
            k -= 1
    return result
                
            
    
            
        
        
print(sort_transformed_array([-4, -2, 2, 4], 1 , 3, 5))    
print(sort_transformed_array([-4, -2, 2, 4], -1 , 3, 5))