
def hanoi (a,b,c,n,k):
    if k ==2**(n-1):
        print("{} {}".format(a,c))
    elif k <2**(n-1):
         return hanoi (a,c,b,n-1,k)
    else:
        return hanoi (b,a,c,n-1,k-2**(n-1))



round_num=int(input())
for i in range(round_num):
    n, k = map(int, input().split())
    hanoi(1,2,3,n,k)
