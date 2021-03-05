N = int(input())
an = 0
for i in range(N):
    N1,N2 = map(int,input().split())
    G = N2%N1
    an += G
print(an)