N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def RotateArr(arr, si, sj, ei, ej):
    # 회전할 부분의 요소를 저장
    top_left = arr[si][sj]

    # 위쪽
    for j in range(sj, ej):
        arr[si][j] = arr[si][j + 1]

    # 오른쪽
    for i in range(si, ei):
        arr[i][ej] = arr[i + 1][ej]

    # 아래쪽
    for j in range(ej, sj, -1):
        arr[ei][j] = arr[ei][j - 1]

    # 왼쪽
    for i in range(ei, si, -1):
        arr[i][sj] = arr[i - 1][sj]

    # 첫 번째 요소를 회전된 위치에 넣기
    arr[si + 1][sj] = top_left


# 회전할 사각형의 경계 설정
ei = N - 1
ej = M - 1
si, sj = 0, 0

while ei > si and ej > sj:
    # 회전할 요소의 개수
    turn = (ej - sj + ei - si) * 2
    R = R % turn  # R을 turn으로 나눈 나머지로 최적화

    for _ in range(R):
        RotateArr(arr, si, sj, ei, ej)

    # 다음 내부 사각형으로 이동
    ei -= 1
    ej -= 1
    si += 1
    sj += 1

# 결과 출력
for i in arr:
    print(*i)
https://www.acmicpc.net/problem/16926