# -*- coding: utf-8 -*-

'''
cnblog的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class Test_Login(unittest.TestCase):

    # before each test
    def setUp(self):
        """Open Chrome """
        # opt = webdriver.ChromeOptions()  # 创建chrome参数对象
        # opt.set_headless()  # 把chrome设置成无头模式，不论windows还是linux都可以，自动适配对应参数
        # self.driver = webdriver.Chrome(options=opt, executable_path='./chromedriver_72')#不制定options选项则是普通有头浏览器
        self.driver = webdriver.Chrome(executable_path='../chromedriver_72')
        self.driver.implicitly_wait(2) # 隐性等待, essential

    def login(self, username, password):
        """login basic case"""
        # Open the Url
        self.driver.get("https://account.xiaomi.com/pass/serviceLogin") #小米登录页面

        # username input textbox
        user_inputbox = self.driver.find_element(By.XPATH,"//input[@class='item_account' and @name='user'and @id='username']")
        user_inputbox.clear()
        user_inputbox.send_keys(username)

        # search for password input textbox
        pwd_inputbox = self.driver.find_element(By.XPATH,"//input[@class='item_account' and @name='password' and @id='pwd']")
        pwd_inputbox.clear()
        pwd_inputbox.send_keys(password)

        # search for submit button
        submit_box = self.driver.find_element(By.XPATH, "//input[@id='login-button' and @type='submit']")
        submit_box.click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('kemi_xxx', 'kemi_xxxx')  # 正确用户名和密码
        sleep(3)
        link = self.driver.find_element_by_id('lnk_current_user')
        self.assertTrue('菜鸟可米' in link.text)  # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
        self.driver.get_screenshot_as_file("./login_success.jpg")  # 截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('kemi_xxx', 'kemi')  # 正确用户名，错误密码
        sleep(2)
        error_message = self.driver.find_element_by_id('tip_btn').text
        self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        self.driver.get_screenshot_as_file("./login_pwd_error.jpg")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('kemi_xxx', '')  # 密码为空
        error_message = self.dr.find_element_by_id('tip_input2').text
        self.assertEqual(error_message, '请输入密码')  # 用assertEqual(a,b)方法来断言  a == b  '请输入密码'等于error_message
        self.dr.get_screenshot_as_file("./login_pwd_null.jpg")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('kemixing', 'kemi_xxx')  # 密码正确，用户名错误
        sleep(2)
        error_message = self.dr.find_element_by_id('tip_btn').text
        self.assertIn('该用户不存在', error_message)  # 用assertIn(a,b)方法来断言 a in b
        self.dr.get_screenshot_as_file("./login_user_error.jpg")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login('', 'kemi_xxx')  # 用户名为空，密码正确
        error_message = self.dr.find_element_by_id('tip_input1').text
        self.assertEqual(error_message, '请输入登录用户名')  # 用assertEqual(a,b)方法来断言  a == b
        self.dr.get_screenshot_as_file("./login_user_null.jpg")

    # after each test
    def tearDown(self):
        """Close Chrome """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 gives a detailed report
