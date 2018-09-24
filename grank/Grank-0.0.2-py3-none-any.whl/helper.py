import requests
import configparser
import os.path
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

configInstance = configparser.ConfigParser()
configInstance.read('grank.ini')
if "time" in configInstance.sections():
    start_time=configInstance["time"]["start_time"]
    end_time=configInstance["time"]["end_time"]
    top_number=int(configInstance["rank"]["top"])

"""
封装的 GraphQL 的请求方法，可以执行 GraphQL
"""
def run(query):
    headers = {"Authorization": "Bearer %s" % configInstance["login"]["token"]}
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


"""
判断是否有下一页的函数
"""
def has_next_page(result,mode):

    if mode == "pr":
        if (has_result(result,"pr")):
            if result["data"]["repository"]["pullRequests"]["pageInfo"]["hasNextPage"]:
                return True
            else:
                return False
        else:
            return False

    if mode == "commit":
        if (has_result(result,"commit")):
            if result["data"]["repository"]["ref"]['target']["history"]["pageInfo"]["hasNextPage"]:
                return True
            else:
                return False
        else:
            return False

"""
获取下一页指针的函数
"""
def get_page_cursor(result,mode):
    if mode == "pr":
        return result["data"]["repository"]["pullRequests"]["pageInfo"]["endCursor"]

    if mode == "commit":
        return result["data"]["repository"]["ref"]['target']["history"]["pageInfo"]["endCursor"]

"""
判断是否有对应的结果
"""
def has_result(result,mode):
    if mode == "pr":
        return ("pullRequests" in result["data"]["repository"])
    elif mode == "commit":
        return ("ref" in result["data"]["repository"])

"""
时间的简化处理
"""
def cover_time(time):
    if time :
        return time[0:10]
    else:
        return "未标注时间"

"""
添加项目到 commit 数组中
"""
def add_item_to_commit_array(item,blank_array):
    blank_array.append({
            'author' : item["node"]["author"]["email"],
            'date': cover_time(item["node"]["pushedDate"]),
            "times":1
        })

"""
添加项目到 PR 数组中
"""
def add_item_to_pr_array(item,blank_array):
    blank_array.append({
      "date":cover_time(item["publishedAt"]),
      "times":1
    })

"""
导出 CSV
"""
def export_csv(series,name):
    series.to_csv("output/%s.csv" % name);
    print("导出 CSV 成功:output/%s.csv" % name);

"""
获取平均值 DF 实例
"""
def get_avarage_instance():
    if not os.path.isfile("output/average.pkl"):
        pd.DataFrame(data={'name': [], 'score': []}).to_pickle("output/average.pkl")
    return pd.read_pickle("output/average.pkl")

"""
保存中间值，并更新 csv 文件
"""
def set_avarage(instance,repository,score):
    instance = instance.append(pd.Series({"name":repository,"score":score}),ignore_index=True)
    instance = instance.drop_duplicates(subset=["name"]).sort_values(["score"],ascending=False)
    instance.to_pickle("output/average.pkl")
    instance.to_csv("result/project_rank.csv")

"""
Series to Pickle
"""
def series_to_pickle(df,name):
    df.to_pickle("output/%s.pkl" % name)

"""
生成数据折线图
"""
def generate_line_number():
    df = pd.read_pickle("output/average.pkl")
    all_df = pd.DataFrame(data=[],index=pd.date_range(start=start_time,end=end_time,freq="W"))

    for index, row in df.iterrows():
        if len(all_df.columns) < top_number:
            all_df[row["name"]] = pd.read_pickle("output/%s.pkl" % row["name"])["score"]
        else:
            break
    all_df.plot().get_figure().savefig("result/line.png")

"""
判断用户是否登录
"""
def is_login():
    if not 'login' in configInstance.sections():
        click.echo("You should login first")
        return False
    else:
        return True