import sys
from abc import ABC, abstractclassmethod

import structly.reader
from stock import Stock



class TableFormatter(ABC):
    @abstractclassmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractclassmethod
    def row(self, rowdata):
        raise NotImplementedError()


class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

from .formats import TextTableFormatter, CSVTableFormatter, HTMLTableFormatter

def create_formatter(format, column_formats=None, upper_header=False):
    formatter = {
        'text': TextTableFormatter,
        'csv': CSVTableFormatter,
        'html': HTMLTableFormatter
     }
    formatter_cls = formatter[format]

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_header:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError(f'Expected {TableFormatter.__name__}')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

if __name__ == '__main__':
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
    print_table(portfolio,['shares','name'], formatter)
    with redirect_stdout(open('out.txt', 'w')) as file:
            print_table(portfolio, ['name','shares','price'], formatter)
            file.close()