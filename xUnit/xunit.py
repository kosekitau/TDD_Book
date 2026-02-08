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
    def setUp(self) -> None:
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp"

    def testMethod(self) -> None:
        self.wasRun = 1


class TestCaseTest(TestCase):
    """ここがテストを先に書く場になる"""

    def setUp(self) -> None:
        """fixture"""
        self.test = WasRun(name="testMethod")

    def testRunning(self) -> None:
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self) -> None:
        self.test.run()
        assert self.test.log == "setUp"


TestCaseTest(name="testRunning").run()
TestCaseTest(name="testSetUp").run()
