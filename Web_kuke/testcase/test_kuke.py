from page.login import Login
from page.address import Address
from page.shopping import Shop
from base.basefile import Base
from base.read_csv import Read_csv
import pytest


class Test_example():
    bas=Base()
    lg = Login()
    ads = Address()
    sp=Shop()
    #打开网站并关闭弹框
    def test_open(self):
        self.bas.open_website('https://www.kuke99.com/')
        self.bas.explicit_wait(20,"//div[@class='close abs']")
        self.bas.iframe('//*[@id="YSF-IFRAME-LAYER"]')
        self.bas.explicit_wait(20, '//div[@data-action="hideIframe"]')
        self.bas.iframe_out()
    #登录
    @pytest.mark.parametrize("username,password", Read_csv.read_user())
    def test_login(self,username,password):
        self.lg.login(username,password)
    #添加地址
    def test_address(self):
        self.ads.address()
    #购物、创建订单
    def test_shop(self):
        self.sp.shop()
        self.sp.order()
    #删除地址并关闭浏览器
    def test_deleteads(self):
        self.ads.delete_ads()
        self.bas.close()





