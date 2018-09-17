import pandas as pd
from datetime import datetime

"""
本部分代码主要用于固化一些常规的指标，并用一定的命名规范对数据进行预处理：
细则如下：
- eco开头表示经济层面
- inf开头表示通胀层面
- val开头表示估值层面
- mon开头表示资金层面
- cyc开头表示周期层面
- sea开头表示海外层面
- tec开头表示技术情绪层面
"""


def gz10y(begin_date, end_date):
    """
    社融
    :param begin_date:
    :param end_date:
    :return:
    """
    from pyfi import WindHelper
    ytm = WindHelper.edb(codes=["gz10y"],
                         begin_date=begin_date,
                         end_date=end_date).iloc[:, 0]
    return ytm


def eco_sf(begin_date, end_date):
    """
    社融存量同比
    2016年以前的数据，存量年度增量和月度增量和的差按照加权比例分配到每个月进行核销
    :return:
    """
    from pyfi import WindHelper
    if begin_date < datetime(2004, 1, 31):
        raise Exception("社融起始时间太早啦")
    init_reserve = 148532.0  # 2002年末
    inc = WindHelper.edb(codes=["M5206730"],
                         begin_date=datetime(2003, 1, 1),
                         end_date=end_date, adjust=False)
    reserve = inc.cumsum() + init_reserve
    return (reserve / reserve.shift(12) - 1).iloc[:, 0].dropna()


def eco_ip(begin_date, end_date, method=2, adjust=False):
    """
    获取预处理之后的工业增加值数据
    :param method: 1: 删除 or 2: 沿用12月数据
    :param adjust: 是否交易日调整
    :param begin_date:
    :param end_date:
    :return:
    """

    from pyfi import WindHelper, macro_adjust
    start_date = "2002-02-01" if type(begin_date) is str else datetime(2002, 2, 1)
    ip = WindHelper.edb(codes=["ip_yoy", "ip_cyoy"],
                        begin_date=start_date,
                        end_date=end_date, adjust=adjust)
    ip = macro_adjust(ip.ip_yoy, ip.ip_cyoy, method=method)  # 2月份替换为累计同比
    return ip.loc[(ip.index >= begin_date) & (ip.index <= end_date)]


def eff_rmb_idx(begin_date="2010-01-01", end_date="2018-01-02"):
    """
    生成CFETS人民币汇率指数，并用BIS人民币实际汇率指数作为前期补充，该数据为月度数据
    :param begin_date:
    :param end_date:
    :return:
    """
    from pyfi import WindHelper as W
    mid_date = "2015-11-30" if type(end_date) is str else datetime(2015, 11, 30)
    bis = W.edb(["M0000209"], begin_date, mid_date).resample("M").last().ffill().iloc[:, 0]
    cfets = W.edb(["M0325601"], mid_date, end_date).resample("M").last().ffill().iloc[:, 0]
    data = ((bis.iloc[:-1]) * cfets[0] / bis[-1]).append(cfets)
    return data


def ds_ip_idx(begin_date, end_date):
    """
    去除季节性之后的ip的定基指数
    :param begin_date:
    :param end_date:
    :return:
    """
    import pyfi.DSfunctions as dsf
    # -----还原工业增加值绝对值-----
    IVA_idx = ip_idx(begin_date, end_date)
    IVA_Deseason = dsf.Deseason(IVA_idx.iloc[:, 0].dropna(how='all'), Jan_Feb=False)
    yoy_Deseason = (IVA_Deseason / IVA_Deseason.shift(12) - 1).dropna(how='all')
    return yoy_Deseason


def ip_idx(begin_date, end_date):
    from pyfi import WindHelper
    import pyfi.IVA_idx as ii
    df = WindHelper.edb(codes=['ip_yoy', 'ip_cyoy'], begin_date=begin_date, end_date=end_date)
    base = WindHelper.edb(codes=["M5567963"], begin_date=begin_date, end_date=end_date).iloc[:, 0]
    IVAyoy = df.loc[:, 'ip_yoy'] / 100.0
    IVAyoyc = df.loc[:, 'ip_cyoy'] / 100.0
    IVAyoyr = pd.DataFrame(1 + IVAyoy)
    IVAyoycr = pd.DataFrame(1 + IVAyoyc)
    Base = ii.mean_Jan_Feb(base)  # 平均基值的1、2月数据
    # -----还原工业增加值绝对值-----
    IVA_idx = ii.get_idx(IVAyoyr, IVAyoycr, Base).dropna()
    return IVA_idx


def ouput_gap(data, begin_date, end_date):
    pass


def ds_cpi():
    pass


def shuini(begin_date, end_date):
    """
    水泥指数
    :param begin_date:
    :param end_date:
    :return:
    """
    from pyfi import WindHelper
    df = WindHelper.edb(codes=["S5104572",
                               "S5104580",
                               "S5104577",
                               "S5104584",
                               "S5104588",
                               "S5104592"],
                        begin_date=begin_date,
                        end_date=end_date)
    return pd.DataFrame({"水泥指数": df.mean(axis=1)}, index=df.index)


def hbhdlm(begin_date, end_date):
    """
    环渤海动力煤(周度数据）
    :param begin_date:
    :param end_date:
    :return:
    """
    from pyfi import WindHelper
    df = WindHelper.edb(codes=["S5104572",
                               "S5104580",
                               "S5104577",
                               "S5104584",
                               "S5104588",
                               "S5104592"],
                        begin_date=begin_date,
                        end_date=end_date).ffill()
    return pd.DataFrame({"环渤海动力煤指数": df.mean(axis=1)}, index=df.index)


