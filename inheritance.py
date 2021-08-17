class A:
    def b(self):
        return "Coming from class A"

class B(A):
    def b(self):
        return "Coming from class B"

class C(A):
    def b(self):
        return "Coming from class C"

class D(C,B):
    ...