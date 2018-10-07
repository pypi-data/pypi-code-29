import fire


class GitTask:
    """Git-task is a task management system"""

    @staticmethod
    def add():
        print("add")

    @staticmethod
    def remove():
        """Removes one todo item"""
        print("remove")


if __name__ == '__main__':
    fire.Fire(GitTask)
