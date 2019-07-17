from bs4 import BeautifulSoup
import urllib.request as request
import time


def get_html_source(url):
    return request.urlopen(url)


def build_url_for_date(date):
    return "http://www.nuforc.org/webreports/ndxe" + date + ".html"


def all_table_entries_for_date(content):
    soup = BeautifulSoup(content, 'html.parser')
    all_entries = soup.find('table', attrs={"cellspacing": "1"})
    body = all_entries.tbody
    return body.find_all("tr")


def safe_extract_contents(tag):
    if tag.contents and str(tag.contents[0]) != "<br/>":
        return tag.contents[0]


def extract_sight_data_from_entry(entry):
    table_data = entry.find_all("td")
    date = safe_extract_contents(table_data[0].font.a)
    city = safe_extract_contents(table_data[1].font)
    shape = safe_extract_contents(table_data[3].font)
    summary = safe_extract_contents(table_data[5].font)
    return date, city, shape, summary


def get_current_year_and_month():
    zeitattribute = time.gmtime()
    year = zeitattribute.tm_year
    month = zeitattribute.tm_mon
    return year, month


def get_last_month(year, current_year, current_month):
    if year == current_year:
        return current_month
    else:
        return 12
        # wenn year gleich current_year
        # dann gebe current_month zurück
        # sonst gebe 12 zurück


# get_last_month(2017, 2019, 07) => 12
# get_last_month(2019, 2019, 07) => 07



def get_months_since(year, month):
    pass


url = build_url_for_date("201907")
html_code = get_html_source(url)
rows = all_table_entries_for_date(html_code)
print(get_current_year_and_month())
# for row in rows:
#    print(extract_sight_data_from_entry(row))
