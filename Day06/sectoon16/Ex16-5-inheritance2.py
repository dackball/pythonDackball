
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다')


class D(B, C):
    pass  # 내부 동작 필요 없고 빈 껍데기만 필요할때 pass 사용

x = D()
x.greeting()
print(D.mro())