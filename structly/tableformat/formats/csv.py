from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join('%s' % h for h in headers))
    def row(self, rowdata):
        print(','.join('%s' % h for h in rowdata))