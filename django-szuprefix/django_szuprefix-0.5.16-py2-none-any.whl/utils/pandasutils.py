# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals, division
import pandas as pd
from .dbutils import db_sqlalchemy_str, get_table_fields, getDB
from pandas.io.sql import pandasSQL_builder
import math
from datetime import datetime
from collections import OrderedDict
import logging

log = logging.getLogger("django")


def get_select_sql(sql):
    sql = sql.strip()
    return ' ' in sql.lower() and sql or (u'select * from %s' % sql)


def get_dataframe_from_table(table_name_or_sql, connection="default", coerce_float=True, just_sql=True):
    sql = table_name_or_sql if just_sql else get_select_sql(table_name_or_sql)
    sql = sql.replace("%", "%%")
    con = connection.startswith("hive://") and connection or db_sqlalchemy_str(connection)
    return pd.read_sql(sql, con, coerce_float=coerce_float)


def write_dataframe_to_table(df, **kwargs):
    kwargs['con'] = db_sqlalchemy_str(kwargs['con'])
    return df.to_sql(**kwargs)


def smart_write_dataframe_to_table(df, **kwargs):
    con = db_sqlalchemy_str(kwargs['con'])


def split_dataframe_into_chunks(df, chunksize=10000):
    for i in range(int(math.ceil(len(df) / chunksize))):
        b = i * chunksize
        e = b + chunksize - 1
        yield df.loc[b:e]


def dtype(dt):
    return dt.startswith('int') and 'int' \
           or dt.startswith('float') and 'float' \
           or dt.startswith('datetime') and 'datetime' \
           or 'string'


def series_dtype(series):
    dt = str(series.dtype)
    return dtype(dt)


def ftype(ft):
    return ft == "string" and "varchar(255)" or ft == "datetime" and "TIMESTAMP" or ft


def format_timestamp(df):
    for c, dt in df.dtypes.iteritems():
        if str(dt).startswith("datetime"):
            df[c] = df[c].apply(lambda x: x.isoformat())
    return df


def clear_dict_nan_value(d):
    for k, v in d.items():
        if pd.isnull(v) or v == 'NaT':
            d[k] = None
    return d


def lower_column_name(df):
    a = {}
    for c in df.columns:
        if c != c.lower():
            a[c] = c.lower()
    if a:
        df.rename(columns=a, inplace=True)


def dataframe_to_table(df, is_preview=False):
    count = len(df)
    if is_preview and count > 20:
        data = df[:10].merge(df[-10:], how='outer')
    else:
        data = df
    data = [clear_dict_nan_value(d) for d in data.to_dict("records")]
    from pandas.io.json.table_schema import build_table_schema
    schema = build_table_schema(df, index=False)
    return dict(data=data, count=count, fields=schema.get('fields'), is_preview=is_preview)


def group_by(df, dimension, measures=None, agg='count', interval=None):
    if interval:
        formats = {
            'year': '%Y',
            'month': '%Y-%m',
            'day': '%Y-%m-%d',
            'hour': '%Y-%m-%d %H',
            'minute': '%Y-%m-%d %H:%M',
            'second': '%Y-%m-%d %H:%M:%S',
        }
        group = df.groupby(df[dimension].dt.strftime(formats.get(interval)))
    else:
        group = df.groupby(dimension)
    if not measures:
        return group[dimension].agg(agg).to_frame(agg).reset_index()
    else:
        return group[measures].agg(agg).reset_index()


def guess_dimension_category(n):
    d = {
        "国家": "geo.country",
        "省份": "geo.province",
        "城市": "geo.city",
        "金额": "currency",
        "日期": "date",
        "时间": "datetime"
    }
    for k, v in d.iteritems():
        if n.endswith(k):
            return v


def guess_measure_category(n):
    d = {
        "金额": "currency"
    }
    for k, v in d.iteritems():
        if n.endswith(k):
            return v


def guess_dimensions(df, nunique_limit=1000):
    columns = OrderedDict()
    rc = len(df)
    for c in df.columns:
        dt = series_dtype(df[c])
        columns[c] = {'name': c, 'type': dt}

    id_field = None
    measures = []
    dimensions = []
    for c in columns.values():
        cn = c['name']
        nunique = df[cn].agg('nunique')
        if nunique == rc and id_field is None:
            id_field = cn
            continue
        if c['type'] in ['int', 'float']:
            c['category'] = guess_measure_category(cn)
            measures.append(c)
        else:
            dimension_deny = c['type'] not in ['datetime',
                                               'date'] and rc >= nunique_limit and nunique > nunique_limit * 0.1
            if dimension_deny:
                print c
                continue
            c['category'] = guess_dimension_category(cn)
            if c['type'] == 'string' and c['category'] not in ['date', 'datetime']:
                c['members'] = list(df[cn].unique())
            dimensions.append(c)
    return OrderedDict(
        dimensions=dimensions,
        measures=measures,
        id_field=id_field
    )


