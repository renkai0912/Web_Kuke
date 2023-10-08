from airtest_selenium import WebChrome
from airtest.core.api import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class Base:
    driver = WebChrome()
    driver.maximize_window()
    def open_website(self,path):  #打开网站
        self.driver.get(path)

    def click_xpath(self,xpath):  #通过xpath点击内容
        self.driver.find_element_by_xpath(xpath).click()

    def click_class(self,id):     #通过id点击内容
        self.driver.find_element_by_id(id).click()

    def enter_text(self,xpath,text):   #写入文本
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def page_scroll(self, px):     #页面滚动
        self.driver.execute_script(f"document.documentElement.scrollTop={px}")

    def select(self,xpath,subscript):   #选择<select>标签的内容 subscript：下标
        Select(self.driver.find_element_by_xpath(xpath)).select_by_index(subscript)

    def explicit_wait(self,time,xpath):   #显示等待
      ele=WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
      ele.click()

    def iframe(self,xpath):  #切入iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))

    def iframe_out(self):   #退出iframe返回上一级
        self.driver.switch_to.parent_frame()

    def PageControl(self,x):  #页面句柄跳转
        self.driver.switch_to.window(self.driver.window_handles[x])

    def close(self):
        self.driver.quit()


