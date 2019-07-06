import time
import _strptime
# Mit strptime kann man aus einem String ein Datum machen
birthday = time.strptime("19.08.95", "%d.%m.%y")  
print(birthday.tm_wday)