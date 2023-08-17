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
        self.initial_url = url

    def scrape_offers(self):
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
            offer_page_soup = BeautifulSoup(offer_page_url.content, 'html.parser')
            date_elem_parent = offer_page_soup.find('div', class_='adPrice')
            date_elem = date_elem_parent.findChild('div', class_='info')
            print(date_elem.text)
            print(date_manager.parse_date(date_elem.text))
            break #temp so we dont overload the server with requests while testing
        # General idea:
        # 1. Get the offers from the first page
        # 2. Read the Last visited date
        # 3. Loop through the offers while offer's date is newer than the last visited date.

        # Challenges:
        # compare the dates in textual Bulgarian - partialy implemented
        # navigate to next page
