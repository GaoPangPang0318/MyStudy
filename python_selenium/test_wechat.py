"""
使用cookie登陆企业微信，完成导入联系人，加上断言验证
"""
import shelve

from selenium import webdriver


class TestWechat:
    def setup(self):
        #复用浏览器
        #定义ChromeOptions
        chrome_arg=webdriver.ChromeOptions()
        #添加debugger address  端口必须与浏览器开启的一致    浏览器调佣方法：cmd中执行：chrome --remote-debugging-port=9222
        chrome_arg.debugger_address='127.0.0.1:9222'
        #创建driver
        self.driver=webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()

    def test_wechat(self):
        #获取cookie：1复用浏览器，打开网页并登陆 ，然后请求url 获取cookies并打印
        #self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #cookies=self.driver.get_cookies()
        #print(cookies)

        #将cookie持续化存储，存入shelve中  shelve相当于一个小型的数据库
        db=shelve.open('./mydatabase/cookies')
        #db['cookie']=cookies  #存入shelve中的操作
        #db.close()

        cookies=db['cookie']
        for cookie in cookies:
            if 'exoiry' in cookie.keys():
                cookie.pop("expiry")
            #将cookie传给driver
            self.driver.add_cookie(cookie)
        #请求企业微信登陆url
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        #元素定位1：定位企业微信“导入通讯录”
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        #元素定位2：定位企业微信“上传文件”
        self.driver.find_element_by_id('js_upload_file_input').send_keys("C:/Users/Gao/Desktop/testdata.xlsx")
        #获取上传文件的文件名并进行断言
        file_name=self.driver.find_element_by_id('upload_file_name').text
        assert "testdata.xlsx"==file_name

#ht