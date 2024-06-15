import os
import pytest
import numpy as np
from python_scripts import Utilities


r'''
Functions that bridging unix operations
'''
def test_var_subs():
    '''
    Test the var_subs function
    '''
    # example 1, actually do nothing
    result = Utilities.var_subs("foo")
    assert(result == 'foo')
    # example 2
    result = Utilities.var_subs("${HOME}/foo/${ASPECT_LAB_DIR}")
    result_std = os.environ['HOME'] + "/foo/" + os.environ['ASPECT_LAB_DIR']
    assert(result == result_std)
    pass


r'''
Functions for read files
'''
def test_read_header():
    '''
    Test the ReadHeader function
    Asserts:
        key == keywords in header, with ' ' substituded by '_'
        cols == columes in header - 1
        units == units in header or None
    '''
    _texts = ['# 1: Time step', '# 2: Time (years)', '# 12: Iterations for composition solver 1']
    _header = Utilities.ReadHeader(_texts)  # call function
    assert(_header['Time_step']['col'] == 0)
    assert(_header['Time_step']['unit'] == None)
    assert(_header['Time']['col'] == 1)
    assert(_header['Time']['unit'] == 'years')
    assert(_header['Iterations_for_composition_solver_1']['col'] == 11)
    assert(_header['Iterations_for_composition_solver_1']['unit'] == None)


def test_read_header2():
    '''
    Test the ReadHeader2 function
    Asserts:
        key == keywords in header, with ' ' substituded by '_'
        cols == columes in header - 1
        units == units in header or None
    '''
    _texts = [' Time_step   Time    Iterations_for_composition_solver_1']
    _header = Utilities.ReadHeader2(_texts)  # call function
    assert(_header['Time_step']['col'] == 0)
    assert(_header['Time_step']['unit'] == None)
    assert(_header['Time']['col'] == 1)
    assert(_header['Time']['unit'] == None)
    assert(_header['Iterations_for_composition_solver_1']['col'] == 2)
    assert(_header['Iterations_for_composition_solver_1']['unit'] == None)


def test_re_count_indent():
    '''
    Tests the re_count_indent funtion
    Asserts:
        indent = right value
    '''
    # test 1
    _pattern = ' \tfoo'
    _indent = Utilities.re_count_indent(_pattern)
    assert(_indent == 5)
    # test 2
    _pattern = '    foo'
    _indent = Utilities.re_count_indent(_pattern)
    assert(_indent == 4)


def test_ggr2cart2():
    '''
    Tests the ggr2cart2 funtion
    Asserts:
        return value is correct
    '''
    # test 1
    lon = 0.0
    r = 1.0
    x, y = Utilities.ggr2cart2(lon, r)
    # x = 1.0, y = 0.0
    assert(abs(x-1.0)/1.0 < 1e-8)
    assert(y/1.0 < 1e-8)
    # test 2
    lon = np.pi / 4.0
    r = 1.0
    x, y = Utilities.ggr2cart2(lon, r)
    # x = sqrt(2)/2, y = sqrt(2)/2
    temp = 2.0**0.5 / 2.0
    assert(abs(x-temp)/temp < 1e-8)
    assert(abs(y-temp)/temp < 1e-8)


def test_ggr2cart():
    '''
    Tests the ggr2cart funtion
    Asserts:
        return value is correct
    '''
    # test 1
    lon = 0.0
    lat = 0.0
    r = 1.0
    # x = 1.0, y = z = 0.0
    x, y, z = Utilities.ggr2cart(lat, lon, r)
    assert(abs(x-1.0)/1.0 < 1e-8)
    assert(y/1.0 < 1e-8)
    assert(z/1.0 < 1e-8)
    # test 2
    lon = - np.pi / 4.0
    lat = np.pi / 4.0
    r = 1.0
    # x = 0.5 , y = -0.5,  z = sqrt(2)/2
    x, y, z = Utilities.ggr2cart(lat, lon, r)
    assert(abs(x-0.5)/0.5 < 1e-8)
    assert(abs((y+0.5)/0.5) < 1e-8)
    temp = 2.0**0.5 / 2.0
    assert(abs(z-temp)/temp < 1e-8)


def test_cart2sph():
    '''
    Tests the cart2sph funtion
    Asserts:
        return value is correct
    '''
    # test1
    x, y, z = 0., 1., 0.
    r0, th0, ph0 = 1., np.pi/2.0, np.pi/2.0
    r, th, ph = Utilities.cart2sph(x, y, z)
    assert(abs((r - r0)/r0) < 1e-8)
    assert(abs((th-th0)/th0) < 1e-8)
    assert(abs((ph-ph0)/ph0) < 1e-8)

    # test2
    x, y, z = 3.0**0.5/2.0, 0.5, 1.0 
    r0, th0, ph0 = 2.0**0.5, np.pi/4.0, np.pi/6.0
    r, th, ph = Utilities.cart2sph(x, y, z)
    assert(abs((r - r0)/r0) < 1e-8)
    assert(abs((th-th0)/th0) < 1e-8)
    assert(abs((ph-ph0)/ph0) < 1e-8)


