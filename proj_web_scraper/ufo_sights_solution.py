from bs4 import BeautifulSoup
import urllib.request as request
import sqlite3


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
    table_data = entry.find_all("td")
    date = safe_extract_contents(table_data[0].font.a)
    city = safe_extract_contents(table_data[1].font)
    shape = safe_extract_contents(table_data[3].font)
    summary = safe_extract_contents(table_data[5].font)
    return date, city, shape, summary


def get_list_of_all_sightings_in_month(date):
    url = build_url_for_date(date)
    content = get_html_source(url)
    sightings = []
    for entry in all_table_entries_for_date(content):
        sightings.append(extract_sight_data_from_entry(entry))
    return sightings


def get_index_page_contents():
    return request.urlopen("http://www.nuforc.org/webreports/ndxevent.html")


def extract_month_from_index_entry(entry):
    all_columns = entry.find_all("td")
    date = safe_extract_contents(all_columns[0].font.a)
    return date


def month_to_url_format(month):
    month, year = month.split("/")
    return year + month


def get_recorded_months(content):
    soup = BeautifulSoup(content, 'html.parser')
    all_entries = soup.find("table", attrs={'cellspacing': '1'}).tbody.find_all("tr")
    result = []
    for entry in all_entries:
        result.append(month_to_url_format(extract_month_from_index_entry(entry)))
    return result


def save_to_database(conn, record):
    conn.cursor().execute("INSERT INTO ufo_sights (time, summary, shape, location) VALUES (?, ?, ?, ?)", record)
    con.commit()


create_table_statement = """
CREATE TABLE IF NOT EXISTS ufo_sights (
    time string,
    summary string,
    shape string,
    location string
);"""

if __name__ == '__main__':
    con = sqlite3.connect("ufo-db.sqlite")
    cur = con.cursor()
    cur.execute(create_table_statement)
    index = get_index_page_contents()
    months_to_download = get_recorded_months(index)
    for month in months_to_download[:1]:
        for sighting in get_list_of_all_sightings_in_month(month):
            save_to_database(con, sighting)
    con.close()
