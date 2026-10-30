age = int(input('나이를 입력해주세요:'))

if(age < 8):
    print('8세 미만 무료')
elif(8<age<=13 ):
    print('8에 이상 13 이하 500원')
elif(13<age<=16 ):
    print('800원')
elif(16<age<=19 ):
    print('1100원')
else:
    print('1500원')
