#엘베
#1~4층 통과, 5층 도착

# i = 1
# while i <=5:
#     if(i < 5):
#         print(f'{i}층 통과')
#     else:
#         print(f'{i}층 도착')
#     i +=1

# 결과 = '도착' if i == 5 else '통과' #삼항 연산자
# # print(결과)

# 입력 = input('id: ')
# 이름 = 입력 if 입력 != '' else '익명'

# print(이름)
# num = int(input('횟수: '))

# i = 0
# while i < num:
#     print('출력')
#     i += 1
num = int(input('줄넘기 횟수: '))
i = 1
while i <= num:
    print(f'{i}번째 줄넘기')
    i += 1
