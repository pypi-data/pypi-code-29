import json
import requests


pm25_level = {
    '优质': '一级',
    '良好': '二级',
    '轻度污染': '三级',
    '中度污染': '四级',
    '重度污染': '五级',
    '严重污染': '六级'
}

pm25_affect = {
    '优质': '空气质量令人满意，基本无空气污染',
    '良好': '空气质量可接受，但某些污染物可能对极少异常敏感人群健康有较弱影响',
    '轻度污染': '易感人群症状有轻度加剧，健康人群出现刺激症状',
    '中度污染': '进一步加剧易感人群症状，可能对健康人群心脏、呼吸系统有影响',
    '重度污染': '心脏病和肺病患者症状显著加剧，运动耐受力降低，健康人群普通出现症状',
    '严重污染': '健康人群运动耐受力降低，有明显强烈症状，提起出现某些疾病'
}

pm25_advise = {
    '优质': '各类人群可正常活动',
    '良好': '极少异常敏感人群减少户外活动',
    '轻度污染': '儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼',
    '中度污染': '儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼，一般人群适量减少户外运动',
    '重度污染': '儿童、老年人和心脏病、肺病患者应停留在室内，停止户外运动，一般人群适量减少户外运动',
    '严重污染': '儿童、老年人和病人应停留在室内，避免体力消耗，一般人群应避免户外运动'
}


def pm25(city=''):
    if city == '':
        return -1
    url='https://ali-pm25.showapi.com/pm25-detail?city=' +  city

    appcode = '6f84ed50805f4b4982d17f1ae00563e1'
    headers = {
        'Authorization': 'APPCODE ' + appcode,
    }

    r = requests.get(url, headers=headers)
    res = r.json()['showapi_res_body']
    if res:
        pm = res['pm']
        res_dict = {}
        res_dict['city']=city
        res_dict['pm25']=pm['pm2_5']
        res_dict['quality']=pm['quality']
        res_dict['level']=pm25_level.get(pm['quality'])
        res_dict['affect']=pm25_affect.get(pm['quality'])
        res_dict['advise']=pm25_advise.get(pm['quality'])

        if res_dict['quality'] == '优质':
            res_dict['quality'] = '优'

        if res_dict['quality'] == '良好':
            res_dict['quality'] = '良'

        position = res['siteList']
        res_dict['position'] = []
        for val in position:
            pos_list = {}
            pos_list['posname'] = val['site_name']
            pos_list['pm25'] = val['pm2_5']
            pos_list['quality'] = val['quality']
            if pos_list['quality'] == '优质':
                pos_list['quality'] = '优'

            if pos_list['quality'] == '良好':
                pos_list['quality'] = '良'
            res_dict['position'].append(pos_list)
        return res_dict
    else:
        return -1


def main():
    print(pm25('北京'))

if __name__ == '__main__':
    main()
