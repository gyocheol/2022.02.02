# 31 아래 코드의 실행 결과를 예상해보세요.
a = "3"
b = "4"
print(a + b)

# 예상 : 34
# 정답 : 34

# 32 아래 코드의 실행 결과를 예상해보세요.
print("Hi" * 3)

# 예상 : HiHiHi
# 정답 : HiHiHi

# 33 화면에 '-'를 80개 출력하세요.
print('-' * 80)

# 34 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
#    변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
print((t1 + ' ' + t2 + ' ') * 4)

# 35 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print('이름: %s 나이: %d' %(name1, age1))
print('이름: %s 나이: %d' %(name2, age2))

# 36 문자열의 format( ) 메서드를 사용해서 35번 문제를 다시 풀어보세요.
print('이름: {} 나이: {}'.format(name1, age1))
print('이름: {} 나이: {}'.format(name2, age2))

# 37 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 38 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
num = "5,969,782,550"

rep = num.replace(',', '')
intN = int(rep)
print(intN,type(intN))

# 39 다음과 같은 문자열에서 '2020/03'만 출력하세요.
quarter = "2020/03(E) (IFRS연결)"
print(quarter[:7])

# 40 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print(data.strip())

# 41 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

# 42 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker2 = "BTC_KRW"
print(ticker2.lower())

# 43 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
h = 'hello'
h = h.capitalize()
print(h)

# 44 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

# 45 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# 내가 한것 : print(file_name.endswith('xlsx'or'xls'))
# 정답 : print(file_name.endswith(('xlsx','xls')))

# 46 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name1 = "2020_보고서.xlsx"
print(file_name1.startswith('2020'))

# 47 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split())

# 48 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
b = "btc_krw"
print(b.split('_'))

# 49 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
d = "2020-05-01"
print(d.split('-'))

# 50 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data2 = "039490     "
print(data2.rstrip())

# 왼쪽 공백 제거
data3 = "     039490"
print(data3.lstrip())