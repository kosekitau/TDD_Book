class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self) -> None:
        self.runCount += 1

    def testFailed(self) -> None:
        self.errorCount += 1

    def summary(self) -> str:
        return f"{self.runCount} run, {self.errorCount} failed"


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self) -> TestResult:
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result


class WasRun(TestCase):
    def setUp(self) -> None:
        self.log: str = "setUp "

    def testMethod(self) -> None:
        self.log = self.log + "testMethod "

    def testBrokenMethod(self) -> None:
        raise Exception

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
        result: TestResult = test.run()
        assert result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        test = WasRun(name="testMethod")
        result: TestResult = test.run()
        # assert result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"


TestCaseTest(name="testTemplateMethod").run()
TestCaseTest(name="testResult").run()
TestCaseTest(name="testFailedResult").run()
TestCaseTest(name="testFailedResultFormatting").run()
