import logging
import sys
import json
from pathlib import Path
from datetime import datetime
from git import Repo, TagReference
from zensols.pybuild import Version

logger = logging.getLogger('zensols.zenpybuild.tag')


class TagUtil(object):
    """Git tag helper"""
    def __init__(self, repo_dir='.', message='none', dry_run=False):
        logger.debug('creating witih repo dir: {}'.format(repo_dir))
        if isinstance(repo_dir, Path):
            repo_dir = str(repo_dir.resolve())
        self.repo = Repo(repo_dir)
        assert not self.repo.bare
        self.message = message
        self.dry_run = dry_run

    def get_entries(self):
        tags = self.repo.tags
        logger.debug('tags: {}'.format(tags))
        tag_entries = []
        for tag in tags:
            logger.debug('{} ({})'.format(tag, type(tag)))
            name = str(tag)
            ver = Version.from_string(name)
            date = None
            if hasattr(tag.object, 'tagged_date'):
                date = tag.object.tagged_date
            if ver is not None:
                tag_entries.append({'name': name,
                                    'ver': ver,
                                    'date': date,
                                    'tag': tag,
                                    'message': tag.object.message})
        tag_entries = sorted(tag_entries, key=lambda t: t['ver'])
        return tag_entries

    def last_tag_entry(self):
        entries = self.get_entries()
        logger.debug('entires: {}'.format(entries))
        if (len(entries) > 0):
            return entries[-1]

    def get_last_tag(self):
        entry = self.last_tag_entry()
        if entry:
            return entry['ver'].format(prefix='')

    def print_last_tag(self):
        last_tag = self.get_last_tag()
        if last_tag:
            print(last_tag)

    def get_last_commit(self):
        commits = list(self.repo.iter_commits('HEAD'))
        if len(commits) > 0:
            return commits[0]

    def get_info(self):
        inf = {'build_date': datetime.now().isoformat()}
        last_entry = self.last_tag_entry()
        if last_entry:
            tag = last_entry['tag']
            message = None
            if hasattr(tag.object, 'message'):
                message = tag.object.message
            inf.update({'tag': last_entry['ver'].format(prefix=''),
                        'name': last_entry['name'],
                        'message': message})
        c = self.get_last_commit()
        if c:
            inf['commit'] = {'author': str(c.author),
                             'date': c.committed_datetime.isoformat(),
                             'sha': str(c),
                             'summary': c.summary}
        return inf

    def dump_info(self, writer=sys.stdout):
        json.dump(self.get_info(), writer, indent=2)

    def delete_last_tag(self):
        entry = self.last_tag_entry()
        tag = entry['tag']
        name = entry['name']
        logger.info('deleting: {}'.format(name))
        if not self.dry_run:
            TagReference.delete(self.repo, tag)

    def recreate_last_tag(self):
        entry = self.last_tag_entry()
        tag = entry['tag']
        name = entry['name']
        msg = entry['message']
        logger.info('deleting: {}'.format(name))
        if not self.dry_run:
            TagReference.delete(self.repo, tag)
        logger.info('creating {} with commit <{}>'.format(name, msg))
        if not self.dry_run:
            TagReference.create(self.repo, name, message=msg)

    def create(self):
        entry = self.last_tag_entry()
        if entry is None:
            ver = Version.from_string('v0.0.0')
        else:
            ver = entry['ver']
        ver.increment('debug')
        new_tag_name = str(ver)
        logger.info('creating {} with commit <{}>'.format(
            new_tag_name, self.message))
        if not self.dry_run:
            TagReference.create(self.repo, new_tag_name, message=self.message)
