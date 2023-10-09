import csv
import stock
from typing import List
import io
import logging
logging.basicConfig(level=logging.DEBUG)

__all__ = ['read_csv_as_dicts', 'read_csv_as_instances']

def read_csv_as_dicts(filename: str, types: []) -> []:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file,types)

def csv_as_dicts(lines: io.TextIOWrapper, types: [], has_header:bool=True) -> []:
    rows = csv.reader(lines)
    if has_header:
        headers = next(rows)
    else:
        headers = types
    return _csv_as_dicts(rows, types, headers)

def _csv_as_dicts(rows: List[str], types: [], headers:str):
    records = []
    for n, row in enumerate(rows):
        try:
            record = { name: func(val) 
                        for name, func, val in zip(headers, types, row) }
            records.append(record)
        except Exception as e:
            logging.warning(f"Row {n}: Bad row: {row}")
            logging.debug(e)
    return records


def read_csv_as_instances(filename: str, cls: object) -> List[object]:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)

def csv_as_instances(lines: io.TextIOWrapper, cls:object, has_header:bool=True) -> List[object]:
    records = []
    rows = csv.reader(lines)
    if has_header:
        _ = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def make_dict(headers, row):
    return dict(zip(headers, row))

def convert_csv(lines, func, has_header:bool=True):
    rows = csv.reader(lines)
    if has_header:
        headers = next(rows)
    return list(map(lambda row: func(headers, row), rows))
    

if __name__ == '__main__':
    file = open('Data/portfolio.csv')
    port = csv_as_dicts(file, [str,int,float])
    print(port)
    file = open('Data/portfolio.csv')
    port = csv_as_instances(file, stock.Stock)
    print(port)
    file = open('Data/portfolio_noheader.csv')
    port = csv_as_instances(file, stock.Stock, has_header=False)
    print(port)
    lines = open('Data/portfolio.csv')
    port = convert_csv(lines, make_dict)
    print(port)
    port = read_csv_as_dicts('Data/missing.csv', types=[str, int, float])
    print(len(port))