# cli/commands/backup.py

from .base import Base


class Backup(Base):

    def run(self):
        print('Executing backup script...')
        print('done')
