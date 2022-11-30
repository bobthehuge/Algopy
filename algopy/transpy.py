# -*- coding: utf-8 -*-
"""
Created on Jul. 2022
@author: BobTheHuge

Import your python files with their absolute path.
"""

import importlib.util
import sys


def import_file(module_name, module_path):

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)

    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module
