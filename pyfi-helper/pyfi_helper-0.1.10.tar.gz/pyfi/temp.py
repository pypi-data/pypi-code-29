# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:12:45 2018

@author: lukewang
"""
from datetime import datetime
import pandas as pd

begin_date = datetime(2006, 1, 1)
end_date = datetime(2018, 2, 1)
from pyfi import WindHelper as w, spring_month

# cpi环比
cpi_r = w.edb(codes=["M0068116"], begin_date=datetime(1995, 1, 1), end_date=end_date).iloc[:, 0]
spring = pd.Series(index=cpi_r.index)
for i in range(len(cpi_r)):
    if cpi_r.index[i].month == 1 or i == 0:
        spring_m = spring_month(cpi_r.index[i].year)
    if cpi_r.index[i].month == spring_m:
        spring[i] = True
    else:
        spring[i] = False
supseason_ind = pd.Series(index=cpi_r.index)
supseason_cum_ind = pd.Series(index=cpi_r.index)
window = 5
for i in range(12, len(cpi_r)):

    cur_date = cpi_r.index[i]
    past = cpi_r[:i]
    past_spring = spring[:i]
    spring_cur = spring[i]
    chosen = past.loc[(past.index.month == cpi_r.index[i].month) & (past_spring == spring_cur)][-window:]
    chosen_cum = past.loc[(past.index.month == cpi_r.index[i].month)][-window:]
    avg = chosen.mean()
    avg_cum = chosen.mean()
    supseason_ind[i] = cpi_r[i] - avg
    if cpi_r.index[i].month == 1:
        supseason_cum_ind[i] = supseason_ind[i]
    else:
        supseason_cum_ind[i] = supseason_cum_ind[i - 1] + supseason_ind[i]
supseason_ind[begin_date:end_date]
data = supseason_cum_ind[begin_date:end_date].dropna()
print(cpi_r.loc[(cpi_r.index.month == cpi_r.index[i].month) & (spring == False)])
