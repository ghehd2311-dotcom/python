name = '백호동'
res = type(name)
print(res)

str = '''
    집가고 싶다
'''
str2 = """진짜로"""

print(str, str2)

name = "이서희"
age = 20

print("나는 이름이 ",name,"나이는 " ,age ,"세",sep="")
print("나는 이름이 ",name,"나이는 " ,age ,"세",sep="@")
print("나는 이름이 ",name,"나이는 " ,age ,"세",sep="!")
print("나는 이름이 ",name,"나이는 " ,age ,"세",sep="$")

#문자열 포매팅(f-string)
#- 문자 안에 변수를 집어넣을 수 있다.
print(f"이름은 {name}, 나이는 {age}세")

#문자랑 숫자 더하기 안됌
# print(name + str(age) + '세')
가격 = 12300
가격2 = 13133
print("현제 총금액: ", 가격)
print(f"현제 총금액: {가격}원")
print(f"현제 총금액: {가격:,}원")
print(f"현제 총금액: {가격2:,}원")

수강률 = 0.6
print('현제 달성률: ', 수강률)
# ':' 출력할때 모양 지정
# '.1' 소수점 아래 1자리
# % - 100을  곱해 백분율 표시하고 %로 붙인다.
print(f'현제 달성률: ${수강률:.0%}')