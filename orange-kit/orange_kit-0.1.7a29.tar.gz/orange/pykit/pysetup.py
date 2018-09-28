# 项目：工具函数库
# 模块：python模块
# 作者：黄涛
# License:GPL
# Email:huangtao.sh@icloud.com
# 创建：2018-09-28 21:52

from orange.shell import Path, sh, POSIX, HOME

libpath = HOME/'OneDrive/pylib'


def run_cmd(cmd: str, *args, **kw)->int:
    return sh(cmd, *args, capture_output=False, **kw)


def pysetup(*args)->int:
    if not Path('setup.py'):
        print('Can''t find file setup.py!')
        exit(1)
    cmd = 'python3 setup.py' if POSIX else 'setup'
    return run_cmd(cmd, *args)


def pip(*args)->int:
    return run_cmd('pip3', *args)


def pyupload():
    pysetup('sdist', '--dist-dir', libpath, 'upload')
    pyclean()


def pysdist():
    pysetup('sdist', '--dist-dir', libpath)
    pyclean()


def pyclean():
    for path in ('build', 'dist', '*egg-info'):
        for p in Path('.').glob(path):
            p.rmtree()
            print(f'Path {p} have been deleted!')


def py_setup():
    pysetup('install')
    pyclean()


if __name__ == '__main__':
    py_setup()
