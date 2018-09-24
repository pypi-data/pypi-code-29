import pandas as pd
import numpy as np
from helper import *
from query import *
import math
import configparser
configInstance = configparser.ConfigParser()
configInstance.read('grank.ini')

start_time=configInstance["time"]["start_time"]
end_time=configInstance["time"]["end_time"]

def analytics_repo(owner,repository):
    print("开始抓取数据");
    query = all_query % (owner, repository)
    result = run(query)
    commitArray = []
    pullRequestArray = []
    date_range = pd.date_range(start=start_time,end=end_time,freq="W")
    date_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    """
    进入循环处理
    """
    while has_next_page(result,"commit") or has_next_page(result,"issue") or has_next_page(result,"pr"):
        print("继续抓取数据");
        """
        处理上一个循环中查询到的数据
        """
        if (has_result(result,"commit")):
            for commit in result["data"]["repository"]["ref"]["target"]["history"]["edges"]:
                add_item_to_commit_array(commit,commitArray)
                pass
        if (has_result(result,"pr")):
            for pullRequest in result["data"]["repository"]["pullRequests"]["nodes"]:
                add_item_to_pr_array(pullRequest,pullRequestArray)

        if (has_next_page(result,"pr") and has_next_page(result,"commit")):
            query = all_query_with_pager % (owner,repository,get_page_cursor(result,"pr"),get_page_cursor(result,"commit"))
        elif (has_next_page(result,"pr")):
            query = pr_query_with_pager % (owner,repository,get_page_cursor(result,"pr"))
        elif (has_next_page(result,"commit")):
            query = commit_query_with_pager % (owner,repository,get_page_cursor(result,"commit"))

        """
        进入新的循环
        """
        result = run(query)

    print("开始分析");

    print("分析 PR")
    pr_frame = pd.DataFrame(pullRequestArray);
    # pr_frame.to_pickle("output/prs.pkl")
    pr_frame = pr_frame[pr_frame.date != "未标注时间"]
    pr_frame["date"] = pd.to_datetime(pr_frame['date'])
    pr_dstList = pr_frame.set_index('date').resample('W')['times'].sum()
    pr_dstList = pr_dstList.loc[start_time:end_time]


    print("分析 commit")
    commit_frame = pd.DataFrame(commitArray);
    # commit_frame.to_pickle("output/commits.pkl")
    commit_frame = commit_frame[commit_frame.date != "未标注时间"]
    commit_frame["date"] = pd.to_datetime(commit_frame['date'])
    commit_dstList = commit_frame.set_index('date').resample('W')['times'].sum()
    commit_dstList = commit_dstList.loc[start_time:end_time]

    print("分析 Contributor")
    contributor_frame = pd.DataFrame(commitArray);
    contributor_frame = contributor_frame[contributor_frame.date != "未标注时间"]
    contributor_frame["date"] = pd.to_datetime(contributor_frame['date'])
    contributor_dstList = contributor_frame.drop_duplicates(subset=["author"]).set_index('date').resample('W')['times'].sum()
    contributor_dstList = contributor_dstList.loc[start_time:end_time] # 修改开始时间和结束时间修改这里


    # 为新的 DataFrame 准备数据

    new_commit_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    for item in commit_dstList.index:
        if item in date_series.index:
            new_commit_series[item] = commit_dstList[item]

    new_pr_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    for item in pr_dstList.index:
        if item in date_series.index:
            new_pr_series[item] = pr_dstList[item]

    new_contributor_series = pd.Series(np.zeros((len(date_range),), dtype=int),index=date_range)
    for item in contributor_dstList.index:
        if item in date_series.index:
            new_contributor_series[item] = contributor_dstList[item]

    # 构成新的 DataFrame

    new_df = pd.DataFrame({
        "contributor":new_contributor_series.values,
        "commit":new_commit_series.values,
        "pr":new_pr_series.values
    },index = date_range)

    # 计算活跃分数

    new_df["score"] = new_df.apply(lambda row: math.sqrt(row.pr*row.pr + row.contributor * row.contributor + row.commit*row.commit), axis=1)

    # 求活跃分数平均值

    target_score = new_df["score"].sum() / len(new_df)

    # 获取平均分实例，用于后续排序

    instance = get_avarage_instance()

    # 将项目的活跃分数保存到新的 Pickle 中，用于后续的折线图输出

    series_to_pickle(new_df,repository)

    # 对平均分实例进行排序

    set_avarage(instance,repository,target_score)

    # 输出项目的 CSV 数据
    export_csv(new_df,"%s" % repository)

    # 生成折线图

    generate_line_number()

    print("输出成功,%s 旗下的 %s 项目的活跃分数为 %.15f"% (owner,repository,target_score))
    print("排行榜及折线图请查看 result 目录")
