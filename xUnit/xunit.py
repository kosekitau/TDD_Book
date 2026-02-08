class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.wasRun = None
        super().__init__(name=name)

    def testMethod(self) -> None:
        self.wasRun = 1


class TestCaseTest(TestCase):
    def testRunning(self) -> None:
        test: WasRun = WasRun(name="testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun


TestCaseTest(name="testRunning").run()
