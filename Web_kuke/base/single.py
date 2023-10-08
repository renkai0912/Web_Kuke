from airtest_selenium import WebChrome
from airtest_selenium.proxy import WebFirefox


class Singal:
    _instance=None

    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class CommDriver(Singal):
    driver=None

    def get_driver(self,browser_type):
        if self.driver is None:
            if browser_type == "chrome":
                self.driver = WebChrome()
            elif browser_type == "firefox":
                self.driver = WebFirefox()
            else:
                raise Exception(f"{browser_type}暂不支持")
            self.driver.maximize_window()
            self.driver.implicitly_wait(20)
        return self.driver