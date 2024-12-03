def range_addition(length, updates):
    """
    Given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].
    Apply all updates to a zero-indexed array of length length, and return the sum of the array after all updates.

    Example 1:
    Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
    Output: 8
    """
    # Initialize prefix_sum array with zeros
    # prefix_sum[i] will store the sum of elements from index 0 to i (inclusive)
    # prefix_sum[i] = prefix_sum[i - 1] + updates[i - 1][2]

    # Apply updates to prefix_sum array
    #! prefix_sum[start] += inc
    #! prefix_sum[end + 1] -= inc (if end index is not the last index)
    prefix_sum = [0] * length

    for start, end, inc in updates:
        prefix_sum[start] += inc
        if end != length - 1:
            prefix_sum[end + 1] -= inc
    prefix_sum[0] = prefix_sum[0]
    for i in range(1, length):
        prefix_sum[i] = prefix_sum[i - 1] + prefix_sum[i]
    return prefix_sum
print(range_addition(5, [[1,3,2],[2,4,3],[0,2,-2]]))
print(range_addition(10, [[2,4,6],[5,6,8],[1,9,-4]]))