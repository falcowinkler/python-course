from bs4 import BeautifulSoup
import urllib.request as request
import urllib.error


class UfoSight:
    def __init__(self, timestamp, summary, shape, location):
        self.timestamp, self.summary, self.shape, self.location = timestamp, summary, shape, location

    def __str__(self):
        return "{}, gesichtet zum Zeitpunkt {} in der Stadt {}. Beschreibung: {}" \
            .format(self.shape or "Unbekannt", self.timestamp, self.location or "Unbekannt", self.summary)


def get_html_source(url):
    content = request.urlopen(url)
    return content


def build_url_for_date(date):
    return "http://www.nuforc.org/webreports/ndxe{}.html".format(date)


def all_table_entries_for_date(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find("table", attrs={'cellspacing': '1'}).tbody.find_all("tr")


def safe_extract_contents(tag):
    if len(tag.contents) > 0 and tag.contents[0].strip is not None:
        return tag.contents[0].strip()
    return None


def extract_sight_data_from_entry(entry):
    all_columns = entry.find_all("td")
    date = safe_extract_contents(all_columns[0].font.a)
    city = safe_extract_contents(all_columns[1].font)
    shape = safe_extract_contents(all_columns[3].font)
    summary = safe_extract_contents(all_columns[5].font)
    return UfoSight(date, summary, shape, city)


if __name__ == '__main__':
    date = "201907"
    url = build_url_for_date(date)
    content = get_html_source(url)
    for entry in all_table_entries_for_date(content):
        print(extract_sight_data_from_entry(entry))
