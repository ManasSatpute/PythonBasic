class A:
    def print(self):
        print('Class A object.')


class B:
    def prin(self):
        print('Class B object.')


class C(A,B):
    def pri(self):
        print('Class C object.')


o=C()
o.print()
o.prin()
o.pri()