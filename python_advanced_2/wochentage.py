import time

wochentage = {0: "Montag", 1: "Dienstag"

def get_weekday(date_as_string):
    date_object = time.strptime(date_as_string, "%d.%m.%Y")
    print(date_object)
    return wochentage[date_object.tm_wday]

print(get_weekday("02.01.2011"))