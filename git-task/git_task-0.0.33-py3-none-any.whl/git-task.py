import fire

class GitTask():
    """Git-task is a task management system"""
    def add(self):
        print("add")

    def remove(self):
        """Removes one todo item"""
        print("remove")


fire.Fire(GitTask)
