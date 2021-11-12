class A:
    def __init__(self):
        print("A initiated")


class B(A):
    def __init__(self):
        super().__init__()
        print("B initiated")


class C(B):
    def __init__(self):
        super(C, self).__init__()  # super().__init()
        print("C initiated")


c = C()

########################################################


class A1:
    def __init__(self):
        print("A initiated")


class B1(A1):
    def __init__(self):
        super().__init__()
        print("B initiated")


class C1(B1):
    def __init__(self):
        super(B1, self).__init__()
        print("C initiated")


c1 = C1()
