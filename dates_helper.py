from datetime import datetime
import locale


class DateHelper:

    def __init__(self, last_visited):
        self.last_visited = last_visited

    def __init__(self):
        self.last_visited = datetime.now()

    def parse_date(self, date_str):
        """
        Deals with extracting the date info from the date element and creating a date obj

        :return datetime object
        """
        date_split = date_str.rsplit(' на ')[1].rsplit(' год.')[0]
        print(date_split)
        locale.setlocale(locale.LC_ALL, 'bg_BG')
        date_words = date_split.split()
        date_words[1] = date_words[1].capitalize()
        print(date_words)
        overall_date = datetime.strptime(' '.join(date_words), '%d %B, %Y')
        print(overall_date)
        return overall_date
