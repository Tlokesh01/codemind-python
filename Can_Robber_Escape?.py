x = int(input())
l = list(map(int,input().split()))
s=0
for i in l:
    if i%2==1:
        s+=1
if s<=2:
    print('YES')
else:
    print('NO')