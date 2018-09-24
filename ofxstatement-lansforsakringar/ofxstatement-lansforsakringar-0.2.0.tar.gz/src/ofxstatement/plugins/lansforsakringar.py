import xlrd
from ofxstatement.parser import StatementParser
from ofxstatement.plugin import Plugin
from ofxstatement.statement import Statement, StatementLine, generate_transaction_id


class LansforsakringarPlugin(Plugin):
    """Länsförsäkringar <https://www.lansforsakringar.se>"""

    def get_parser(self, filename):
        bank_id = self.settings.get('bank', 'ELLFSESS')
        account_id = self.settings.get('account')
        return LansforsakringarParser(filename, bank_id, account_id)


class LansforsakringarParser(StatementParser):
    statement = Statement(currency='SEK')

    def __init__(self, filename, bank_id, account_id):
        self.filename = filename
        self.statement.bank_id = bank_id
        self.statement.account_id = account_id
        self.sheet = None
        self.row_num = 0

    def parse(self):
        with xlrd.open_workbook(self.filename) as book:
            self.sheet = book.sheet_by_index(0)
            return super().parse()

    def split_records(self):
        rows = self.sheet.get_rows()
        next(rows)  # statement date
        next(rows)  # headers
        return rows

    def parse_record(self, row):
        self.row_num += 1
        line = StatementLine()
        line.date = self.parse_datetime(row[0].value)
        line.date_user = self.parse_datetime(row[1].value)
        line.refnum = str(self.row_num)
        line.memo = row[2].value
        line.amount = row[3].value
        line.trntype = self.get_type(line)
        line.id = generate_transaction_id(line)
        return line

    @staticmethod
    def get_type(line):
        if line.amount > 0:
            return 'CREDIT'
        elif line.amount < 0:
            return 'DEBIT'
        else:
            return 'OTHER'
