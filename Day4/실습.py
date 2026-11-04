# 요일 = ['월', '화', '수', '목', '금', '토', '일'];

# print(요일)
# print(요일[0])
# print(요일[-1])
# print(type(요일))

# # 문제3
# 상품 = ["노트북", "마우스", "키보드", "모니터", "웹캠"]
# 가격 = [120000, 25000, 60000, 300000, 45000]

# print(f'{상품[1]}: {가격[1]}')
# print(f'{상품[-1]}: {가격[-1]}')
# print(f'마우스와 키보드 합계 출력: {가격[1] + 가격[2]}')



def solution(n):     
    answer = [[0]*n for _ in range(n)]

    # 시계 방향 이동 방향: 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 현제 좌표 0,0으로 설정    
    x,y = 0,0
    dir = 0
    i = 1
    while i <= n*n:
       answer[x][y] = i
       nx = x + dx[dir]
       ny = y + dy[dir]
             
       if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            dir = (dir + 1) % 4 
            nx = x + dx[dir]
            ny = y + dy[dir]
            
       x, y = nx, ny
       i += 1
    return answer

solution(4)