def test_cart2sph2():
    '''
    Tests the cart2sph2 funtion
    Asserts:
        return value is correct
    '''
    # test1
    x, y = 0., 1.
    r0, ph0 = 1., np.pi/2.0
    r, ph = Utilities.cart2sph2(x, y)
    assert(abs((r - r0)/r0) < 1e-8)
    assert(abs((ph-ph0)/ph0) < 1e-8)

    # test2
    x, y = -0.5, 3.0**0.5/2.
    r0, ph0 = 1., 2.0*np.pi/3.0
    r, ph = Utilities.cart2sph2(x, y)
    assert(abs((r - r0)/r0) < 1e-8)
    assert(abs((ph-ph0)/ph0) < 1e-8)


def test_make_2d_array():
    """
    Tests the Make2dArray function
    Asserts:
        return value is of the correct type
    """
    # test 1
    x = 1.0
    y = Utilities.Make2dArray(x)
    assert(y.shape == (1, 1))

    # test 2
    x = [0.0, 1.0]
    y = Utilities.Make2dArray(x)
    assert(y.shape == (1, 2))
    
    # test 3, we flip test 2
    x = [0.0, 1.0]
    y = np.transpose(Utilities.Make2dArray(x))
    assert(y.shape == (2, 1))

    # test 4, raises error if type is incorrect
    with pytest.raises(TypeError) as excinfo:
        x = {'foo': 0.0}
        y = Utilities.Make2dArray(x)
    assert ('Make2dArray, x must be int, float, list or 1d ndarray' in str(excinfo.value))


def test_code_sub():
    '''
    Test the class CODESUB
    '''
    pass

def test_string2list():
    input = '[5, 6, 7, 8, 9, 10, 11, 12, 13]'
    output = Utilities.string2list(input)
    assert(output==[5, 6, 7, 8, 9, 10, 11, 12, 13])


def test_write_dict_recursive():
    '''
    test write_dict_recursive
    assert:

    '''
    test_dict = {'foo': {'subfoo': 1}, 'foo1': 0}
    # test 1
    result_dict = Utilities.write_dict_recursive(test_dict, ['foo', 'subfoo'], 2)
    assert(result_dict ==  {'foo': {'subfoo': 2}, 'foo1': 0})
    # test 2
    result_dict = Utilities.write_dict_recursive(test_dict, ['foo2'], 3)
    assert(result_dict == {'foo': {'subfoo': 2}, 'foo1': 0, 'foo2': 3})


def test_insert_dict_after():
    '''
    test the implementation of dict_insert_after
    assert:
        1. the new option is successfully inserted into the dictionary
        2. this also works for a complex dict
    '''
    test_dict = {'a': 1, 'b': 2, 'd': 4}
    Utilities.insert_dict_after(test_dict, 'c', 3, 'b')
    assert(str(test_dict)=="{'a': 1, 'b': 2, 'c': 3, 'd': 4}")  # assert 1
    test_dict = {'a': {'a1': 1.1, 'a2': 1.2}, 'b': 2, 'd': {'d1': 4, 'd2': 5}}
    Utilities.insert_dict_after(test_dict, 'c', [3.1, 3.2], 'b')
    assert(str(test_dict) == "{'a': {'a1': 1.1, 'a2': 1.2}, 'b': 2, 'c': [3.1, 3.2], 'd': {'d1': 4, 'd2': 5}}") # assert 2


def test_map_mid_point():
    '''
    test the function of map_mid_point(lon1, lat1, lon2, lat2, frac)
    assert:
        the coordinates of the mid points
    '''
    lon1, lat1 = -73.935242, 40.730610  # New York City (approx.)
    lon2, lat2 = -118.243683, 34.052235  # Los Angeles (approx.)
    # assert 1: point in the middle
    frac = 0.5
    mid_lon, mid_lat = Utilities.map_mid_point(lon1, lat1, lon2, lat2, frac)
    mid_lon_std, mid_lat_std = -97.12968569482643, 39.52640503514376
    assert(abs(mid_lon - mid_lon_std)/mid_lon_std < 1e-6 and abs(mid_lat - mid_lat_std)/mid_lat_std < 1e-6)
    # assert 2: point approaching one end
    frac = 0.0
    mid_lon, mid_lat = Utilities.map_mid_point(lon1, lat1, lon2, lat2, frac)
    mid_lon_std, mid_lat_std = -73.935242, 40.730610
    assert(abs(mid_lon - mid_lon_std)/mid_lon_std < 1e-6 and abs(mid_lat - mid_lat_std)/mid_lat_std < 1e-6)
    # assert 3: query points are at two sides of 180.0
    lon1, lat1 = -173.935242, -40.730610  # New York City (approx.)
    lon2, lat2 = 177.243683, 34.052235  # Los Angeles (approx.)
    frac = 0.5
    mid_lon, mid_lat = Utilities.map_mid_point(lon1, lat1, lon2, lat2, frac)
    mid_lon_std, mid_lat_std = -178.54285589904237, -3.3490631461072344
    assert(abs(mid_lon - mid_lon_std)/mid_lon_std < 1e-6 and abs(mid_lat - mid_lat_std)/mid_lat_std < 1e-6)


def test_map_point_by_distance():
    '''
    test the function map_point_by_distance
    assert:
        the coordinates of the derived point
    '''
    lon0, lat0 = -178.0, 50.0
    theta, d = 270.0, 1000e3 # 100 km
    lon1_std, lat1_std = 168.16811943494397, 49.16776775255277
    lon1, lat1 = Utilities.map_point_by_distance(lon0, lat0, theta, d)
    assert(abs((lon1 - lon1_std)/lon1) < 1e-6)
    assert(abs((lat1 - lat1_std)/lat1) < 1e-6)