def TINGARIKAI(n):
    if n<= 2:
        return n
    if n == 3:
        return 4
    return TINGARIKAI(n-1)+TINGARIKAI(n-2)+TINGARIKAI(n-3)
    
n = int(input())
print(TINGARIKAI(n))