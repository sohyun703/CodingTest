https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do#none

T = int(input())


for tc in range(1,T+1):
    ans = 0

    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    mnum = int(1e9)
    Mnum = -1
    for i in range(0, N-M+1):
        ak = sum(arr[i:i+M])
       # print(arr[i:i+M])
        #print(ak)
        mnum = min(ak,mnum)
        Mnum = max(ak,Mnum)

        #print(mnum,Mnum)
    ans = Mnum-mnum
    print(f'#{tc} {ans}')


#구간합 해결하기 끝부분이랑 윈도우 슬라이싱 (시작 포함 끝 안 포함)