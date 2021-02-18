"""
 企业微信通讯录添加联系人操作

"""
#from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestWecomInsertMenber:
    def setup(self):
        #设置初始化参数
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True  # 首次启动的时候，不停止APP，方便进行调试
        desired_caps['skipDeviceInitialization'] = True  # 跳过安装，权限设置等操作

        # 创建driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wecom_clockin(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        #self.driver.find_element(MobileBy.XPATH,'//*[@text="完整输入"]').click()

        xpath_base='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout'
        #姓名
        el_name=self.driver.find_element(MobileBy.XPATH,xpath_base+'/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText')
        el_name.send_keys("高大胖")

        #账号
        el_account=self.driver.find_element(MobileBy.XPATH,xpath_base+'/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.EditText')
        el_account.send_keys("gdp123")

        #别名
        el_aname=self.driver.find_element(MobileBy.XPATH,xpath_base+'/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.EditText')
        el_aname.send_keys('高小胖')

        #性别
        el_sex=self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]')
        el_sex.click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()

        #手机
        el_phone=self.driver.find_element(MobileBy.XPATH,'//*[@text="手机号"]')
        el_phone.send_keys('18360000000')

        #座机
        el_call=self.driver.find_element(MobileBy.XPATH,xpath_base + '/android.widget.RelativeLayout[6]/android.widget.RelativeLayout/android.widget.EditText')
        el_call.send_keys('025-85600000')

        #邮箱
        el_mail=self.driver.find_element(MobileBy.XPATH,xpath_base + '/android.widget.RelativeLayout[7]/android.widget.RelativeLayout/android.widget.EditText')
        el_mail.send_keys("710000000@qq.com")

        #地址
        el_address=self.driver.find_element(MobileBy.XPATH,xpath_base + '/android.widget.RelativeLayout[8]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
        el_address.click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"请输入公司地址")]').send_keys("测试大楼")
        self.driver.find_element(MobileBy.XPATH,'//*[@text="确定"]').click()

        #职务
        el_position = self.driver.find_element(MobileBy.XPATH,xpath_base + '/android.widget.RelativeLayout[9]/android.widget.RelativeLayout/android.widget.EditText')
        el_position.send_keys("测试")

        #保存
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()

        #断言
        assert "添加成功"==self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text

        #sleep(2)
        #print(self.driver.page_source)  #打印出page_sourcce 才能查看到toast相关信息，然后使用xpaath定位


