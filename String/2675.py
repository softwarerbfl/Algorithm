T=int(input())
for i in range(T):
    a, arr = input().split()
    for x in arr:
        print(x*int(a), end='')
    print()