class SameNameTest:
    def __init__(self) -> None:
        self.same_name = 666

    def same_name(self):
        return 'func'

a = SameNameTest()
print(type(a.same_name))
print(a.same_name)
print(a.same_name())