from logging import exception
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import *
from selenium.common.exceptions import NoSuchElementException
from time import sleep, thread_time


class Scraper:

    def __init__(self, name, url):
        self.name = name
        self.url = url

#---------------------Selenium Selectors---------------------#

#---------------------------------------------------------#

# The get_price functions are built on two parts:
#- The first part gets the whole number price on the left side of the decimal
#- The second part gets the fraction on the right side of the decimal
# It then returns a float of both numbers in the form (56.89 for instance)

# Currently supports 3 platforms: AMAZON, NEWEGG, BESTBUY.
    """ def get_price_amazon(cls, self):
        driver = webdriver.Firefox()
        url = self.url
        driver.get(url)
        sleep(5)
        try:
            element = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[1]/div[1]/span[2]/span[2]/span[2]')
            price = element.get_attribute('innerText')
        except NoSuchElementException:
            try:
                element = driver.find_element('css selector', 'span.a-price:nth-child(2) > span:nth-child(2) > span:nth-child(2)')
                price = element.get_attribute('innerHTML')
            except:
                return(f'\nNo price was found on amazon due to:\n @@@@@{exception}\n@@@@@')

        try:
            sleep(3)
            element = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[1]/div[1]/span[2]/span[2]/span[3]')
            decimal = element.get_attribute('innerHTML')
        except NoSuchElementException:
            try:
                sleep(3)
                element = driver.find_element('css selector', 'span.a-price:nth-child(2) > span:nth-child(2) > span:nth-child(3)')
                decimal = element.get_attribute('innerHTML')
            except:
                print(f'{self.name} may be out of stock')
                return(f'\nError finding decimal of price due to:\n @@@@@{exception}\n@@@@@')
            finally:
                driver.close()
                driver.quit()
                return(float(f'{price}.{decimal}'))
             """

    def get_price_newegg(cls, self):
        driver = webdriver.Firefox()
        url = self.url
        driver.get(url)
        try:
            element = driver.find_element('xpath', '/html/body/div[9]/div[3]/div/div/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]/strong')
            price = element.get_attribute('innerHTML')
        except NoSuchElementException:
            sleep(2)
            try:
                element = driver.find_element('css selector', 'ul.price:nth-child(2) > li:nth-child(3) > strong:nth-child(2)')
                price = element.get_attribute('innerHTML')
            except:
                print(f'{self.name} may be out of stock')
                print(f'\nNo price was found on amazon due to: {exception}')

        try:
            sleep(3)
            element = driver.find_element('xpath', '/html/body/div[9]/div[3]/div/div/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]/sup')
            decimal = element.get_attribute('innerHTML')
        except NoSuchElementException:
            try:
                sleep(3)
                element = driver.find_element('css selector', 'ul.price:nth-child(2) > li:nth-child(3) > sup:nth-child(3)')
                decimal = element.get_attribute('innerHTML')
            except:
                print(f'\nError finding decimal of price due to: {exception}')

    
    
        return(float(f"{price}.{decimal}"))

    def get_price_bestbuy(cls, self):
        driver = webdriver.Firefox()
        url = self.url
        driver.get(url)
        driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]').click()
        sleep(5)
        try:
            element = driver.find_element('xpath', '/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/span[1]')
            price = element.get_attribute('innerHTML')
        except NoSuchElementException:
            sleep(2)
            try:
                element = driver.find_element('css selector', 'div.pricing-price:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
                price = element.get_attribute('innerHTML')
            except:
                print(f'{self.name} may be out of stock')
                print(f'\nNo price was found on bestbuy due to: {exception}')

        price = price.lstrip('$')
        return(float(f"{price}"))


if __name__ == "__main__":
    Scraper()
