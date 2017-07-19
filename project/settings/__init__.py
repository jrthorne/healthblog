from  settings.base import *

try:
    from settings.local import *
except ImportError:
    print('Could not import local.py settings')