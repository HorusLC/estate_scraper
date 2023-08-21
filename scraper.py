import requests
from bs4 import BeautifulSoup
from requests import Session
import configs
from dates_helper import DateHelper


class Scraper:
    """
    The Scraper class, that will do the hard work of getting the data.
    """

    def __init__(self, url: str):
        self._offer_src: BeautifulSoup = None
        self.initial_url = url

    def scrape_page(self):
        page = requests.get(configs.URL)
        results_page = BeautifulSoup(page.text, 'html.parser')
        offer_cl = 'lnk1'
        date_manager = DateHelper()
        offers = results_page.find_all('a', class_=offer_cl)
        for offer_item in offers:
            offer_page_url = requests.get('https:' + offer_item['href'])
            print(offer_page_url.encoding)
            offer_page_url.encoding = 'utf-8'
            print(offer_page_url.text)
            self._offer_src = BeautifulSoup(offer_page_url.content, 'html.parser')
            self._scrape_offer()
            # date_elem_parent = self.offer_src.find('div', class_='adPrice')
            # date_elem = date_elem_parent.findChild('div', class_='info')
            # print(date_elem.text)
            # print(date_manager.parse_date(date_elem.text))
            break #temp so we dont overload the server with requests while testing
        # General idea:
        # 1. Get the offers from the first page
        # 2. Read the Last visited date
        # 3. Loop through the offers while offer's date is newer than the last visited date.

        # Challenges:
        # compare the dates in textual Bulgarian - partialy implemented
        # navigate to next page
    def _scrape_offer(self):
        # scrape the date published
        if self._offer_src is not None:
            date_manager = DateHelper()
            try:
                self._scrape_date_data(date_manager)
                # scrape the price
                price, currency = self._scrape_price_offer()
                # scrape the adParams- size and level-info
                size, level_info = self._scrape_size_lvl()
            except AttributeError as ae:
                print(ae)

    def _scrape_date_data(self, date_manager):
        date_elem_parent = self._offer_src.find('div', class_='adPrice')
        date_elem = date_elem_parent.findChild('div', class_='info')
        print(date_manager.parse_date(date_elem.text))

    def _scrape_size_lvl(self):
        offer_parameters = self._offer_src.find('div', class_='adParams')
        children = offer_parameters.findChildren('div')
        size_str = children[0].text
        size = int(size_str.split()[1])
        level_info_str = children[1].text
        print(size_str)
        print(size)
        print(level_info_str)
        return size, level_info_str

    def _scrape_price_offer(self):

        price_cur_str = self._offer_src.find('div', id='cena').text.split()
        currency = price_cur_str[-1]
        price_cur_str.pop()
        price = int(''.join(price_cur_str))
       # print(price)
       # print(currency)
        return price, currency
