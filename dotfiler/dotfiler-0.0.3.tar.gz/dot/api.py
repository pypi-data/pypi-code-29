# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List, Optional

from .config import DotfileConfig
from .topic import Topic


def _always_true(topic: Topic) -> bool:
    return True


def _is_enabled(topic: Topic) -> bool:
    return topic.enabled


def _is_disabled(topic: Topic) -> bool:
    return not topic.enabled


predicates = {
    True: _is_enabled,
    False: _is_disabled,
}


def list_topics(
    config: DotfileConfig,
    enabled: Optional[bool] = None,
) -> List[Topic]:
    """Return a list of Topic objects."""
    predicate = predicates.get(enabled, _always_true)

    return [topic for topic in config.topics if predicate(topic)]


def _create_dot_symlink_in_dir(source: Path, target: Path, overwrite: bool = False):
    dot_link = target.joinpath('.' + source.stem)

    if overwrite and dot_link.exists():
        backup = target.joinpath(dot_link.name + '.bak')
        dot_link.rename(backup)

    print(f'[LINKING] "{source}" -> "{dot_link}"')

    dot_link.symlink_to(source)


def link_topic(
    topic: Topic,
    overwrite: bool = False,
):
    """Symlink necessary files from the Topic into user's home directory."""
    home = Path.home()
    for symlink in topic.symlinks:
        _create_dot_symlink_in_dir(source=symlink, target=home, overwrite=overwrite)
