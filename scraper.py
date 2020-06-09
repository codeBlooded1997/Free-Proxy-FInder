import requests
from bs4 import BeautifulSoup
#from tabulate import *
import csv

class ProxyScraper:
    results = []

    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        content = BeautifulSoup(html, 'html.parser')
        table = content.find('table')
        rows = table.findAll('tr')
        headers = [header.text for header in rows[0]]
        results = [headers]

        for row in rows:
            # Checking if there is any data avilable.
            if len(row.findAll('td')):
                self.results.append([data.text for data in row.findAll('td')])

    def to_csv(self):
        with open('proxies.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.results)

    def run(self):
        response = self.fetch('https://free-proxy-list.net/')
        self.parse(response.content)
        self.to_csv()

if __name__ == '__main__':
    scraper = ProxyScraper()
    scraper.run()
