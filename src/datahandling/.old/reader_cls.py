import csv
import collections.abc
from abc import ABC, abstractmethod

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

class Collection(collections.abc.Sequence):
    '''
    Collection
    '''
    def __init__(self, columns):
        self.column_names =list(columns)
        self.column_data =list(columns.values())


    def __len__(self):
        return len(self.column_data[0])

    def __getitem__(self, index):
        return dict(zip(self.column_names,
                        (col[index] for col in self.column_data)))

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)

def  read_csv_as_columns(file, types):
    columns = collections.defaultdict(list)
    with open(file) as handler:
        reader = csv.reader(handler)
        headers = next(reader)
        for row in reader:
            for name, func, val in zip(headers, types, row):
                columns[name].append(func(val))
    return Collection(columns)


def  read_csv_as_dicts(file, coltypes):
    parser = DictCSVParser(coltypes)
    return parser.parse(file)


if __name__ == '__main__':
    # portfolio = read_csv_as_dicts('Data/portfolio.csv', [str,int,float])
    # for s in portfolio:
    #      print(s)

    rows = read_csv_as_dicts('Data/ctabus.csv', [str,str,str,int])
    print(rows)
    print(len(rows))
    print(rows[0])
