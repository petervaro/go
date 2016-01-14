#!/usr/bin/env python3
## INFO ##
## INFO ##

# Import python modules
from os.path import join

# Module level constants
CURRENT_DIR = '.'
LANG_PATH   = join(CURRENT_DIR, 'langs')

# Import tmtools modules
try:
    from tmtools.convert import Language, Theme
except ImportError:
    from sys import exit
    print('[ ERROR ] tmtools modules are missing: '
          'install it from http://github.com/petervaro/tmtools')
    exit(-1)

#------------------------------------------------------------------------------#
# Import user modules
from src.go import syntax

# I/O Details of languages and themes
go = {'name' : 'Go',
      'path' : LANG_PATH,
      'scope': 'go',
      'comments' : {'lines': '//', 'blocks': ('/*', '*/')},
      'test_name': 'Go_TEST',
      'test_path': '~/.config/sublime-text-3/Packages/User/Go_TEST'}

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Setup names and locations
lang = Language(**go)
# Convert and save language file
lang.from_dict(syntax)
lang.write()