class AutoGrowTable(object):
    def __init__(self, db_name, table_name, primary_key, insert_timestamp_field=None, update_timestamp_field=None):
        self.db_name = db_name
        self.connection = getDB(self.db_name)
        tps = table_name.split(".")
        self.table_name = tps[-1]
        self.schema = len(tps) > 1 and tps[0] or None
        self.full_table_name = self.schema and "%s.%s" % (self.connection.ops.quote_name(self.schema),
                                                          self.connection.ops.quote_name(
                                                              self.table_name)) or self.connection.ops.quote_name(
            self.table_name)
        self.primary_key = primary_key
        self.fields = {}
        self.insert_timestamp_field = insert_timestamp_field
        self.update_timestamp_field = update_timestamp_field
        self.pd_sql = pandasSQL_builder(db_sqlalchemy_str(self.db_name), schema=self.schema)
        self.detect_fields()

    def detect_fields(self):
        try:
            self.fields = [f.lower() for f in get_table_fields(getDB(self.db_name), self.table_name, self.schema)]
        except Exception, e:
            err_str = str(e)
            if "does not exist" in err_str:
                return
            log.error("AutoGroupTable.detect_fields %s %s error: %s", self.db_name, self.table_name, e)

    def get_field_definition(self, fields):
        return ",".join(["%s %s" % (f, ftype(f)) for f in fields])

    def create_table(self, df):
        exists = self.pd_sql.has_table(self.table_name)
        dtypes = dict([(c, dtype(str(dt))) for c, dt in df.dtypes.iteritems()])
        new_fields = ["%s %s" % (f, ftype(dt)) for f, dt in dtypes.iteritems() if f.lower() not in self.fields]
        if self.update_timestamp_field and self.update_timestamp_field not in self.fields:
            new_fields.append("%s timestamp default CURRENT_TIMESTAMP" % self.update_timestamp_field)
        if self.insert_timestamp_field and self.insert_timestamp_field not in self.fields:
            new_fields.append("%s timestamp default CURRENT_TIMESTAMP" % self.insert_timestamp_field)
        with self.connection.cursor() as cursor:
            if not exists:
                sql = "create table %s(%s)" % (self.full_table_name, ",".join(new_fields))
                # print sql
                cursor.execute(sql)
                sql = "alter table %s add primary key(%s)" % (self.full_table_name, self.primary_key)
                # print sql
                cursor.execute(sql)
                self.detect_fields()
            else:
                if new_fields:
                    sql = "alter table %s add column %s" % (self.full_table_name, ", add column ".join(new_fields))
                    # print sql
                    cursor.execute(sql)

    def run(self, data_frame):
        df = data_frame
        lower_column_name(df)
        self.create_table(df)
        errors = self.insert_or_update(df)
        return errors

    def gen_sql_table(self, df):
        from pandas.io.sql import SQLTable
        from sqlalchemy import Column, DateTime
        self.table = SQLTable(self.table_name, self.pd_sql, df, index=False, schema=self.schema).table.tometadata(
            self.pd_sql.meta)
        if self.update_timestamp_field and self.update_timestamp_field not in self.table.columns:
            self.table.append_column(Column(self.update_timestamp_field, DateTime))
        if self.insert_timestamp_field and self.insert_timestamp_field not in self.table.columns:
            self.table.append_column(Column(self.insert_timestamp_field, DateTime))

    def split_insert_and_update(self, df):
        # self.table.select(  df[self.primary_key]
        pass

    def insert_or_update(self, df):
        self.gen_sql_table(df)
        errors = []
        df = format_timestamp(df)
        pks = [k.strip() for k in self.primary_key.split(",")]
        efs = ['1 as a']
        if self.insert_timestamp_field:
            efs.append(self.insert_timestamp_field)
        if self.update_timestamp_field:
            efs.append(self.update_timestamp_field)
        sql_template = "select %s from %s where %%s" % (",".join(efs), self.full_table_name)
        quote_name = self.connection.ops.quote_name
        for i in xrange(len(df)):
            try:
                s = df.iloc[i]
                d = clear_dict_nan_value(s.to_dict())
                where = " and ".join(["%s='%s'" % (quote_name(pk), d[pk.lower()]) for pk in pks])
                sql = sql_template % where
                rs = self.pd_sql.read_sql(sql, coerce_float=False)
                now = datetime.now().isoformat()
                if not rs.empty:
                    r = rs.iloc[0]
                    if self.update_timestamp_field:
                        d[self.update_timestamp_field] = now
                    if self.insert_timestamp_field:
                        d[self.insert_timestamp_field] = r[self.insert_timestamp_field]
                    self.table.update().where(where).values(d).execute()
                else:
                    if self.insert_timestamp_field:
                        d[self.insert_timestamp_field] = now
                    if self.update_timestamp_field:
                        d[self.update_timestamp_field] = now
                    self.table.insert(d).execute()
            except Exception, e:
                errors.append(([d[k.lower()] for k in pks], str(e)))
        if errors:
            log.error("pandas.AutoGrowTable %s.%s insert_or_update got %d errors: %s", self.db_name, self.table_name,
                      len(errors), errors)
        return errors

    def update(self, df):
        for r in xrange(len(df)):
            self.table.update(df.iloc[r].to_dict()).execute()
