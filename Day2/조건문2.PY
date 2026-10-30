# if False:
#     print('정답')
# else:
#     print('거짓')

# 사이즈 = input('사이즈 선택(S/M/L)')
# if(사이즈 == 'S'):
#     print('3000원')
# elif(사이즈 == 'M'):
#     print('4000원')
# elif(사이즈 == 'L'):
#     print('5000원')

# battery = int(input('베터리 잔량:'))
# res = ''
# if(battery > 80):
#    res =   '충분'
# elif(battery > 30):
#     res ='정상 사용 가능'
# elif(battery > 10):
#     res = '충전 준비'
# else:
#    res = '충전 필요'
# print(res)

# answer = 30
# req = int(input('숫자를 입력해주세요: '))

# if(answer == req):
#     print('정답입니다')
# else:
#     print('오답입니다')


# #2468, 1111
# answer = 2468
# password = int(input('비밀번호를 입력해주세요: '))
# message = ''

# if(answer == password):
#     message = '금고열림'

# #음수값을 입력했을때    
# elif(password < 0):
#     message = '비밀번호는 양수만 사용 할 수 있습니다'
# else:
#     message = '비밀번호를 확인해주세요'

# print(message)



# #가위바위보 함수
# #5번 경기 중 승리,패배 횟수 카운트
# win,loss,draw = 0,0,0;
# def game(player, isEnd):
#     global win,loss,draw
#     if(player == '가위'):
#         print('비겼습니다 \n')
#         draw += 1
#     elif(player == '바위'):
#         print('이겼습니다 \n')
#         win += 1
#     elif(player == '보'):
#         print('졌습니다 \n')
#         loss += 1

#     if(isEnd):
#         print('결과는??? 승:',win,'패:',loss,'비김:',draw)

# i = 1
# while i <= 5:
#     me = input('가위바위보!!!: ')

#     if me not in ['가위', '바위', '보']:
#         print('잘못 입력하셨습니다. 가위, 바위, 보 중에서 입력해주세요.\n')
#         continue
        
#     if(i == 5):
#         game(me,True)
#     else:
#         game(me,False)

#     i += 1 


#가위바위보 함수
#5번 경기 중 승리,패배 횟수 카운트
import random
win,loss,draw = 0,0,0;
def game(player, isEnd):
    global win,loss,draw
    computer = random.choice(['가위', '바위', '보'])

    print('컴퓨터: ',computer,'VS', '나: ', player)
    if(player == computer):
        print('비김')
        draw +=1
    elif (player == '가위' and computer == '보') or \
         (player == '바위' and computer == '가위') or \
         (player == '보' and computer == '바위'):
        print('이겼습니다!\n')
        win += 1
    else:
        print('졌습니다!\n')
        loss += 1

    if(isEnd):
        print('결과는??? 승:',win,'패:',loss,'비김:',draw)

i = 1
while i <= 5:
    me = input('가위바위보!!!: ')

    if me not in ['가위', '바위', '보']:
        print('잘못 입력하셨습니다. 가위, 바위, 보 중에서 입력해주세요.\n')
        continue
        
    if(i == 5):
        game(me,True)
    else:
        game(me,False)

    i += 1 
    
    