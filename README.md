# estate_scraper
Decided to try scraping

The idea of the program is to visit a real estate website and scrape the new offers(based on last visited mechanism).

**Current data scraped for the offer:**
1. Description
2. Size of property
3. Level
4. Price
5. Currency
6. Pictures
7. Date published(or changed)- currently the website shows 'published' until an edit to the property offer has been made. Then it shows the 'Last modified' date.

After scraping the data, the program sends the offer as a Telegram message through a bot, that I've made.

I've purposefully omitted the website link and other configurations. They are being loaded from and unversioned config file.
