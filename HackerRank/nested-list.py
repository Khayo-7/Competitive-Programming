if __name__ == '__main__':
    
    n = input()
    
    records = {}
    min1 = float('inf')
    min2 = float('inf')
    
    for _ in range(int(n)):
        name = input()
        score = float(input())
   
        if score in records:
            records[score].append(name)
        else:
            records[score] = [name]
        
        if score < min1:
            min2 = min1
            min1 = score
        elif score < min2 and score != min1:
            min2 = score

    for name in sorted(records[min2]):
        print(name)
