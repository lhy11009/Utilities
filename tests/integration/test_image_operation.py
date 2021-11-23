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
# from matplotlib import pyplot as plt
# from shutil import rmtree  # for remove directories
from python_scripts.Utilities import ImageMerge, PillowRun, func_name, IMAGE_OPT, PILLOW_OPT

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
    if os.path.isfile(o_path):
        os.remove(o_path)  # remove old ones
    new_image = ImageMerge([file_path0, file_path1],\
        mask=[0, 1], resize=[1.0, 1.0], position=[(), (124, 331)])
    new_image.save(o_path)  # save figure
    print("%s: saved figure %s" % (func_name(), o_path))
    assert(os.path.isfile(o_path))
    # test 1: crop the previous figure
    o_path = os.path.join(test_im_dir, 'merge_crop.png')
    new_image = new_image.crop((124, 331, 1000, 900))
    new_image.save(o_path)  # save figure
    print("%s: saved figure %s" % (func_name(), o_path))


def test_image_option():
    '''
    test the options for ImageMerge
    '''
    json_path = os.path.join(source_dir, 'figure_option.json')
    assert(os.path.isfile(json_path))
    pillow_opt = PILLOW_OPT()
    pillow_opt.read_json(json_path)
    assert(len(pillow_opt.values) == 1)
    assert(len(pillow_opt.values[0]) == 3)
    assert(pillow_opt.values[0][0].values ==\
        ['tests/integration/fixtures/image_operation/um_temperature000024.png',\
            'new', 0, 1.0, [0, 0], '', 'on_first_figure', 0])


def test_pillow_run():
    '''
    test the pillow run function
    '''
    json_path = os.path.join(source_dir, 'figure_option.json')
    assert(os.path.isfile(json_path))
    o_paths = [".test/image_operation/pillow_merge.png",\
        ".test/image_operation/pillow_merge_crop.png"]
    for o_path in o_paths:
        if os.path.isfile(o_path):
            os.remove(o_path)  # remove old files
    pillow_opt = PILLOW_OPT()
    pillow_opt.read_json(json_path)
    PillowRun(*pillow_opt.to_pillow_run())
    assert(not os.path.isfile(o_paths[0]))  # assert intermediate results deleted
    assert(os.path.isfile(o_paths[1]))  # assert file generation

    
# notes
    
# to check for error message
    # with pytest.raises(SomeError) as _excinfo:
    #    foo()
    # assert(r'foo' in str(_excinfo.value))

# assert the contents of file
    # assert(filecmp.cmp(out_path, std_path))

