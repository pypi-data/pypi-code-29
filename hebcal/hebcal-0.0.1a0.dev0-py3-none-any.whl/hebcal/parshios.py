from pyluach import parshios
import datetime
import heb_date


if __name__ == '__main__':

    d = heb_date.Date(datetime.datetime.now(), (40.092383, -74.219996),
                      timezone='America/New_York')

    par = parshios.getparsha_string(d.heb_date)

    print(par)
