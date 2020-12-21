class A:
    def a1(self):
        print('A a1')
    
class B(A):
    def a1(self):
        print('B a1')

class C(A):
    def a1(self):
        print('C a1')


class D(C,B):
    pass


a = D()
a.a1()
