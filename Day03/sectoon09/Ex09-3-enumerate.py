'''
enumerate
         List, Tuple, String  등 여러가지 자료형을 입력받으면
         인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(month):
    print('{}월 = {}일'.format(month, day))