# -*- coding: utf-8 -*-
""" Alumia Framework | Alumia Core Library """

import configparser

__name__ = "Keyper"
__version__ = "1.0.0"
__author__ = "OpSec WareHouse LLC"
__author_email__ = "team@opsec.sh"
__copyright__ = "Copyright (c) 2022 OpSec WareHouse LLC"

__verbose__ = False

__database__ = "data/keyring.dat"

from .MainCore import MainCore
from .DataCore import DataCore
from .GUICore import GUICore
from .UtilCore import UtilCore
