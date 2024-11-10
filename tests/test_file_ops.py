# tests/test_file_ops.py
"""
针对file_ops.py模块的测试用例。
"""

import os
import shutil
import pytest

# 将src目录添加到系统路径，以便导入file_ops模块
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from file_ops import copy_file, delete_file, backup_file

@pytest.fixture
def setup_test_environment():
    """
    设置测试环境，包括源目录、目标目录和备份目录。
    """
    # 定义测试目录路径
    src_dir = 'test_env/src'
    dst_dir = 'test_env/dst'
    backup_dir = 'test_env/backup'

    # 如果目录存在，先删除
    for directory in [src_dir, dst_dir, backup_dir]:
        if os.path.exists(directory):
            shutil.rmtree(directory)

    # 创建目录
    os.makedirs(src_dir)
    os.makedirs(dst_dir)
    os.makedirs(backup_dir)

    return src_dir, dst_dir, backup_dir

def teardown_test_environment():
    """
    清理测试环境，删除测试目录。
    """
    test_env_dir = 'test_env'
    if os.path.exists(test_env_dir):
        shutil.rmtree(test_env_dir)

def test_copy_file_success(setup_test_environment):
    """
    测试copy_file函数在正常情况下的复制操作。
    """
    src_dir, dst_dir, _ = setup_test_environment
    src_file = os.path.join(src_dir, "test_copy.txt")
    dst_file = os.path.join(dst_dir, "test_copy.txt")

    try:
        # 创建源文件并写入内容
        with open(src_file, 'w') as f:
            f.write("This is a test file for copying.")

        # 执行复制操作
        result = copy_file(src_file, dst_file)

        # 断言复制操作成功
        assert result is True
        assert os.path.exists(dst_file)

        # 断言文件内容一致
        with open(dst_file, 'r') as f:
            content = f.read()
        assert content == "This is a test file for copying."
    finally:
        # 清理复制的文件
        if os.path.exists(dst_file):
            os.remove(dst_file)
        teardown_test_environment()

def test_copy_file_failure(setup_test_environment):
    """
    测试copy_file函数在目标路径无写权限时的复制操作失败情况。
    """
    src_dir, dst_dir, _ = setup_test_environment
    src_file = os.path.join(src_dir, "test_copy_fail.txt")
    dst_file = os.path.join(dst_dir, "test_copy_fail.txt")

    try:
        # 创建源文件并写入内容
        with open(src_file, 'w') as f:
            f.write("This file copy should fail.")

        # 模拟目标目录无写权限
        os.chmod(dst_dir, 0o400)  # 只读权限

        # 执行复制操作
        result = copy_file(src_file, dst_file)

        # 断言复制操作失败
        assert result is False
        assert not os.path.exists(dst_file)
    finally:
        # 恢复目标目录权限以便清理
        os.chmod(dst_dir, 0o700)
        teardown_test_environment()

def test_delete_file_success_file(setup_test_environment):
    """
    测试delete_file函数成功删除文件的情况。
    """
    src_dir, _, _ = setup_test_environment
    file_to_delete = os.path.join(src_dir, "test_delete.txt")

    try:
        # 创建文件并写入内容
        with open(file_to_delete, 'w') as f:
            f.write("This file will be deleted.")

        # 确认文件存在
        assert os.path.exists(file_to_delete)

        # 执行删除操作
        result = delete_file(file_to_delete)

        # 断言删除操作成功
        assert result is True
        assert not os.path.exists(file_to_delete)
    finally:
        teardown_test_environment()

def test_delete_file_success_directory(setup_test_environment):
    """
    测试delete_file函数成功删除目录的情况。
    """
    src_dir, _, _ = setup_test_environment
    dir_to_delete = os.path.join(src_dir, "test_dir_delete")
    dir_to_delete_inner_file = os.path.join(dir_to_delete, "inside_file.txt")

    try:
        # 创建目录和内部文件
        os.makedirs(dir_to_delete)
        with open(dir_to_delete_inner_file, 'w') as f:
            f.write("This file is inside the directory to be deleted.")

        # 确认目录和文件存在
        assert os.path.exists(dir_to_delete)
        assert os.path.exists(dir_to_delete_inner_file)

        # 执行删除操作
        result = delete_file(dir_to_delete)

        # 断言删除操作成功
        assert result is True
        assert not os.path.exists(dir_to_delete)
    finally:
        teardown_test_environment()

def test_delete_file_failure(setup_test_environment):
    """
    测试delete_file函数在删除不存在的文件时的失败情况。
    """
    _, _, _ = setup_test_environment
    non_existent_path = "non_existent_file.txt"

    try:
        # 确认文件不存在
        assert not os.path.exists(non_existent_path)

        # 执行删除操作
        result = delete_file(non_existent_path)

        # 断言删除操作失败
        assert result is False
    finally:
        teardown_test_environment()
