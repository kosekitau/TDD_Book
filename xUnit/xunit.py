class WasRun:
    def __init__(self, name) -> None:
        pass
        self.wasRun = None

    def testMethod(self) -> None:
        pass
        self.wasRun = 1


test: WasRun = WasRun(name="testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
