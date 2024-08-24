import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time

class BaseConstants:



      base_url = "https://shop.polymer-project.org/"
      check_out_url = "https://shop.polymer-project.org/checkout"


      # def get_driver(self,browser):
      #     if browser == "chrome" or browser == "Chrome" or browser == "CHROME":
      #        driver = webdriver.Chrome()
      #     elif browser == "firefox" or browser == "Firefox" or browser == "FIREFOX":
      #         driver = webdriver.Firefox()
      #     else:
      #         driver = webdriver.Edge()
      #
      #     driver.maximize_window()
      #     yield driver
      #     driver.quit()




      def click_cart(self):
          self.get_cart().click()

      # def dr_object(self,request):
      #     driver = self.get_driver(browser="chrome")
      #     dr = driver.__next__()
      #     dr.get(self.base_url)
      #     time.sleep(5)
      #     return dr




