class BaseRule(object):
    def __init__(self, build_context, dir_path):
        self.build_context = build_context
        self.dir_path = dir_path
