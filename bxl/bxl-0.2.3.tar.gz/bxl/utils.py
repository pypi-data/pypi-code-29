import json
import xnat

def setup_xnat(config_file):
    ''' Setup an XNAT instance given a valid configuration file'''
    config = json.load(open(config_file))
    hostname = config['server']

    if config.get('certificate_verify'):
        verify_ssl_context = config['certificate_verify']
    else :
        verify_ssl_context = False

    if config.get('jsession_id') :
        credentials = config.get('jsession_id')
    elif config.get('password') and config.get('user') :
        credentials = (config['user'],config['password'])
    else:
        credentials = None

    return xnat.Connection(hostname, credentials, verify=verify_ssl_context)

# def __md5__(fname):
#     import hashlib
#     hash_md5 = hashlib.md5()
#     if fname.endswith('.pyc'):
#         fname = fname[:-1]
#     with open(fname, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()
#
# def __is_valid_scan__(scan_dict) :
#     ''' Helper gathers all rules for XNAT scan suitability '''
#     valid = False
#     if scan_dict['ID'].isdigit() \
#             and not scan_dict['ID'].startswith('0') \
#             and scan_dict['quality'] == 'usable' \
#             and scan_dict['xsiType'] == 'xnat:mrScanData' :
#         valid = True
#     return valid