from python_selenium_po.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.indexpage = IndexPage()

    def test_addmember(self):
        username="测试001"
        englishname="test001"
        account="test001"
        phonenum="18362000000"
        telnum="85600000"
        email="test001@163.com"
        address="测试省测试市测试区测试小区测试栋测试楼测试实"
        title="测试工程师"
        page = self.indexpage.goto_addmembers()
        page.add_members(username,englishname,account,phonenum,telnum,email,address,title)

    def teardown(self):
        self.indexpage.quit_driver()
