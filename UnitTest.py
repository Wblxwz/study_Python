import unittest
from HtmlTestRunner import HTMLTestRunner
def setUpModule():
    print(1111)

@unittest.skipIf(1 > 2,"False")
class Test(unittest.TestCase):
    """Test"""
    def setUp(self) -> None:
        print("before test")
    def test(self):
        """test"""
        self.assertEqual(1,2)
    def test2(self):
        """test2"""
        self.assertDictEqual({"a":1},{"a":1})
    @unittest.skipUnless(True,"True")
    def test3(self):
        """test3"""
        self.num1 = input("num1...")
        self.num2 = input("num2...")
        self.assertEqual(self.num1,self.num2,"{num1} and {num2} not equal".format(num1 = self.num1,num2 = self.num2))
    @unittest.expectedFailure
    def fail(self):
        pass
    def tearDown(self) -> None:
        print("after test")
    @classmethod
    def tearDownClass(cls) -> None:
        print(6666)

if __name__ == "__main__":
    #with open("./report/report.txt","w") as file:
        suite = unittest.TestSuite()
        #全部测试
        #suite = unittest.TestLoader().loadTestsFromTestCase(Test)
        suite.addTests([Test("test2"),Test("test3"),Test("fail")])
        #unittest.main()
        #verbosity:0（静默模式）、1（默认模式，显示简单的测试结果）、2（详细模式，显示每个测试用例的详细信息）。
        #runner = unittest.TextTestRunner(stream=file,verbosity=2)
        runner = HTMLTestRunner(output="./report",report_title="用例执行情况",report_name="test_report")
        runner.run(suite)