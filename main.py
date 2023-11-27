from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

price_list = []



class Bot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.max_rent = 50000
        self.web_url = f"https://www.zameen.com/Rentals/Karachi-2-1.html?price_max={self.max_rent}"
        self.web_data = requests.get(url=self.web_url)
        self.web_data_text_format = self.web_data.text
        self.soup = BeautifulSoup(self.web_data_text_format, "html.parser")

    def scrap_property_prices(self):
        price = self.soup.findAll("span", "f343d9ce")
        for prices in price:
            price_list.append(prices.text)
        self.length_list = len(price_list)
        return self.length_list

    def enter_prices_to_form(self):
        form_link = self.driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLScPNZQZ9RQeuHs40tDkAURP1omF7NUiq1oaqJpwh0qgH4GQxg/viewform")
        time.sleep(1)
        for i in range(len(price_list)):
            input_price = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(1)
            input_price.send_keys(price_list[i])
            time.sleep(1)
            submit_button = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            submit_button.click()
            time.sleep(1)
            submit_another_response = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another_response.click()


bot = Bot()
bot.scrap_property_prices()
bot.enter_prices_to_form()


