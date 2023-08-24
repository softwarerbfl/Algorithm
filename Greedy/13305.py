import sys
n=int(sys.stdin.readline())
l=list(map(int, sys.stdin.readline().split()))
price=list(map(int, sys.stdin.readline().split()))

total_price=0 # 지불해야 하는 총 금액
min_price = min(price[:n - 1])
idx = price.index(min_price)
total_price += min_price * (sum(l[idx:]))
tmp_idx=n-1
while idx!=0:
    if tmp_idx==0 or idx==1:
        total_price += price[0]*l[0]
        print(total_price)
        exit()
    min_price = min(price[:idx-1])
    tmp_idx=idx
    idx = price.index(min_price)
    total_price += min_price * (sum(l[idx:tmp_idx]))
print(total_price)