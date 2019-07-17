from bs4 import BeautifulSoup
import urllib.request as request
import time


class UfoSight:
    def __init__(self, timestamp, summary, shape, location):
        self.timestamp, self.summary, self.shape, self.location = timestamp, summary, shape, location

    def __str__(self):
        return "{}, gesichtet zum Zeitpunkt {} in der Stadt {}. Beschreibung: {}" \
            .format(self.shape or "Unbekannt", self.timestamp, self.location or "Unbekannt", self.summary)


def get_html_source(url):
    return request.urlopen(url)


def build_url_for_date(date):
    return "http://www.nuforc.org/webreports/ndxe{}.html".format(date)


def all_table_entries_for_date(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find("table", attrs={'cellspacing': '1'}).tbody.find_all("tr")


def safe_extract_contents(tag):
    if tag.contents and str(tag.contents[0]) != "<br/>":
        return tag.contents[0]


def extract_sight_data_from_entry(entry):
    all_columns = entry.find_all("td")
    date = safe_extract_contents(all_columns[0].font.a)
    city = safe_extract_contents(all_columns[1].font)
    shape = safe_extract_contents(all_columns[3].font)
    summary = safe_extract_contents(all_columns[5].font)
    return UfoSight(date, summary, shape, city)


def get_list_of_all_sightings_in_month(date):
    url = build_url_for_date(date)
    content = get_html_source(url)
    sightings = []
    for entry in all_table_entries_for_date(content):
        sightings.append(extract_sight_data_from_entry(entry))
    return sightings


def get_current_year_month():
    current_time = time.gmtime()
    current_year = current_time.tm_year
    current_month = current_time.tm_mon
    return current_year, current_month


def get_last_month(year, current_year, current_month):
    if year == current_year:
        return current_month
    else:
        return 12


def get_months_since(year, month):
    current_year, current_month = get_current_year_month()
    all_months = []
    for year in range(year, current_year + 1):
        last_month = get_last_month(year, current_year, current_month)
        for m in range(month, last_month + 1):
            all_months.append(str(year) + str(m).zfill(2))
    return all_months


if __name__ == '__main__':
    months_to_download = get_months_since(2018, 1)
    for month in months_to_download:
        for sighting in get_list_of_all_sightings_in_month(month):
            print(sighting)
