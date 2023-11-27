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
        self.max_rent = 50000
        self.web_url = f"https://www.zameen.com/Rentals/Karachi-2-1.html?price_max={self.max_rent}"
        self.web_data = requests.get(url=self.web_url)
        self.web_data_text_format = self.web_data.text
        self.soup = BeautifulSoup(self.web_data_text_format, "html.parser")

    def scrap_property_prices(self):
        price = self.soup.findAll("span", "f343d9ce")
        for prices in price:
            price_list.append(prices.text)

    def scrap_property_links(self):
        elements_with_class = self.soup.find_all(class_="_357a9937")

        # Iterate through each element and find <a> elements within it
        for element in elements_with_class:
            links = element.find_all("a")
            for link in links:
                link_list.append(link['href'])

        return link_list



d = Bot()
d.scrap_property_prices()
d.scrap_property_links()

print(price_list)
print(link_list)

