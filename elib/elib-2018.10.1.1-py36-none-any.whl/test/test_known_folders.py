# coding=utf-8

import os

import pytest

from elib import known_folders


def test_current_user_class():
    """
    This test will fail if the user has set a custom saved games dir
    """
    raw = known_folders.get_path(
        getattr(known_folders.FolderId, 'SavedGames'),
        getattr(known_folders.UserHandle, 'current')
    )
    assert known_folders.CurrentUser.saved_games() == raw
    assert known_folders.CurrentUser.saved_games().lower() == rf'c:\users\{os.getlogin()}\Saved Games'.lower()


def test_path_not_found():
    with pytest.raises(known_folders.PathNotFoundException):
        known_folders.get_path(
            getattr(known_folders.FolderId, 'SkyDriveCameraRoll'),
        )
