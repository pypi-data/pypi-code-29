from prompt_toolkit.completion import WordCompleter

cmds = {
        'keys': 'pattern',
        'get': 'key',
        'set': 'key value [EX seconds] [PX milliseconds] [NX|XX]',
        }

redis_completer = WordCompleter(cmds.keys(), meta_dict=cmds, ignore_case=True)
