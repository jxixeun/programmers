def solution(n: int, m: int):
    for i in range(0, m):
        for j in range(0,n):
            print('*', end='')
        print('')

a, b = map(int, input().strip().split(' '))
solution(a,b)
