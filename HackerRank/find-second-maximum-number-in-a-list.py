if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_arr = sorted(list(set(arr)))
    
    print(sorted_arr[-2])