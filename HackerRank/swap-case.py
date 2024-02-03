def swap_case(s):
    
    swapped = []
    
    for ch in s:
        if ch.islower():
            swapped.append(ch.upper())
        else:
            swapped.append(ch.lower())
            
    return ''.join(swapped)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    