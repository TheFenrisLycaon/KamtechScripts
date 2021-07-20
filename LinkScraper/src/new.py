import os
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd


def set_opt():
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_argument('--ignore-certificate-errors-spki-list')
    opt.add_argument('--ignore-ssl-errors')
    opt.add_experimental_option(
        "excludeSwitches", ["enable-logging", 'enable-automation'])
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    return opt


Hanumangarh = '02'
Karauli = '09'
Partapgarh = '33'
Alwar= '06'
Banswara = '28'
Jodhpur = '15'


class bot:

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='/home/fenris/work/Kamtech/Scrapers/LinkScraper/src/chromedriver_1', options=set_opt())
        self.driver.get("http://cbhi.nic.in/")
        time.sleep(25)

    def getLink(self, link, city):
        for i in range(2014, 2020):
            self.homepage = self.driver.get(link)
            self.driver.find_element_by_xpath(
                '//*[@id="txtyear"]').send_keys(i)
            time.sleep(1)
            Select(self.driver.find_element_by_xpath(
                '//*[@id="drop_month"]')).select_by_value('12')
            time.sleep(1)
            Select(self.driver.find_element_by_xpath(
                '//*[@id="drop_level"]')).select_by_value('02')
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="RadioButton2"]').click()
            time.sleep(1)
            Select(self.driver.find_element_by_xpath(
                '//*[@id="DropDownList1"]')).select_by_value('02')
            time.sleep(1)
            Select(self.driver.find_element_by_xpath(
                '//*[@id="drop_state"]')).select_by_value('08')
            time.sleep(1)
            Select(self.driver.find_element_by_xpath(
                '//*[@id="drop_dist"]')).select_by_value(city)
            time.sleep(1)
            for j in ['rep40', 'rep42']:
                form = Select(self.driver.find_element_by_xpath(
                         '//*[@id="drop_rep"]'))
                form.select_by_value(j)
                self.driver.find_element_by_xpath('//*[@id="Button1"]').click()
                time.sleep(1)
                Select(self.driver.find_element_by_xpath(
                    '//*[@id="ReportViewer1__ctl1__ctl5__ctl0"]')).select_by_value('CSV')
                self.driver.find_element_by_xpath(
                    '//*[@id="ReportViewer1__ctl1__ctl5__ctl1"]').click()
                self.driver.back()
                self.driver.find_element_by_tag_name(
                    'body').send_keys(Keys.CONTROL + Keys.TAB)
                time.sleep(1)
            

    def saveState(self):
        self.df.columns = self.df.iloc[0, :]
        self.df.drop(index=0, inplace=True)
        self.df.to_csv(f'./sheet{self.index}.csv')

    def bye(self):
        driver = self.driver
        driver.quit()


if __name__ == "__main__":
    opt = set_opt()
    x = bot()
    cities = [Alwar, Banswara, Jodhpur]

    for city in cities:
        x.getLink('http://cbhi.nic.in/outReport.aspx', city)
    x.bye()


# The districts are -
# 1. Alwar
# 2. Banswara
# 3. Jodhpur

# //*[@id="DropDst"]    state
# //*[@id="DropDdt"]    user
# //*[@id="TextBox1"]   pass
# //*[@id="Button1"]    submit
#  //*[@id="txtyear"]   year
