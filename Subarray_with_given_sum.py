for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    cs = 0
    j=0
    for i in range(n):
        cs += lst[i]
        if(cs > k):
            while(cs > k and j < i):
                cs -= lst[j]
                j+=1
        if(cs == k):
            print(j+1, i+1)
            break
    else:
        print(-1)