'''
조건문
     특정 조건을 만족하는지 여부에 따라 실행하는 코드가 달라야 할 때 사용한다.
     들여쓰기를 사용하여 코드의 범위를 정의

     if(조건식)
     if(조건식) else
     if(조건식1) elif(조건식2)
'''
# if(조건식)
a = 7
b = 100
if b > a:
    print("b는 a보다 크다")
# if(조건식) else
a = 7
b = 4
if b >= a:
    print("b는 a보다 크거나 같다")
else:
    print("b는 a보다 작다")

# if(조건식1) elif(조건식2) else
a = 20
b = 3
if b > a:
    print("b는 a보다 크다")
elif a == b:
    print("a는 b와 같다")
else:
    print("a는 b보다 크다")