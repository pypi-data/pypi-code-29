# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/9/17 上午10:43
#  @brief: 
# ===============================================================

# mysql连接池配置
sql_engine_config = {
    # 默认连接池数量
    'pool_size': 1,
    # 最多允许溢出的连接数
    'max_overflow': 4,
    # 连接池回收时间
    'pool_recycle': 5,
    # 与mysql交互的超时时间
    'pool_timeout': 15,
    # 在与mysql交互前先检验连接是否有效
    'pool_pre_ping': True
}

# 邮件服务器的配置
mail_config = {
    'host': 'smtp.exmail.qq.com',
    'port': 465,
    'user': 'alert@zhiyitech.cn',
    'password': 'BUpiEjgxJjNRKGAN'
}
