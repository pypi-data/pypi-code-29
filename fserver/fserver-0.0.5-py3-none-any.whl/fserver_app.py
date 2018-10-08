from flask import Flask
from flask import render_template, request
from flask import make_response, send_from_directory, send_file
import os
import urllib
import posixpath
import mimetypes
import sys, getopt

from fserver.util import debug

VIDEO_SUFFIX = ['mp4', 'flv', 'hls', 'dash']
CDN_JS = {
    'flv': 'https://cdnjs.cloudflare.com/ajax/libs/flv.js/1.4.2/flv.min.js',
    'hls': 'https://cdn.jsdelivr.net/npm/hls.js@latest',
    'dash': 'https://cdnjs.cloudflare.com/ajax/libs/dashjs/2.9.1/dash.all.min.js',
    'mp4': ''
}

app = Flask(__name__, template_folder='templates')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_ls(path):
    debug('get_ls: ', path, [a for a in request.args.values()])
    mod = request.args.get('m', '')
    moda = ''
    if mod != '':
        moda = '?m=' + mod
    local_path = translate_path(path)
    if os.path.isdir(local_path):  # 目录
        lst = os.listdir(local_path)
        for i, l in enumerate(lst):
            if os.path.isdir('/'.join([local_path, l])):
                lst[i] += '/'
        return render_template('list.html',
                               path=path,
                               arg=moda,
                               list=lst)
    elif os.path.exists(local_path):  # 非目录
        try:
            suffix = get_suffix(path)

            if mod == 'dv':  # down video
                return respond_video(path)
            elif suffix in VIDEO_SUFFIX or mod == 'p':  # 播放视频
                return play_video(path)
            else:  # mod = 'd' # down file
                return respond_file(path)
        except Exception as e:
            return render_template('error.html', error=e)

    return render_template('error.html', error='No such dir or file: ' + path)


def respond_file(path):
    debug('respond_file:', path)
    if os.path.isdir(path):
        return get_ls(path)
    local_path = translate_path(path)
    type = mimetypes.guess_type(local_path)[0]
    return send_file(local_path, mimetype=type)


def respond_video(path):
    debug('respond_video:', path)
    local_path = translate_path(path)
    if os.path.isdir(local_path):  # 重定向
        return get_ls(path)

    filename = get_filename(path)
    ppath = get_parent_path(local_path)
    response = make_response(send_from_directory(ppath, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response


def play_video(path):
    debug('play_video:', path)
    if os.path.isdir(translate_path(path)):
        return get_ls(path)

    t = request.args.get('t')
    suffix = get_suffix(path)
    if suffix in VIDEO_SUFFIX:
        t = suffix
    elif t is None or t == '':
        t = 'auto'
    try:
        tj = CDN_JS[t]
        tjs = []
    except:
        tj = ''
        tjs = CDN_JS.values()
    return render_template('video.html',
                           name=get_filename(path),
                           url='/' + path + '?m=dv',
                           type=t,
                           typejs=tj,
                           typejss=tjs)


def get_filename(path):
    try:
        return path[path.rindex('/') + 1:]
    except:
        try:
            return path[path.rindex('\\') + 1:]
        except:
            return path


def get_parent_path(path):
    try:
        filename = get_filename(path)
        return path[:path.rindex(filename)]
    except:
        return ''


def get_suffix(path):
    try:
        return path[path.rindex('.') + 1:]
    except:
        return ''


def translate_path(path):
    """Translate a /-separated PATH to the local filename syntax.

    Components that mean special things to the local file system
    (e.g. drive or directory names) are ignored.  (XXX They should
    probably be diagnosed.)

    """
    # abandon query parameters
    path = path.split('?', 1)[0]
    path = path.split('#', 1)[0]
    # Don't forget explicit trailing slash when normalizing. Issue17324
    trailing_slash = path.rstrip().endswith('/')
    try:
        path = urllib.parse.unquote(path, errors='surrogatepass')
    except UnicodeDecodeError:
        path = urllib.parse.unquote(path)
    path = posixpath.normpath(path)
    words = path.split('/')
    words = filter(None, words)
    path = os.getcwd()
    for word in words:
        if os.path.dirname(word) or word in (os.curdir, os.pardir):
            # Ignore components that are not a simple file/directory name
            continue
        path = os.path.join(path, word)
    if trailing_slash:
        path += '/'
    return path


def main():
    port = 2000
    help_str = '''usage: python fserver_app.py [-h] [port]

  positional arguments:
    port                  Specify alternate port [default: 2000]

  optional arguments:
    -h, --help            show this help message and exit

  arguments of url:
    m                     get_arg to set the mode of processing method of file
                          Such as http://localhost:port?m=dv to download the file specified by url
                          value 'p' to play file with Dplayer
                          value 'v' to show the file specified by url
                          value 'dv' to download the file specified by url
 '''

    try:
        options, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError as e:
        print('error:', e.msg)
        print(help_str)
        sys.exit()

    if len(args) > 0:
        port = args[0]
        if not port.isdigit():
            print('error: port must be int, input:', port)
            sys.exit()

    for name, value in options:
        if name in ['-h', '--help']:
            print(help_str)
            sys.exit()

    app.run(
        host='0.0.0.0',
        port=port,
    )


if __name__ == '__main__':
    main()
