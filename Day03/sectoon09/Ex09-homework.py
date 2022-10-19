'''
[회원가입]
아이디를 입력하세요 (3글자 이상) >>>
>3글자 이상 입력해 주세요.

아이디를 입력하세요 (3글자 이상) >>>

패스워드를 입력하세요(영문 숫자 퍼함 8자이상) >>>
>영문 숫자 포함 8자이상 입력해 주세요

패스워드를 한번더 입력하세요 >>>
>일치하지 않습니다. 다시 입력해주세요

패스워드를 입력하세요(영문 숫자 퍼함 8자이상) >>>
>영문 숫자 포함 8자이상 입력해 주세요

패스워드 한번더 입력하세요 >>>

회원가입 완료!!

[로그인]
아이디를 입력하세요 >>>
>아이디가 일치하지 않습니다

아이디를 입력하세요 >>>

패스워드를 입력하세요 >>>
>패스워드가 일치하지 않습니다.

패스워드를 한번더 입력하세요 >>>

로그인 완료!!
'''

id = None
pwd = None

# 아이디 입력
while True:
    id = input('아이디를 입력하세요 (3글자 이상) >>> ')
    if len(id) >= 3:
        break
    print('> 3글자 이상 입력해 주세요.')

# 패스워드 입력
while True:
    pwd = input('패스워드를 입력하세요(영문 숫자 퍼함 8자이상) >>> ')
    isContainAlpha = False
    isContainNumeric = False

    for ch in pwd:

        if ch.isalpha():
            isContainAlpha = True
        elif ch.isnumeric():
            isContainNumeric = True

    if not isContainAlpha or not isContainNumericor or len(pwd) < 8:
        print('>영문 숫자 포함 8자이상 입력해 주세요.')
        continue

    pwdChk = input('패스워드 한번더 입력하세요 >>> ')
    if pwd != pwdChk:
        print('>일치하지 않습니다. 다시 입력해주세요.')
        continue
    break

print('회원가입 완료!!')

# 로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 >>> ')
    if id == loginId:
        break
    print('>아이디가 일치하지 않습니다.')

# 로그인 패스워드
while True:
    loginpwd = input('패스워드를 입력하세요 >>> ')
    if pwd == loginpwd:
        break
    print('>패스워드가 일치하지 않습니다.')

print('로그인 완료!!')