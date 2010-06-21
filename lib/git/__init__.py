# __init__.py
# Copyright (C) 2008, 2009 Michael Trier (mtrier@gmail.com) and contributors
#
# This module is part of GitPython and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

import os
import sys
import inspect

__version__ = 'git'


#{ Initialization
def _init_externals():
	"""Initialize external projects by putting them into the path"""
	sys.path.append(os.path.join(os.path.dirname(__file__), 'ext'))
	
#} END initialization

#################
_init_externals()
#################

#{ Imports

from git.config import GitConfigParser
from git.objects import *
from git.refs import *
from git.diff import *
from git.errors import *
from git.cmd import Git
from git.repo import Repo
from git.remote import *
from git.index import *
from git.utils import (
						LockFile, 
						BlockingLockFile, 
						Stats
						)

#} END imports

__all__ = [ name for name, obj in locals().items()
			if not (name.startswith('_') or inspect.ismodule(obj)) ]
			
