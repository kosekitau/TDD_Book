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


class TestSuite:
    def __init__(self) -> None:
        self.tests: list = []

    def add(self, test: "TestCase") -> None:
        self.tests.append(test)

    def run(self, result) -> None:
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self, result) -> TestResult:
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()


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
        result = TestResult()
        test.run(result=result)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self) -> None:
        test = WasRun(name="testMethod")
        result = TestResult()
        test.run(result=result)
        assert result.summary() == "1 run, 0 failed"

    def testFailedResult(self) -> None:
        test = WasRun(name="testMethod")
        result = TestResult()
        test.run(result=result)
        # assert result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"

    def testSuite(self) -> None:
        suite = TestSuite()
        suite.add(test=WasRun(name="testMethod"))
        suite.add(test=WasRun(name="testBrokenMethod"))
        result: TestResult = TestResult()
        suite.run(result)
        assert result.summary() == "2 run, 1 failed"


suite = TestSuite()
suite.add(test=TestCaseTest(name="testTemplateMethod"))
suite.add(test=TestCaseTest(name="testResult"))
suite.add(test=TestCaseTest(name="testFailedResult"))
suite.add(test=TestCaseTest(name="testFailedResultFormatting"))
suite.add(test=TestCaseTest(name="testSuite"))
result = TestResult()
suite.run(result=result)
print(result.summary())
