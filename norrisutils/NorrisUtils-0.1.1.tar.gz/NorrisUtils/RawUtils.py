# 提取Raw信息中的dict  默认为,分割 =为key value
def extractRawDict(src, dict, splitSymbol=',', splitSymbol2='='):
    items = src.split(splitSymbol)
    for kv in items:
        split = kv.split(splitSymbol2)
        if len(split) == 2:
            if dict.get(split[0], -1) == -1:
                dict[split[0]] = split[1]
            else:
                pass
        else:
            pass
    return dict
