'''
readrides.py
'''

import csv
import tracemalloc
from pprint import pprint
import collections.abc
import reader
from sys import intern

class RidersData(collections.abc.Sequence):
    '''
    RidersData
    '''
    def __init__(self):
        self.routes = []
        self.date = []
        self.daytype = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return {
                'date': self.date[index],
                'daytype': self.daytype[index],
                'numrides': self.numrides[index],
                'route': self.routes[index]
            }
        elif isinstance(index, slice):
            return [{
                'date': date,
                'daytype': daytype,
                'numrides': numrides,
                'route': route
            } for route, date, daytype, numrides in
            zip(self.routes[index], self.date[index], self.daytype[index], self.numrides[index])]
        else:
            raise NotImplementedError()


    def append(self, row):
        '''
        append
        '''
        self.routes.append(row['route'])
        self.date.append(row['date'])
        self.daytype.append(row['daytype'])
        self.numrides.append(row['rides'])

class Row:
    '''
    Row
    '''
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__
class RowSlots:
    ''''
    RowSlots
    '''
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = RidersData()
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    from collections import namedtuple
    RowTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
    records = []
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowTuple(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_class_slots(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowSlots(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

def main():
    '''
    main'''
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('Memory Use (Tuples): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_dicts('Data/ctabus.csv')
    print('Memory Use (Dictionary): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_columns('Data/ctabus.csv')
    print('Memory Use (Columns): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_class('Data/ctabus.csv')
    print('Memory Use (Class): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_named_tuple('Data/ctabus.csv')
    print('Memory Use (Named Tuple): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_class_slots('Data/ctabus.csv')
    print('Memory Use (Class Slots): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = reader.read_csv_as_dicts('Data/ctabus.csv', [str,str,str,int])
    print('Memory Use (Zipped Dict): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = reader.read_csv_as_dicts('Data/ctabus.csv', [intern, str, str,int])
    print('Memory Use (Zipped Dict), Key cached): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = reader.read_csv_as_dicts('Data/ctabus.csv', [intern, intern, str,int])
    print('Memory Use (Zipped Dict), Key and Date Cached): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = reader.read_csv_as_columns('Data/ctabus.csv', [str,str,str,int])
    print('Memory Use (Data Collection Columns): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = reader.read_csv_as_columns('Data/ctabus.csv', [intern, str, str,int])
    print('Memory Use (Data Collection Columns, Key cached): Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = reader.read_csv_as_columns('Data/ctabus.csv', [intern, intern, str,int])
    print('Memory Use (Data Collection Columns, Key and Date Cached): Current %d, Peak %d' % tracemalloc.get_traced_memory())


if __name__ == '__main__':
    main()
    # rows = read_rides_as_dicts('Data/ctabus.csv')
    # print(len(rows))
    # print(rows[0])
    # r = rows[0:10]
    # pprint(r)
    # print(len(r))
    # print(r[0])
