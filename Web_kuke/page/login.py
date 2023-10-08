from base.basefile import Base
from time import sleep




class Login:
    bas=Base()
    def login(self,username,password):
        self.bas.click_xpath('//span[text()="登录"]')
        self.bas.click_xpath('//span[text()="密码登录"]')
        self.bas.click_xpath('//*[@id="tel-input-password"]')
        self.bas.enter_text('//*[@id="tel-input-password"]',username)
        self.bas.click_xpath('//*[@id="password"]')
        self.bas.enter_text('//*[@id="password"]', password)
        self.bas.click_xpath('//button[@class="login-btn login-pw-btn"]')


