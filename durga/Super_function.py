class P:
    def m1(self):
        print("parent")
class C(P):
    def m1(self):
        #super().m1()
        print("child")
a=C()
a.m1()