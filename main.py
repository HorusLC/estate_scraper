import configs
from scraper import Scraper

if __name__ == '__main__':
    estate_scraper: Scraper = Scraper(configs.URL)
    estate_scraper.scrape_offers()

