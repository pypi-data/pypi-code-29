name = "wtf"

from . import base

def baidu2google(lng, lat):
	return base.bd09_to_wgs84(lng, lat)

def google2baidu(lng, lat):
	return base.wgs84_to_bd09(lng, lat)

def amap2google(lng, lat):
	return base.gcj02_to_wgs84(lng, lat)

def google2amap(lng, lat):
	return base.wgs84_to_gcj02(lng, lat)

