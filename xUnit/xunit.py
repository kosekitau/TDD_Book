class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    def setUp(self) -> None:
        self.log: str = "setUp "

    def testMethod(self) -> None:
        self.log = self.log + "testMethod "

    def tearDown(self) -> None:
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):
    """ここがテストを先に書く場になる"""

    def testTemplateMethod(self) -> None:
        test = WasRun(name="testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        test = WasRun(name="testMethod")
        result: str = test.run()
        assert result.summary() == "1 run, 0 failed"


TestCaseTest(name="testTemplateMethod").run()
TestCaseTest(name="testResult").run()
