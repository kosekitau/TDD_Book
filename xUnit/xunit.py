class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def setUp(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.wasRun = None
        super().__init__(name=name)

    def testMethod(self) -> None:
        self.wasRun = 1

    def setUp(self) -> None:
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    """ここがテストを先に書く場になる"""

    def testRunning(self) -> None:
        test: WasRun = WasRun(name="testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun

    def testSetUp(self) -> None:
        test: WasRun = WasRun(name="testMethod")
        test.run()
        assert test.wasSetUp


TestCaseTest(name="testRunning").run()
TestCaseTest(name="testSetUp").run()
