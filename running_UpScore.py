if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = list(arr)
    scores.sort()
    first,second = -100,-100
    
    for score in scores:
        if first < score:
            second=first
            first = score
    
    print(second)