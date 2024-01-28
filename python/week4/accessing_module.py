import sys
from pprint import pprint

locations = sys.path

print(locations)
pprint(locations)

for x in locations:
    print(x)

import calendar 

isleap=calendar.leapdays(2034,2040)
print(isleap)

print(calendar.isleap(2036))