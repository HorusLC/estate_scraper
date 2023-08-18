import configs
from scraper import Scraper

if __name__ == '__main__':
    estate_scraper: Scraper = Scraper(configs.URL)
    estate_scraper.scrape_page()
    from _datetime import datetime
    import locale
    locale.setlocale(locale.LC_ALL, 'bg_BG')
    #print(datetime.strftime("%a, %d %b %Y %H:%M:%S"))
    date = datetime.strptime('четв, 17 авг 2023', "%a, %d %b %Y")
    print(date)
