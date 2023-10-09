from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        print(' '.join('<th>%s</th>' % h for h in headers), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        print(' '.join('<td>%s</td>' % h for h in rowdata), end='')
        print('</tr>')