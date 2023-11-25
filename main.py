from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

price_list = []
link_list = []
address = []


class Bot:
    def __init__(self):
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(options=self.chrome_options)
        self.web_url = "https://www.zameen.com/Rentals/Karachi-2-1.html?price_max=50000"
        self.web_data = requests.get(url=self.web_url)
        self.web_data_text_format = self.web_data.text
        self.soup = BeautifulSoup(self.web_data_text_format, "html.parser")

    def scrap_property_prices(self):
        price = self.soup.findAll("span", class_="f343d9ce")
        for prices in price:
            print(prices.text)


d = Bot()
d.scrap_property_prices()
