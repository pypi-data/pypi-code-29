"""
A bunch of the non-interface libraries go in this module.
This also separates the test modules from the production modules.
Other modules should import everything from here.
"""

import sys

from .. import opts


# A list of functions and modules that should
# be accessible through the backend
_PROVIDE = [
    'inventory',             # Contents of sites
    'registry',              # Submit transfers and deletions here
    'siteinfo',              # Site information from inventory
    'get_listers',           # Get remote listers for a site
    'check_site',            # A function that determines if site is ready to run
    'deletion_requests',     # Deletion requests in proper dataset format
    'filelist_to_blocklist', # Converts a file of list of files to a summary of blocks
    'DatasetFilter'          # A filter class that identifies files by dataset
    ]


if opts.TEST:
    from . import test as mod

else:
    from . import prod as mod


_THIS = sys.modules[__name__]

for thing in _PROVIDE:
    setattr(_THIS, thing, getattr(mod, thing))
