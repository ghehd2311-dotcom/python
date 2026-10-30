# cnt =0

# while True: 
#     비번 = int(input('비밀번호'))

#     if(비번 == 1234):
#         print('비번이 맞았습니다')
#         break
#     else:
#         print('비밀번호 다시 입력하세요')
#         cnt +=1

#     if(cnt == 5):
#         print('10분 뒤 다시 실행하세요.')
#         break


cnt =0
할인코드 = 1234

while cnt < 5: 
    입력번호 = int(input('쿠폰번호를 입력해주세요: '))

    if(입력번호 == 할인코드):
        print('쿠폰 적용 성공! 10%할인')
        break
    else:
        cnt +=1

    if(cnt == 5):
        print('쿠폰 입력 횟수 초과!')
        