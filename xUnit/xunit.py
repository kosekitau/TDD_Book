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
        self.log: str = "setUp "

    def testMethod(self) -> None:
        self.log = self.log + "testMethod "


class TestCaseTest(TestCase):
    """ここがテストを先に書く場になる"""

    def testTemplateMethod(self) -> None:
        test = WasRun(name="testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown"


TestCaseTest(name="testTemplateMethod").run()
