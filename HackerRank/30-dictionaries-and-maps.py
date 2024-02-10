# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

record = {}
for _ in range(n):
    name, phone = input().split()
    record[name] = phone

while True: 
    try:
        name = input()

        if name in record:
            print(name + '=' + record[name])
        else:
            print('Not found')
    except:
        break