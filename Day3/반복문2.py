# # num =1
# # while num <=5:
# #     print(f'{num}생활관 점호') 

# progress = 0
# while progress < 100:
#     print(f'게임 로딩중... 진행률{progress}%')
#     progress += 10

# print('게임 시작')

# cnt = 0 #5회 제한
# success =  1234

# while cnt < 5:
#     password = int(input('비밀번호를 입력해주세요: '))

#     if(password == success): 
#         print('로그인에 성공하셨습니다')
#         break
#     else:
#         print('비밀번호를 다시 입력해주세요')
#         cnt += 1

#     if(cnt == 5):
#         print('10분후에 다시 입력해주세요')

#up down

cnt = 0 #5회 제한
success =  1234

while cnt < 5:
    password = int(input('숫자를 입력해주세요: '))

    if(password == success): 
        print('성공하셨습니다')
        break
    elif(password > success):
        print('UP')
        cnt += 1
    elif(password < success):
        print('down')
        cnt += 1
    if(cnt == 5):
        print('게임에서 졌습니다')