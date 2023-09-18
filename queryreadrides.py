"""
queryreadrides.py
"""
from collections import Counter
from collections import defaultdict
import readrides

rows = readrides.read_rides_as_dict('Data/ctabus.csv')

# How many bus routes exist in Chicago?
len({route["route"] for route in rows})

# How many people rode the number 22 bus on February 2, 2011? 
# What about any route on any date of your choosing?
rides = [route['rides'] \
 for route in rows \
    if route['date'] == '02/22/2011' and route['route'] == '22']
sum([route['rides'] for route in rows if route['date'] == '02/22/2011'])

# What is the total number of rides taken on each bus route?
total = Counter()
for route in rows:
    total[route['route']] += route['rides']

# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
byyear = defaultdict(list)
for row in rows:
    date = row["date"]
    year = date.split('/')[2]
    byyear[(year,row["route"])].append(row)

total_byyear = Counter()
for year, route in byyear:
    total_byyear[(year, route)] += sum([row["rides"] for row in byyear[(year,route)]])

increase_byyear = Counter()
for year, route in total_byyear:
    PREV_YEAR = str(int(year)-1)
    if (PREV_YEAR, route) in total_byyear:
        increase_byyear[(year, route)] += \
            total_byyear[(PREV_YEAR, route)] - total_byyear[(year, route)]
    else:
        increase_byyear[(year, route)] = 0
increase_byyear.most_common(2)
