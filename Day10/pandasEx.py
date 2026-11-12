# pandasEx.py
# 데이터 분석 Pandas도구를 설치
# python -m pip install pandas

# 설치 확인
# - pandasEx.py 파이썬 파일이 실행하면
#   위에서 부터 하나씩 읽어서 실행한다.
# import 문을 만나면 pandas도구를 포함한다.
# import pandas as pd

# 버전확인하는 방법
# 파이썬 실행 ctrl + f5
print()
#print("판다스 버전 확인: ",pd.__version__)

# 판다스 버전 3.1.0 쓰는데 버전이 달라도
# 상관없다!

# 판다스라는 도구 없으면?
# 파이썬이 제공해주는 기능도 모르면 코드가 길어진다.
data = [80,90,80,90,50,60]

합계 = 0


for 점수 in data:
    합계 += 점수

평균 = 합계 / len(data)

print(평균)

#----------------------------------------------------
# sum() 합계를 내주는 기능(함수)
data = [80,90,80,90,50,60]

합계 = sum(data)
print(합계 / len(data))

#----------------------------------------------------
# 데이터가 비정상적으로 들어올때
# None 데이터 없음
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
#
# data = [80,90,80,None,50,600, -10, "ㅓ"]

# # 데이터를 하나씩 꺼내서 None 제외시키는 코드
# for 데이터 in data:
#     if 데이터 == None or 데이터 >100:
#         data.remove(None)

# print(data)
#합계 = sum(data)
#print(합계 / len(data))

#--------------------------------------------------
data2 = ["12,000", "8,000", "8,000", "5,000"]

#sum() 모든 숫자든 문자든 더하는 기능
# 파이썬에서는 문자 + 문자 = 연결
print(sum(data2))

#------------------------------------------------
# 데이터를 정리하고 쉽게 분석하기 위해서 판다스를 쓴다