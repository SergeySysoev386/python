class zero:
    def __init__(self, div, zer):
        self.div = div
        self.zer = zer

    @staticmethod
    def zero1(div, zer):
        try:
            return (div / zer)
        except:
            return (f"делина на ноль нельзя")


print(zero.zero1(10, 1))
print(zero.zero1(10, 0))

