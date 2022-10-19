'''
time 모귤
   시간 처리에 관련된 time 모듈
'''
import time

# 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과 시간을 반환
# 마이크로초
print(time.time())

# ctime() 함수 - 인수로 전달된 ime 시간 형식을 갖춰 변환
print(time.ctime(time.time()))

# 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
# 날짜 데이터를 문자열로 변환
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 인자 초만큼 시스템 일시중지
time.sleep(1)

sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1
