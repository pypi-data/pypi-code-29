import collections
import io
import sysconfig

from imd_handler.imd_handler import edit_imd
from imd_handler.imd_handler import put_imd
from imd_handler.imd_handler import read_imd
from imd_handler.imd_handler import write_imd


# expects a dictionary in the event
# file_uri: <uri of imd>
# edits: <dictionary of IMD parameters to be applied
def imd_diddler(event, context):
    imd_to_edit = event['file_uri']
    edit_thing = event['edit']
    print('File to edit: ' + imd_to_edit)
    print('Edit Specifier: ')
    print(type(edit_thing))
    print('Reading IMD')
    imd_dict = read_imd(imd_to_edit)
    print('Parsing edit dictionary' + str(imd_dict))
    edit_dict = collections.OrderedDict(edit_thing)  # json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(edit_thing)
    print('Editing file with:' + str(type(edit_dict)) + " Contents: " + str(edit_dict))
    imd_dict = edit_imd(imd_dict, edit_dict)
    print("Dictionary after editing: " + str(imd_dict))
    imd_buffer = io.StringIO()
    print('Buffering output')
    write_imd(imd_buffer, imd_dict, False)
    print('Putting edited IMD file back')
    put_imd(imd_to_edit, imd_buffer)
    return {'message': 'Success'}


def env_dumper(event, context):
    env_dict = {'python_version': sysconfig.get_python_version(), 'config_vars': sysconfig.get_config_vars(), 'paths': sysconfig.get_paths(expand=True)}
    print(sysconfig.get_python_version() + ' ' + sysconfig.get_platform())
    print(sysconfig.get_config_vars())
    print(sysconfig.get_paths(expand=True))
    return env_dict
