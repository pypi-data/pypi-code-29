import json


class Json(object):
    LINE_COMMENT = "//"
    BLOCK_COMMENT_START = "/*"
    BLOCK_COMMENT_END = "*/"

    @classmethod
    def load(cls, path):
        with open(path) as file:
            result = json.load(file)
        return result

    @classmethod
    def save(cls, data, path):
        with open(path) as file:
            json.dump(data, file)

    @classmethod
    def encode(cls, data):
        return json.dumps(data)

    @classmethod
    def decode(cls, data):
        return json.loads(data)

    def lint(self, compatibility=False):
        # TODO implement lint function locally
        pass

    def _pre_process(self):
        # TODO remove comment after load()
        pass

    def _post_process(self):
        # TODO restore comment before save()
        pass
