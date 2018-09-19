cache_folder = '/tmp/cache'


def hashkey(*args):
    import json
    dump = json.dumps(args, sort_keys=True)

    import hashlib
    hash = hashlib.sha224(dump.encode()).hexdigest()

    return hash


def exists(*args):
    hs = hashkey(*args)
    filename = "%s/%s" % (cache_folder, hs)
    import os.path
    if os.path.exists(filename):
        return True
    else:
        return False


def load(args):
    hs = hashkey(*args)
    filename = "%s/%s" % (cache_folder, hs)
    import json
    return json.loads('\n'.join(list(open(filename))))


def save(value, *args):
    def json_datetime(o):
        import datetime
        if isinstance(o, datetime.datetime):
            return o.__str__()

    hs = hashkey(*args)
    filename = "%s/%s" % (cache_folder, hs)
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(value, default=json_datetime))


def clean_cache():
    import shutil
    import os
    if os.path.exists(cache_folder):
        shutil.rmtree(cache_folder)
    os.makedirs(cache_folder)


def caching(fn, *args):
    if exists(*args):
        results = load(args)
    else:
        results = fn(*args)
        save(results, *args)

    return results
