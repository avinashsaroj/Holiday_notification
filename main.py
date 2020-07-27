from plyer import notification
import requests
from bs4 import BeautifulSoup
import datetime



def notify(title, message):
    notification.notify(title=title, message=message, app_icon="chill.ico", timeout=15)


def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # notify("avi","lets start")
    myhtmldata = getdata('https://www.officeholidays.com/countries/india/')
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    stat_table = soup.find_all('table', class_='country-table')
    today = datetime.datetime.now().strftime("%b %d")
    # print(today)
    # print(len(stat_table))
    # print(soup.prettify())
    stat_table = stat_table[0]
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td')[1:3]:
            x = cell.text
            if today in x:
                notify("Holiday", x)








