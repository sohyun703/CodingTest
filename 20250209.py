https://www.acmicpc.net/problem/2693

T = int(input())

for tc in range(1,T+1):
    Tlist = list(map(int,input().split()))
    Tlist.sort(reverse=True)
    print(Tlist[2])