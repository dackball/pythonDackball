'''
문자열(String)은 하나 이상 연속된 문자(character) 들의 나열.
     파이썬에서 문자열 자료형은 큰 따옴표 (" ") 또는 작은 따옴표(' ') 사이에 위치.
'''

#'hello' 와 "hello" 동일.
print('Hello' == "Hello")

'''
변수에 문자열 
'''

a = "HellO"
print(a)

'''
여러줄 문자열

'''









'''
문자열은 배열입니다
     다른 많은 인기 프로그래밍 언어와 마찬가지로 Python의 문자열은 유니코드 문자를
    나타내는 바이트 배열
    그러나 Python에는 문자데이터 유형이 없으며 단일 문자는 단순한 길이가 1인 문자열
    대괄호[]를 사용하여 문자열의 요소에 액세스 할수 있다.
'''
a="hello"

'''
문자열 인덱싱(indexing)
h e l l o   <== 문자열
0 1 2 3 4   <== 인덱스
-5 -4 -3 -2 -1 <==마이너스 인덱스
'''
print(a[1])
print(a[1] == a[-4])

'''
문자열 슬라이싱 
  슬라이스 구문을 사용하여 문자 볌위를 반환할 수 있다.
  문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 클론으로 구분하여 지정한다.
'''
b = "Hello, World!"
print(b[2:])

# 대문자
a = "Hello, World!"
print(a.upper())

# 소문자
a = "Hello, World!"
print(a.lower())

# 문자열 바꾸기
a = "Hello, World!"
print(a.replace("H", "J"))

# 문자열 연결
a = "Hello"
b = "World"
c = a + " " + b
print(c)
