from django.db.transaction import get_connection


def exec_sql(sql, vars=None, using=None):
    with get_connection(using).cursor() as cursor:
        cursor.execute(sql, vars)

        if cursor.rowcount > 0:
            return cursor.fetchone()


def exec_sql_modify(sql, vars=None, using=None):
    with get_connection(using).cursor() as cursor:
        cursor.execute(sql, vars)
        return cursor.rowcount


def iter_sql(sql, vars=None, using=None):
    with get_connection(using).cursor() as cursor:
        cursor.execute(sql, vars)
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
