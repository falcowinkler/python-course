from persistence_solution import *
from web_scraper_solution import *


if __name__ == '__main__':
    index = get_index_page_contents()
    conn = open_connection()
    create_ufo_table_if_not_exists(conn)
    months_to_download = get_recorded_months(index)
    for month in months_to_download[:10]:
        all_sights = get_list_of_all_sightings_in_month(month)
        for sighting in all_sights:
            save_to_database(conn, sighting)
    conn.close()

