# -*- coding: utf-8 -*-
r"""Test for foo.py

This outputs:

  - test results to value of variable "test_dir"

This depends on:

  - source files written from the value of "source_dir"

Examples of usage:

  - default usage:

        python -m pytest test_foo.py

descriptions:
    every function is a separate test, combined usage with pytest module
""" 


import os
# import pytest
# import filecmp  # for compare file contents
import numpy as np
# import shilofue.Foo as Foo  # import test module
from python_scripts.Utilities import JSON_OPT, show_all_options
# from shilofue.Utilities import 
# from matplotlib import pyplot as plt
# from shutil import rmtree  # for remove directories

test_dir = ".test"
source_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'test_json_opt')

if not os.path.isdir(test_dir):
    # check we have the directory to store test result
    os.mkdir(test_dir)

def test_json_opt():
    '''
    test the JSON_OPT class
    Define the options of one type of json file and read in examples
    Asserts:
    '''
    # assert something
    json_path = os.path.join(source_dir, 'test.json') 
    json_opt = JSON_OPT()
    json_opt.read_json(json_path)
    assert(True)
    
    
def test_show_all_options():
    '''
    test the show_all_options function
    Define the options of one type of json file and read in examples
    '''
    json_path = os.path.join(source_dir, 'test.json') 
    all_options = show_all_options(json_path)
    assert(all_options == \
        [['dirs'], ['py_format'], ['visit'], ['visit', 'slab'], ['visit', 'slab', 'steps'],\
            ['visit', 'slab', 'deform_mechanism'], ['docs'], ['docs', 'imgs']])

    
# notes
    
# to check for error message
    # with pytest.raises(SomeError) as _excinfo:
    #    foo()
    # assert(r'foo' in str(_excinfo.value))

# assert the contents of file
    # assert(filecmp.cmp(out_path, std_path))

