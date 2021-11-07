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
import json
# import shilofue.Foo as Foo  # import test module
from python_scripts.Utilities import JSON_OPT, show_all_options, read_dict_recursive
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
    #
    json_opt.add_key('directory of case', list, ['dirs'], ['.']) # a key in the file
    json_opt.add_key('foo', int, ['foo'], 0)  # an key not in the file
    json_opt.read_json(json_path)
    assert(len(json_opt.values)==2)
    assert(json_opt.values[0] == ['non_linear30/eba_re_mesh1']) # value from the file
    assert(json_opt.values[1] == 0) # the default value
    
    
def test_supporting_functions():
    '''
    test the supporting functions
        show_all_options
        read_dict_recursive
    Define the options of one type of json file and read in examples
    '''
    json_path = os.path.join(source_dir, 'test.json')
    with open(json_path, 'r') as fin:
        _dict = json.load(fin)
    # test show_all_options
    all_options = show_all_options(json_path)
    assert(all_options == \
        [['dirs'], ['py_format'], ['visit'], ['visit', 'slab'], ['visit', 'slab', 'steps'],\
            ['visit', 'slab', 'deform_mechanism'], ['docs'], ['docs', 'imgs']])
    # test read_dict_recursive
    value = read_dict_recursive(_dict, ['visit', 'slab', 'deform_mechanism'])
    assert(value == 1)
    value = read_dict_recursive(_dict, ['visit', 'slab', 'steps'])
    assert(value == [0, 1, 2, 3, 4, 5, 6, 7])

    
# notes
    
# to check for error message
    # with pytest.raises(SomeError) as _excinfo:
    #    foo()
    # assert(r'foo' in str(_excinfo.value))

# assert the contents of file
    # assert(filecmp.cmp(out_path, std_path))

