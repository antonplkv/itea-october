class A:

    def start(self):
        print('A')


class B(A):
    def start(self):
        print('B')


class C(B):
    def start(self):
        super(C, self).start()


C().start()