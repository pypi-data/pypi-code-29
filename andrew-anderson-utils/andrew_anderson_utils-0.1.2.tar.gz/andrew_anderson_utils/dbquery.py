def lin_arr(arr):
    res = []
    for i in arr:
        for j in i:
            res.append(j)
    return res


def fit_items(str_, *items):
    for i in items:
        if type(i) is str:
            if i == '*':
                str_ = str_.replace('?', '*', 1)
            else:
                str_ = str_.replace('?', '"%s"' % i, 1)
        elif type(i) is int:
            str_ = str_.replace('?', "%s" % i, 1)
        elif i is None:
            str_ = str_.replace('?', "NULL", 1)
        elif type(i) is list or type(i) is tuple:
            arr = [fit_items('?', j) for j in i]
            str_ = str_.replace('?', ', '.join(arr), 1)
        elif type(i) is dict:
            arr = [fit_items('? = ?', key, value) for key, value in i.items()]
            str_ = str_.replace('?', ' AND '.join(arr), 1)
        else:
            raise TypeError('Unknown type for fitting: %s' % type(i))
    return str_


def get_columns(db, table):
    return [i[1] for i in db.execute('PRAGMA table_info(%s)' %
                                     table).fetchall()]


def variables():
    var = dict()

    def getter(self, name):
        nonlocal var
        var.setdefault(self, dict())
        return var[self][name]

    def setter(self, **kwargs):
        nonlocal var
        var.setdefault(self, dict())
        var[self].update(kwargs)

    def delete(self, name):
        nonlocal var
        var.setdefault(self, dict())
        del var[self][name]

    return getter, setter, delete


class EntryList:
    getter, setter, delete = variables()

    def __init__(self, db, table, selection):
        self.setter(db=db)
        self.setter(table=table)
        self.setter(selection=selection)

    def __str__(self):
        query = fit_items('SELECT * FROM ? WHERE ' +
                          self.getter('selection'),
                          self.getter('table'))
        return str(self.getter('db').execute(query).fetchall())

    def __iter__(self):
        query = fit_items('SELECT * FROM ? WHERE ' +
                          self.getter('selection'),
                          self.getter('table'))
        return iter(self.getter('db').execute(query).fetchall())

    def select(self, *args):
        columns = get_columns(self.getter('db'),
                              self.getter('table'))
        if args != () and args != ('*'):
            for i in args:
                if i not in columns:
                    raise AttributeError
        else:
            args = columns
        query = fit_items('SELECT ? FROM ? WHERE ' +
                          self.getter('selection'), args,
                          self.getter('table'))
        res = self.getter('db').execute(query).fetchall()
        return res

    def update(self, **kwargs):
        columns = get_columns(self.getter('db'),
                              self.getter('table'))
        assert(len(kwargs) > 0)
        for i in kwargs.keys():
            if i not in columns:
                raise AttributeError
        '''
        query = fit_items('UPDATE ? SET ' + '? = ? ' * (len(kwargs)) +
                          'WHERE ' +
                          self.getter('selection'),
                          self.getter('table'),
                          *lin_arr(kwargs.items()))
        '''
        query = fit_items('UPDATE ? SET ? WHERE ' +
                          self.getter('selection'),
                          self.getter('table'),
                          kwargs)
        res = self.getter('db').execute(query).fetchall()
        self.getter('db').commit()
        return res

    def __call__(self, *args):
        return self.select(*args)

    def __getitem__(self, name):
        return [i[0] for i in self.select(name)]

    def __getattr__(self, name):
        return [i[0] for i in self.select(name)]

    def __setitem__(self, name, value):
        return self.update(**{name: value})

    def __setattr__(self, name, value):
        return self.update(**{name: value})

    def __len__(self):
        query = fit_items('SELECT * FROM ? WHERE ' +
                          self.getter('selection'),
                          self.getter('table'))
        res = self.getter('db').execute(query).fetchall()
        return len(res)


class Table:
    def __init__(self, db, table):
        self.db = db
        self.table = table

    def where(self, **kwargs):
        assert(len(kwargs) > 0)
        # '''
        selection = fit_items('AND'.join(['? = ?'] * len(kwargs)),
                              *lin_arr(kwargs.items()))
        '''
        selection = fit_items('?', [kwargs, ' AND '])
        '''
        return EntryList(self.db, self.table, selection)

    def __call__(self, **kwargs):
        return self.where(**kwargs)

    def insert(self, *args):
        query = fit_items('INSERT INTO ? VALUES (%s);' %
                          ', '.join(['?'] * len(args)),
                          self.table, *args)
        self.db.execute(query)
        self.db.commit()
        return args
