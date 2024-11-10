# tests/test_file_scan.py
"""
针对file_scan.py模块的测试用例。
"""

import os
import sys
import shutil
import pytest

# 将src目录添加到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from file_scan import scan_directory, compare_directories, FileEntry

def test_file_entry():
    """
    测试FileEntry类的初始化和属性。
    """
    test_file = 'test.txt'
    with open(test_file, 'w') as f:
        f.write('Test content')
    file_entry = FileEntry(test_file)
    assert file_entry.path == test_file
    assert file_entry.size == os.path.getsize(test_file)
    assert file_entry.mod_time == os.path.getmtime(test_file)
    os.remove(test_file)

def test_scan_directory():
    """
    测试scan_directory函数。
    """
    test_dir = 'test_dir'
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    try:
        with open(os.path.join(test_dir, 'test.txt'), 'w') as f:
            f.write('Test content')
        entries = scan_directory(test_dir)
        assert len(entries) == 2 # 包含 test_dir 和 test.txt
    finally:
        shutil.rmtree(test_dir)

def test_scan_directory_with_nested_dirs():
    """
    测试scan_directory函数，包含内嵌目录和目录内的文件。
    """
    test_dir = 'test_dir'
    nested_dir = os.path.join(test_dir, 'nested_dir')
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(nested_dir)
    """
    test_dir/
    ├── test.txt   
    ├── nested_dir/
    │   ├── nested_test.txt
    """
    try:
        with open(os.path.join(test_dir, 'test.txt'), 'w') as f:
            f.write('Test content')
        with open(os.path.join(nested_dir, 'nested_test.txt'), 'w') as f:
            f.write('Nested test content')
        entries = scan_directory(test_dir)
        assert len(entries) == 4
        paths = [entry.path for entry in entries]
        assert os.path.join(test_dir, 'test.txt') in paths
        assert os.path.join(nested_dir, 'nested_test.txt') in paths
    finally:
        shutil.rmtree(test_dir)

def test_compare_directories():
    """
    测试compare_directories函数。
    """
    # 创建源目录和目标目录，添加测试文件
    src_dir = 'src_test_dir'
    dst_dir = 'dst_test_dir'
    if os.path.exists(src_dir):
        shutil.rmtree(src_dir)
    os.makedirs(src_dir)
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)

    try:
        with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
            f.write('File in source')

        with open(os.path.join(dst_dir, 'file2.txt'), 'w') as f:
            f.write('File in destination')

        src_entries = scan_directory(src_dir)
        dst_entries = scan_directory(dst_dir)

        differences = compare_directories(src_entries, dst_entries)

        # 预期differences应包含'new'和'deleted'类型的文件
        assert any(diff[0] == 'new' for diff in differences)
        assert any(diff[0] == 'deleted' for diff in differences)
    finally:
        # 清理测试目录
        shutil.rmtree(src_dir)
        shutil.rmtree(dst_dir)