def get_inf_r_supseason(begin_date, end_date):
    from pyfi import WindHelper as w, get_end_date
    name_list = ["cpi", "食品", "非食品", "核心", "不包括鲜菜和鲜果",
                 "消费品", "服务", "食品烟酒", "食品烟酒-粮食", "食品烟酒-食用油",
                 "食品烟酒-鲜菜", "食品烟酒-畜肉类", "食品烟酒-畜肉类-猪肉", "品烟酒-畜肉类-牛肉", "食品烟酒-畜肉类-羊肉",
                 "食品烟酒-水产品", "食品烟酒-蛋类", "食品烟酒-奶类", "食品烟酒-鲜果", "食品烟酒-烟草",
                 "食品烟酒-酒类", "衣着", "衣着-服装", "衣着-衣着加工服务费", "衣着-鞋类",
                 "居住", "居住-租赁房房租", "居住-水电燃费", "生活用品及服务", "生活用品及服务-家用电器",
                 "生活用品及服务-家庭服务", "交通和通信", "交通和通信-交通工具", "交通和通信-交通工具用燃料", "交通和通信-交通工具使用和维修",
                 "交通和通信-通信工具", "交通和通信-通信服务", "交通和通信-邮递服务", "教育文化和娱乐", "教育文化和娱乐-教育服务",
                 "教育文化和娱乐-旅游", "医疗保健", "医疗保健-中药", "医疗保健-西药", "医疗保健-医疗服务",
                 "其他用品和服务"
                 ]
    code_list = [
        "M0000705", "M0000706", "M0061581", "M0085934", "M0096670",
        "M0061583", "M0061585", "M0327907", "M0062906", "M0068106",
        "M0062910", "M0062907", "M0068107", "M0085938", "M0085942",
        "M0062909", "M0062908", "M0068169", "M0062911", "M0068108",
        "M0068109", "M0000708", "M0068110", "M0096676", "M0068170",
        "M0000713", "M0068121", "M0068122", "M0000709", "M0068111",
        "M0068112", "M0000711", "M0327927", "M0068116", "M0068117",
        "M0068118", "M0068171", "M0327917", "M0000712", "M0068172",
        "M0068119", "M0000710", "M0068113", "M0068114", "M0068115",
        "M0327908"
    ]
    df = w.edb(code_list, begin_date, end_date) # .loc[:["M0068116"]]
    data = pd.DataFrame(index=df.index)
    data_cum = pd.DataFrame(index=df.index)
    for i in range(len(df.columns)):
        supseason_ind, supseason_cum_ind = supseason_ind(code_list[i], cur_date=get_end_date())
        # 计算超季节性：
        item = pd.DataFrame({df.columns[i]: supseason_ind})
        data = data.join(item, how="outer")
        # 计算累计超季节性：
        item_cum = pd.DataFrame({df.columns[i]: supseason_cum_ind})
        data_cum = data_cum.join(item_cum, how="outer")
    mapper = {key: value for key, value in zip(code_list, name_list)}
    data.columns = name_list
    data_cum.columns = name_list
    return data, data_cum


def supseason_ind(code, cur_date):
    """
    输入的为环比数据的wind代码
    超季节性指数
    :return:
    """
    from pyfi import WindHelper as w, spring_month
    import numpy as np
    # 环比数据
    cpi_r = w.edb(codes=[code], begin_date=datetime(1995, 1, 1), end_date=cur_date).iloc[:, 0]
    # 标记春节， 该月有春节则标记True,否则标记False
    spring = pd.Series(index=cpi_r.index)
    for i in range(len(cpi_r)):
        if cpi_r.index[i].month == 1 or i == 0:
            spring_m = spring_month(cpi_r.index[i].year)
        if cpi_r.index[i].month == spring_m:
            spring[i] = True
        else:
            spring[i] = False
    # 标记完成
    supseason_ind = pd.Series(index=cpi_r.index)
    supseason_cum_ind = pd.Series(index=cpi_r.index)
    cpi_cum_r = pd.Series(index=cpi_r.index)
    window = 5
    for i in range(12, len(cpi_r)):
        if cpi_cum_r.index[i].month == 1:
            cpi_cum_r[i] = cpi_r[i]/100.0
        else:
            cpi_cum_r[i] = (1 + (0 if np.isnan(cpi_cum_r[i - 1]) else cpi_cum_r[i - 1])) * (1 + cpi_r[i]/100.0) - 1
        past = cpi_r[:i]
        past_cum = cpi_cum_r[:i]
        past_spring = spring[:i]
        spring_cur = spring[i]
        chosen = past.loc[(past.index.month == cpi_r.index[i].month) & (past_spring == spring_cur)][-window:]
        chosen_cum = past_cum.loc[(past_cum.index.month == cpi_cum_r.index[i].month)][-window:].dropna()
        if len(chosen) > 0:
            avg = chosen.mean()
            supseason_ind[i] = cpi_r[i] - avg
        if len(chosen_cum) > 0:
            avg_cum = chosen_cum.mean()
            supseason_cum_ind[i] = cpi_cum_r[i] - avg_cum
    return supseason_ind, supseason_cum_ind


if __name__ == "__main__":
    # print(eco_ip("2006-1-1", "2018-1-1", method=2))
    begin_date = datetime(2006, 1, 1)
    end_date = datetime(2018, 9, 30)
    # print(supseason_ind("M0000705", cur_date=end_date))
    data, data_cum = get_inf_r_supseason(begin_date, end_date)
    data.sort_index(ascending=False).to_excel("超季节性.xlsx")
    data_cum.sort_index(ascending=False).to_excel("累计超季节性.xlsx")
    # df.to_excel("")
