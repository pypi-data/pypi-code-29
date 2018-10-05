# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from sql.conditionals import Case
from sql import Null
from trytond.transaction import Transaction
from trytond.pool import Pool


__all__ = ['TimesheetLine']

class TimesheetLine(metaclass=PoolMeta):
    __name__ = 'timesheet.line'
    
    has_invoice = fields.Function(fields.Boolean(string=u'Invoiced', readonly=True), 
        'get_has_invoice', searcher='search_has_invoice')

    @classmethod
    def get_has_invoice_sql(cls):
        """ sql-code for query
        """
        TimesheetLine = Pool().get('timesheet.line')
        tab_tsl = TimesheetLine().__table__()

        qu1 = tab_tsl.select(tab_tsl.id,
                Case(
                    (tab_tsl.invoice_line != Null, True),
                    else_ = False
                ).as_('invoiced')
            )
        return qu1
    
    @staticmethod
    def order_has_invoice(tables):
        tab_tsl, _ = tables[None]

        return [Case((tab_tsl.invoice_line == Null, 0), else_=1)]

    @classmethod
    def get_has_invoice(cls, lines, names):
        """ query table
        """
        tab_qu = cls.get_has_invoice_sql()
        cursor = Transaction().connection.cursor()
        id_lst = [x.id for x in lines]
        
        # prepare result
        res1 = {'has_invoice': {}}
        for i in id_lst:
            res1['has_invoice'][i] = False
        
        qu1 = tab_qu.select(tab_qu.id,
                tab_qu.invoiced,
                where=tab_qu.id.in_(id_lst)
            )
        cursor.execute(*qu1)
        l1 = cursor.fetchall()
        for i in l1:
            (id1, inv1) = i
            res1['has_invoice'][id1] = inv1

        res2 = {}
        for i in names:
            res2[i] = res1[i]
        return res2
    
    @classmethod
    def search_has_invoice(cls, name, clause):
        """ sql-code for table search
        """
        tab_qu = cls.get_has_invoice_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]
        
        qu1 = tab_qu.select(tab_qu.id,
                where=Operator(tab_qu.invoiced, clause[2]))
        return [('id', 'in', qu1)]

# end TimesheetLine
