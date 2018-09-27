# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/8/31 下午3:39
#  @brief: 
# ===============================================================

from .dao import Dao
from ..common import constants, util

sqls = constants.Sql
tb_names = constants.TBName


class TaskDao(Dao):
    def __init__(self, redis_config, mysql_config):
        # 强制设置监控db
        redis_config = {
            **redis_config, **{'db': constants.REDIS_DB}
        }
        super().__init__(redis_config, mysql_config)

    def store_monitor_info(self, key):
        """存储监控信息"""
        value = self.redis_client.hgetall(key)
        value = {k.decode(): v.decode() for k, v in value.items()}
        value['task_key'] = key
        # 计算平均爬取时间
        value = util.get_avg_crawl_time(value)
        sql = sqls.INSERT + f'on duplicate key update success=values(success), ' \
                            f'failed=values(failed), retry=values(retry), avg_crawl_time=values(avg_crawl_time)'
        self.store(sql, tb_names.TASK_MONITOR, value)

    def sum_by_task(self, date):
        """统计任务维度下的整体统计信息"""
        sql = f'select `bis_name`, `task_name`, sum(`queue_length`) `queue_length`, sum(`left`) `left`, ' \
              f'sum(`success`) `success`, sum(`failed`) `failed`, sum(`retry`) `retry` ' \
              f'from `{tb_names.TASK_MONITOR}` where `version` like "{date}%" ' \
              f'group by `bis_name`, `task_name`'
        return self.get(sql)

    def get_tasks(self, date):
        """获取某日的所有任务"""
        sql = f'select distinct `bis_name`, `task_name` from `{tb_names.TASK_MONITOR}` ' \
              f'where `version` like "{date}%"'
        return self.get(sql)

    def get_task_versions(self, bis_name, task_name, date):
        """获取某日某任务的所有批次"""
        sql = f'select `queue_length`, `left`, `success`, `failed`, `retry`, `avg_crawl_time`, `version` ' \
              f'from `{tb_names.TASK_MONITOR}` ' \
              f'where `bis_name` = "{bis_name}" and `task_name` = "{task_name}" and `version` like "{date}%"'
        return self.get(sql)
