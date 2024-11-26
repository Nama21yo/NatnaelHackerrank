from collections import defaultdict
def high_five(items):
    hashmap = defaultdict(list)
    items = sorted(items, reverse=True)
    
    for id, score in items:
        hashmap[id].append(score)
        
    result = []
    for id in hashmap:
        scores = hashmap[id]
        total = sum(scores[:5])
        average = total // 5
        result.append([id, average])
    result.sort()  
    return result
    
        
        
    
print(high_five([
  [1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]
]))