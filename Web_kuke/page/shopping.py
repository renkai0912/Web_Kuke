from base.basefile import Base
import pyautogui
from time import sleep

class Shop:
    bas=Base()
    def shop(self):
        self.bas.click_xpath("/html/body/header/div[2]/div[1]/a/img") #回到首页
        self.bas.PageControl(1)
        self.bas.page_scroll(1000)
        self.bas.explicit_wait(15, '//img[@alt="2024年河南专升本钻石班《公共英语+管理学》"]')
        self.bas.PageControl(2)
        self.bas.iframe('//*[@id="YSF-IFRAME-LAYER"]')
        self.bas.explicit_wait(15,'//div[@data-action="hideIframe"]')
        self.bas.iframe_out()
        self.bas.click_xpath('/html/body/section/div[2]/div[2]/div[2]')  #购买
        self.bas.PageControl(3)
        self.bas.page_scroll(300)
        self.bas.iframe('//*[@id="YSF-IFRAME-LAYER"]')
        self.bas.explicit_wait(15,'//div[@data-action="hideIframe"]')
        self.bas.iframe_out()
        self.bas.click_xpath('//i[@data-btntype="policy"]')  #同意协议
        pyautogui.scroll(-800)
        self.bas.click_xpath('//span[@class="dialog_sale_footer_btn confirm_btn is_confirm"]') #浏览完同意
        self.bas.click_xpath('//button[@onclick="subs()"]') #提交订单

    def order(self):
        self.bas.click_xpath("//span[text()='浪浪']")
        self.bas.click_xpath("//span[text()='全部订单']")
        self.bas.iframe('//*[@id="YSF-IFRAME-LAYER"]')
        self.bas.explicit_wait(10,'//div[@data-action="hideIframe"]')
        self.bas.iframe_out()
        self.bas.click_xpath("//span[text()='取消订单']")
        self.bas.click_xpath('//p[text()="多买/买错/更换"]')
        self.bas.click_xpath('/html/body/section/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/button[1]')

