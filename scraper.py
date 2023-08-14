import requests
from bs4 import BeautifulSoup
from requests import Session
import configs


class Scraper:
    """
    The Scraper class, that will do the hard work of getting the data.
    """

    def __init__(self, url: str):
        self.initial_url = url

    def scrape_offers(self):
        page = requests.get(configs.URL)
        the_soup = BeautifulSoup(page.text, 'html.parser')
        print(page.text)
        # General idea:
        # 1. Get the offers from the first page
        # 2. Read the Last visited date
        # 3. Loop through the offers while offer's date is newer than the last visited date.

        # Challenges:
        # compare the dates in textual Bulgarian
        # navigate to next page
