# src/file_ops.py
"""
文件操作模块，执行实际的文件增、删、改操作。
"""

import shutil
import os
from logger import logger


def copy_file(src, dst):
    """
    复制文件，从src到dst，包含异常处理和日志记录。
    """
    try:
        shutil.copy2(src, dst)
        return True
    except Exception as e:
        # 记录错误日志
        logger.error(f"Failed to copy {src} to {dst}: {e}")
        return False

def delete_file(path):
    """
    删除文件或目录。
    """
    try:
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
        return True
    except Exception as e:
        logger.error(f"Failed to delete {path}: {e}")
        return False

def backup_file(path, backup_dir):
    """
    备份文件到指定的备份目录。
    """
    pass  # 后续实现
