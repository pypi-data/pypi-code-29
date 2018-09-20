# Copyright (c) Microsoft Corporation. All rights reserved.
import copy
import distro
import glob
import os
import re
import shutil
import subprocess
import sys
from typing import List, Optional


__version__ = '2.1.0'   # {major dotnet version}.{minor dotnet version}.{revision}
# We can rev the revision due to patch-level change in .net or changes in dependencies
missing_dep_re = re.compile(r'^(.+)\s*=>\s*not found\s*$', re.MULTILINE)


ubuntu_mappings = {
    'libunwind-x86_64.so.8': 'libunwind8=1.1-4.1',
    'libunwind.so.8': 'libunwind8=1.1-4.1',
    'liblttng-ust.so.0': 'liblttng-ust0=2.7.1-1',
    'libcurl.so.4': 'libcurl3=7.47.0-1ubuntu2',
    'liburcu-bp.so.4': 'liburcu4=0.9.1-3',
    'liburcu-cds.so.4': 'liburcu4=0.9.1-3'
}


distro = distro.linux_distribution(full_distribution_name=False)[0] if sys.platform == 'linux' else None


def _get_mappings():
    if distro == 'ubuntu':
        return ubuntu_mappings
    else:
        raise ValueError('Unsupported Linux distribution')


def _get_dependency_name(dependency: str) -> str:
    dep_mappings = _get_mappings()
    if dependency not in dep_mappings:
        raise ValueError('Required dependency missing: ' + dependency)

    return dep_mappings[dependency]


def _gather_dependencies(path: str, search_path: str=None) -> List[str]:
    libraries = glob.glob(os.path.realpath(os.path.join(path, '**', '*.so')), recursive=True)
    missing_deps = set()
    env = copy.copy(os.environ)
    if search_path is not None:
        env['LD_LIBRARY_PATH'] = search_path
    for library in libraries:
        ldd_output = subprocess.run(['ldd', library], cwd=path, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
        matches = missing_dep_re.findall(ldd_output)
        missing_deps |= set(_get_dependency_name(dep.strip()) for dep in matches)

    return [d for d in missing_deps]


def _install_dependency(dependency: str, target_path: str):
    download_folder = os.path.join(_get_pkg_download_folder(), dependency)
    os.makedirs(download_folder, exist_ok=True)
    subprocess.run(['apt-get', 'download', dependency], cwd=download_folder)
    subprocess.run(['ar', 'x', glob.glob(os.path.join(download_folder, '*.deb'))[0]], cwd=download_folder)
    subprocess.run(['tar', 'xf', 'data.tar.xz'], cwd=download_folder)
    lib_files = glob.glob(os.path.join(download_folder, '**', '*.so*'), recursive=True)
    for file in lib_files:
        shutil.copy(file, target_path)


def _get_pkg_download_folder() -> str:
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bin', 'tmp')


def _get_bin_folder() -> str:
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bin')


def ensure_dependencies() -> Optional[str]:
    if distro is None:
        return None

    bin_folder = _get_bin_folder()
    deps_path = os.path.join(bin_folder, 'deps')
    success_file = os.path.join(deps_path, 'SUCCESS-' + __version__)
    if os.path.exists(success_file):
        return deps_path

    os.makedirs(deps_path, exist_ok=True)
    while True:
        missing_deps = _gather_dependencies(bin_folder, search_path=deps_path)
        if not missing_deps:
            break

        for dep in missing_deps:
            _install_dependency(dep, deps_path)

    shutil.rmtree(_get_pkg_download_folder(), ignore_errors=True)
    with open(success_file, 'a'):
        os.utime(success_file, None)
    return deps_path


def get_runtime_path():
    search_string = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bin', 'dotnet*')
    matches = [f for f in glob.glob(search_string, recursive=True)]
    return matches[0]
