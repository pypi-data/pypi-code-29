import json
import os.path
import re
import ipykernel
import requests
from git import git_root
from IPython import get_ipython

from requests.compat import urljoin

try:  # Python 3
    from notebook.notebookapp import list_running_servers
except ImportError:  # Python 2
    import warnings
    from IPython.utils.shimmodule import ShimWarning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ShimWarning)
        from IPython.html.notebookapp import list_running_servers


def has_ipynb_shell():
    """Check if IPython shell is available"""
    try:
        cls = get_ipython().__class__.__name__
        return cls == 'ZMQInteractiveShell'
    except NameError:
        return False


def in_notebook():
    """Check if this code is being executed in a notebook"""
    if not has_ipynb_shell():
        return False
    from ipykernel.kernelapp import IPKernelApp
    return IPKernelApp.initialized()


def get_notebook_server_path():
    """Return the path of the notebook relative to the Jupyter server"""
    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)
    servers = list_running_servers()
    for ss in servers:
        response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                params={'token': ss.get('token', '')})
        for nn in json.loads(response.text):
            if nn['kernel']['id'] == kernel_id:
                relative_path = nn['notebook']['path']
                return relative_path


def get_notebook_path():
    """
    Return the full path of the jupyter notebook.
    """
    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)
    servers = list_running_servers()
    for ss in servers:
        response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                params={'token': ss.get('token', '')})
        for nn in json.loads(response.text):
            if nn['kernel']['id'] == kernel_id:
                relative_path = nn['notebook']['path']
                return os.path.join(ss['notebook_dir'], relative_path)


def get_notebook_git_path():
    """Return the path of the notebook relative the git root"""
    return get_notebook_path().replace(git_root(), "")[1:]


def get_notebook_name():
    """Return the name of the notebook"""
    return get_notebook_path().split('/')[-1]


def get_notebook_history():
    """Return full code history of notebook"""
    return get_ipython().magic('%history')


def save_notebook():
    """Save the current Jupyter notebook"""
    return get_ipython().run_cell_magic('javascript', '', 'require(["base/js/namespace"],function(Jupyter){Jupyter.notebook.save_checkpoint()})')
