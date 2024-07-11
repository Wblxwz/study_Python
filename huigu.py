import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from unittest import TestCase
import unittest
from HtmlTestRunner import HTMLTestRunner

def waitIframe(driver,id):
    try:
        driver.find_element(By.ID,id)
    except Exception as e:
        return False
    return True

def logIn(webDriver):

    if webDriver == "Edge":
        driver = webdriver.Edge()

        #隐式等待，每当一个元素未定位时即等待一段时间
        #driver.implicitly_wait(5)
        driver.get("https://www.douyu.com")
        driver.maximize_window()

        actionChains = ActionChains(driver)
        hover = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/div[3]/div[7]/div/div")))
        actionChains.move_to_element(hover).perform()
        logIn = driver.find_element(By.XPATH,"/html/body/header/div/div/div[1]/div[3]/div[7]/div/div/div/div/div/div[2]/a[1]")
        logIn.click()

        WebDriverWait(driver,5).until(lambda driver:waitIframe(driver,"login-passport-frame"))
        driver.switch_to.frame("login-passport-frame")
        logInByPwd = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div[1]/div[2]")))
        ActionChains(driver).click(logInByPwd).perform()

        niCheng = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/div[1]/span[2]")
        niCheng.click()

        nc = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/form/div[2]/div/input")
        nc.send_keys("111111")
        pwd = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/form/div[3]/input[1]")
        pwd.send_keys("111111")

        logInBtn = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/form/div[6]/input")
        ActionChains(driver).click(logInBtn).perform()

        time.sleep(300)
        myFollow = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/div[3]/div[3]")))
        ActionChains(driver).move_to_element(myFollow).perform()

        time.sleep(300)

        driver.quit()

class TestClass(TestCase):
    """setUp/tearDown在每个测试前后都会执行
       setUpClass/tearDownClass在整个测试类前后执行
    """
    @classmethod
    def setUpClass(cls) -> None:
        print("start class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("end class")
    def setUp(self) -> None:
        print("start unittest...")
    def testCase1(self):
        """ceShi 1=1"""
        self.assertEqual(1,1,"equal")
    def testCase2(self):
        """ceShi 2!=1"""
        self.assertNotEqual(2,1,"equal")
    def tearDown(self) -> None:
        print("end unittest...")

if __name__ == "__main__":
    #logIn("Edge")
    t = TestClass()
    suite = unittest.TestSuite()
    suite.addTests([TestClass("testCase1"),TestClass("testCase2")])
    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(report_title="huiGUTest")
    runner.run(suite)
    #unittest.main()