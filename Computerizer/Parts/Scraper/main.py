from logging import exception
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import *
from selenium.common.exceptions import NoSuchElementException
from time import sleep, thread_time


class Scraper:
    driver = webdriver.Firefox()

    def __init__(self, name, url, oldprice, newprice):
        self.name = name
        self.url = url
        self.oldprice = oldprice
        self.newprice = newprice

#---------------------Selenium Selectors---------------------#

    # All selectors related to Amazon US
    @staticmethod
    def price_selectors_amazon():
        XPath = '/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]'
        CSSselector = 'span.a-price:nth-child(2) > span:nth-child(2) > span:nth-child(2)'
        Classname = 'twisterSwatchPrice a-size-base a-color-base'
        return [XPath, CSSselector, Classname]

    @staticmethod
    def decimal_selectors_amazon():
        XPath = '/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[1]/div[1]/span[2]/span[2]/span[3]'
        CSSselector = 'span.a-price:nth-child(2) > span:nth-child(2) > span:nth-child(3)'
        Classname = 'a-price-fraction'
        return [XPath, CSSselector, Classname]

    # All selectors related to Newegg US
    @staticmethod
    def price_selectors_newegg():
        XPath = '/html/body/div[9]/div[3]/div/div/div/div[1]/div[1]/div[3]/div[3]/ul/li[3]/strong'
        CSSselector = 'div.product-pane:nth-child(3) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > strong:nth-child(2)'
        CSSpath = 'html.show-tab-store body div#app div.page-content div.page-section div.page-section-inner div.row.is-product.has-side-right.has-side-items div.row-side div.product-buy-box div.product-pane div.product-price ul.price li.price-current strong'
        return [XPath, CSSselector, CSSpath]

    @staticmethod
    def decimal_selectors_newegg():
        XPath = '/html/body/div[9]/div[3]/div/div/div/div[1]/div[1]/div[3]/div[3]/ul/li[3]/sup'
        CSSselector = 'div.product-pane:nth-child(3) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > sup:nth-child(3)'
        CSSpath = 'html.show-tab-store body div#app div.page-content div.page-section div.page-section-inner div.row.is-product.has-side-right.has-side-items div.row-side div.product-buy-box div.product-pane div.product-price ul.price li.price-current sup'
        return [XPath, CSSselector, CSSpath]

    # All selectors related to BestBuy US
    @staticmethod
    def price_selectors_bestbuy():
        XPath = '/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/span[1]'
        CSSselector = 'div.pricing-price:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
        CSSpath = 'html body.size-l div.pl-page-content main div.container-v3 div.row.v-m-bottom-g div.col-lg-4.col-xs-5 div.row div.col-xs-12 div#pricing-price-32843407._none div.pricing-price div.pricing-price div.pricing-lib-price-19-2227-9.price-view-pb.priceView-layout-large div.pricing-price.pricing-lib-price-19-2227-9.priceView-price div div div div.priceView-hero-price.priceView-customer-price span'
        return [XPath, CSSselector, CSSpath]
#---------------------------------------------------------#

    @classmethod
    def get_price_amazon(cls, self):
        global driver
        Price_Selectors = cls.price_selectors_amazon()
        url = self.url
        try:
            sleep(3)
            driver.get(url)
            element = driver.find_element_by_class_name(Price_Selectors[2])
            price = element.get_attribute('innerHTML')
            return (price)
        except NoSuchElementException:
            sleep(2)
            try:
                element = driver.find_element_by_xpath(Price_Selectors[0])
                price = element.get_attribute('innerHTML')
                return (price)
            except NoSuchElementException:
                try:
                    element = driver.find_element_by_css_selector(
                        Price_Selectors[1])
                    price = element.get_attribute('innerHTML')
                    return (price)
                except:
                    return(f'\nNo price was found on amazon due to:\n {exception}')
        driver.quit()

    def get_price_newegg(self):
        pass

    def get_price_bestbuy(self):
        pass


def get_price(url):
    driver = webdriver.Firefox()
    driver.get(url)
    name = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
    try:
        sleep(2)
        driver.get(url)
        element = driver.find_element_by_class_name(
            'twisterSwatchPrice a-size-base a-color-base')
        price = element.get_attribute('innerHTML')
        return (f'\n{name}\nCosts:{price}\n')

    except NoSuchElementException:
        sleep(2)
        try:
            element = driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
            price = element.get_attribute('innerHTML')
            return (f'\n{name}\nCosts:{price}\n')
        except NoSuchElementException:
            print("Error finding element")
            pass

    driver.quit()


def get_sale_percentage(url):
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        sleep(2)
        driver.get(url)
        element = driver.find_element_by_class_name('a-color-price')
        percentage = element.get_attribute('innerHTML')
        return percentage

    except NoSuchElementException:
        sleep(2)
        try:
            element = driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[10]/div[2]/div/table/tbody/tr[3]/td[2]/span[1]')
            percentage = element.get_attribute('innerHTML')
            return percentage
        except NoSuchElementException:
            print("NO SALE")
            pass

    driver.quit()
