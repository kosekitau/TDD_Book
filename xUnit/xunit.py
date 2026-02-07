class WasRun:
    def __init__(self, name) -> None:
        self.wasRun = None
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()

    def testMethod(self) -> None:
        pass
        self.wasRun = 1


test: WasRun = WasRun(name="testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
