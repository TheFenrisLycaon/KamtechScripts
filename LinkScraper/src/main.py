import os
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
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


class bot:

    def __init__(self, link):
        if os.path.isdir('Data'):
            pass
        else:
            os.makedirs('Data')

        self.driver = webdriver.Chrome(
            executable_path="/home/fenris/work/Kamtech/Scrapers/LinkScraper/src/chromedriver_1", options=set_opt())
        self.driver.get(link)

    def findCity(self, cityIndex):
        dd = Select(self.driver.find_element_by_id(
            'ContentPlaceHolder1_Drpdistrictcode'))
        dd.select_by_index(cityIndex)
        try:
            size = Select(self.driver.find_element_by_id(
                'ContentPlaceHolder1_DrpPagesize'))
            size.select_by_value('30000')
        except:
            pass
        self.driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_btnSubmit"]').click()
        self.index = cityIndex
        time.sleep(1)

    def getTable(self, number):
        soup = BeautifulSoup(self.driver.page_source, features="lxml")
        tables = soup.find_all(
            'table', {"id": ["ContentPlaceHolder1_rptMedicalType"]})[0]
        tableData = [[cell.text for cell in row.find_all(["th", "td"])]
                     for row in tables.find_all("tr")]
        # if number == 1:
        #     self.df = pd.DataFrame(tableData)
        self.df = pd.DataFrame(tableData)
        # else:
        #     temp = pd.DataFrame(tableData)
        #     self.df = pd.concat([self.df, temp])
        try:
            self.driver.find_element_by_xpath(
                f'//*[@id = "ContentPlaceHolder1_rptMedicalType"]/tbody/tr[33]/td/table/tbody/tr/td[{number}]/a').click()
        except:
            pass
        time.sleep(1)

    def loadPage(self):
        body = self.driver.find_element_by_xpath('/html/body')
        body.click()
        for _ in range(10):
            body.send_keys(Keys.END)

    def saveState(self):
        self.df.columns = self.df.iloc[0, :]
        self.df.drop(index=0, inplace=True)
        self.df.to_csv(f'./sheet{self.index}.csv', encoding='utf-8')

    def bye(self):
        driver = self.driver
        driver.quit()


if __name__ == "__main__":
    opt = set_opt()
    link = sys.argv[1]
    x = bot(link)
    cities = [3]
    # cities = [3]
    for i in cities:
        x.findCity(i)
        # for j in range(1, 11):
        x.loadPage()
        x.getTable(0)
        x.saveState()
        print(i, "Done")
        k = input("Press any key to exit...")
    x.bye()
