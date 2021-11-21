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
# import numpy as np
# import shilofue.Foo as Foo  # import test module
# from shilofue.Utilities import 
# from matplotlib import pyplot as plt
# from shutil import rmtree  # for remove directories
from python_scripts.Utilities import ImageMerge, ImageClip

test_dir = ".test"
source_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'image_operation')

if not os.path.isdir(test_dir):
    # check we have the directory to store test result
    os.mkdir(test_dir)


r"""
Classes and functions related to post-process images
"""
def test_image_merge():
    '''
    test function ImageMerge
    '''
    test_im_dir = os.path.join(test_dir, 'image_operation')
    if not os.path.isdir(test_im_dir):
        os.mkdir(test_im_dir)
    # test 0
    file_path0 = os.path.join(source_dir, 'um_temperature000024.png')
    file_path1 = os.path.join(source_dir, 'um_frame.png')
    assert(os.path.isfile(file_path0))
    assert(os.path.isfile(file_path1))
    o_path = os.path.join(test_im_dir, 'merge.png')
    o_path = ImageMerge([file_path0, file_path1], o_path, masks=[0, 1])
    assert(os.path.isfile(o_path))


def test_image_clip():
    '''
    test function ImageClip
    '''
    file_path = os.path.join(source_dir, 'um_temperature000024.png')
    assert(os.path.isfile(file_path))
    o_path = ImageClip(file_path, [0, 0, 10, 10])

    
# notes
    
# to check for error message
    # with pytest.raises(SomeError) as _excinfo:
    #    foo()
    # assert(r'foo' in str(_excinfo.value))

# assert the contents of file
    # assert(filecmp.cmp(out_path, std_path))

