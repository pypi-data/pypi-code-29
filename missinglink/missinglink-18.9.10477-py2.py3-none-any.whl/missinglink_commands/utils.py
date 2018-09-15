# -*- coding: utf8 -*-
from missinglink_commands.legit.api import ApiCaller


def monitor_logs(ctx, url, disable_colors):
    from missinglink_commands.sse_firebase import LogsThread

    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', url)

    logs_thread = LogsThread(ctx.obj.config, result['url'], disable_colors)
    logs_thread.start()
    logs_thread.join()
