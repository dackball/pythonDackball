'''
튜플
   단일 변수에 여러 항목을 저장하는데 사용 된다.
   순서가 있고 변경할 수 없는 List
   둥근 괄호로 작성된다
'''

thistuple = ("피카츄", "라이츄", "파이리")
print(len(thistuple))

# 항목 가져오기
thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

# 튜플값 변경 방법
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
thiscast = list(thistuple)
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)


# 튜플 압축 풀기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple

print(type(p1))
print(p2)
print(p3)
print(p4)

#두개 튜플 조인'
thistuple1 = ("a", "b", "c", "d")
thistuple2 = ("e", "f", "g", "h")
