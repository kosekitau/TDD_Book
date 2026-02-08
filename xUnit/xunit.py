class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        super().__init__(name=name)

    def testMethod(self) -> None:
        pass
        self.wasRun = 1


test: WasRun = WasRun(name="testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
