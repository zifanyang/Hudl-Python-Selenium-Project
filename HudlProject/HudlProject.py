from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep
path="C:\chromedriver.exe"
url="http://www.hudl.com/login"
#username:nathanyang18@outlook.com
#password:test1234

class TestLogin(unittest.TestCase):
    #Open url
    def setUp(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(1)

    def test_Login(self):#Login successful
        un = "nathanyang18@outlook.com"
        pw = "test1234"
        driver=self.driver
        username=self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(un)
        password=self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(pw)
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        a=driver.current_url
        self.assertEqual(a,'https://www.hudl.com/home',msg='Login successfully')

    def test_LoginWithTabAndEnter(self):#Tab & Enter
        un = "nathanyang18@outlook.com"
        pw = "test1234"
        driver=self.driver
        self.driver.find_element_by_name('username').send_keys(un + Keys.TAB + pw + Keys.ENTER)
        sleep(3)
        a=driver.current_url
        self.assertEqual(a,'https://www.hudl.com/home',msg='Login successfully')

    def test_LoginWithWrongPw(self):#Wrong password
        un = "nathanyang18@outlook.com"
        pw = "wrongpassword"
        driver = self.driver
        username = self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(un)
        password = self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(pw)
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        self.assertIn("We didn't recognize that email and/or password.",self.driver.page_source)

    def test_LoginWithWrongUn(self):#Wrong username
        un = "wrongusername@outlook.com"
        pw = "test1234"
        driver = self.driver
        username = self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(un)
        password = self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(pw)
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        self.assertIn("We didn't recognize that email and/or password.", self.driver.page_source)

    def test_LoginWithWrongUnAndPw(self):#Wrong username and wrong passowrd
        un = "wrongusername@outlook.com"
        pw = "wrongpassword"
        driver = self.driver
        username = self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(un)
        password = self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(pw)
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        self.assertIn("We didn't recognize that email and/or password.", self.driver.page_source)

    def test_LoginWithNoUn(self):#No username
        un = "nathanyang18@outlook.com"
        pw = "test1234"
        driver = self.driver
        username = self.driver.find_element_by_name('username')
        username.clear()
        password = self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(pw)
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        self.assertIn("We didn't recognize that email and/or password.", self.driver.page_source)

    def test_LoginWithNoPw(self):#No password
        un = "nathanyang18@outlook.com"
        pw = "test1234"
        driver = self.driver
        username = self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(un)
        password = self.driver.find_element_by_name('password')
        password.clear()
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        self.assertIn("We didn't recognize that email and/or password.", self.driver.page_source)

    def test_LoginWithNoUnAndPw(self):
        un = "nathanyang18@outlook.com"
        pw = "test1234"
        driver = self.driver
        username = self.driver.find_element_by_name('username')
        username.clear()
        password = self.driver.find_element_by_name('password')
        password.clear()
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        self.assertIn("We didn't recognize that email and/or password.", self.driver.page_source)

    def test_RememberMe(self):#Remember me
        un = "nathanyang18@outlook.com"
        pw = "test1234"
        driver=self.driver
        username=self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(un)
        password=self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(pw)
        self.driver.find_element_by_class_name('form__label--custom').click()
        self.driver.find_element_by_id('logIn').click()
        sleep(3)
        a=driver.current_url
        self.assertEqual(a,'https://www.hudl.com/home',msg='Login successfully')

    def test_NeedHelp(self):#Need help
        driver = self.driver
        self.driver.find_element_by_id("forgot-password-link").click()
        sleep(3)
        self.assertIn("Login Help", self.driver.page_source)


    def tearDown(self):
        self.driver.quit()

if __name__ =="__main":
    unittest.main()
