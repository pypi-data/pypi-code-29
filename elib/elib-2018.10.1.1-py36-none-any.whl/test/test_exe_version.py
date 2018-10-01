# coding=utf-8

from pathlib import Path

import pytest

from elib import exe_version

HERE = Path('.').absolute()


def test_exe_version():
    version = exe_version.get_product_version(HERE.joinpath('test/test_files/version_ok.exe'))
    assert isinstance(version, exe_version.VersionInfo)
    assert version.file_version == '0.1.0'
    assert version.full_version == 'some+very-special.version'
    assert str(version) == '0.1.0'


def test_exe_no_version():
    with pytest.raises(RuntimeError):
        exe_version.get_product_version(HERE.joinpath('test/test_files/no_version.exe'))


def test_exe_missing_attrib():
    with pytest.raises(RuntimeError):
        exe_version.get_product_version(HERE.joinpath('test/test_files/missing_attrib.exe'))
