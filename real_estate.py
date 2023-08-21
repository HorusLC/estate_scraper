class RealEstateOffer:
    """
    This class will represent the data that has been scraped from the site.
    Will implement it later when I figure out what data I want to save.
    """
    def __init__(self, date_published, price, size, currency, offer_link):
        self.date_published = date_published
        self.price = price
        self.size = size
        self.currency = currency
        self.offer_link = offer_link
