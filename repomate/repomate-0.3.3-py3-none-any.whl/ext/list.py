from pathlib import Path
from repomate_plug import Plugin, HookResult, Status


class List(Plugin):
    def act_on_cloned_repo(self, path, api):
        path = Path(path)
        files = (file for file in path.rglob('*') if '.git' not in str(file))
        msg = '\n'.join(map(str, files))

        api.open_issue(title='These are your files', body=msg, repo_names=[path.name])

        return HookResult('list', Status.SUCCESS, msg)
