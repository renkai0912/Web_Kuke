from base.basefile import Base

class Address:
    bas = Base()
    def address(self):
        self.bas.click_xpath('/html/body/header/div[1]/div[2]/ul/li[1]/a/span[1]/img')
        self.bas.page_scroll(300)
        self.bas.click_xpath('//span[text()="我的地址"]')
        self.bas.click_xpath('//img[@src="/static/home/img/ucenter/sendoutgoods/icon-add.png"]')   #点击新增地址
        self.bas.click_xpath('//input[@placeholder="请选择省/市"]')
        self.bas.click_xpath('//span[text()="河南省"]')
        self.bas.click_xpath('//input[@placeholder="市"]')
        self.bas.click_xpath('//span[text()="郑州市"]')
        self.bas.click_xpath('//input[@placeholder="区/县"]')
        self.bas.click_xpath('//span[text()="金水区"]')
        self.bas.click_xpath('//textarea[@class="el-textarea__inner"]') #详细地址
        self.bas.enter_text('//textarea[@class="el-textarea__inner"]','国奥商务')
        self.bas.click_xpath('//input[@maxlength="10"]')  #收货人
        self.bas.enter_text('//input[@maxlength="10"]','浪浪')
        self.bas.click_xpath('//*[@id="address-app"]/div[2]/div/p/form/div[3]/div/div[2]/div/div/div/input') #手机号
        self.bas.enter_text('//*[@id="address-app"]/div[2]/div/p/form/div[3]/div/div[2]/div/div/div/input','17836988418')
        self.bas.click_xpath('//div[text()="保存"]')

    def delete_ads(self):
        self.bas.page_scroll(300)
        self.bas.click_xpath('//span[text()="我的地址"]')
        self.bas.click_xpath('//div[@class="del operation-btn"]')  #删除地址
        self.bas.click_xpath('//div[text()="确定"]')


