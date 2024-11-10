# src/file_scan.py
"""
文件扫描和比较模块。
"""

import os
import hashlib

class FileEntry:
    """
    文件条目类，表示文件或目录的元数据。
    """
    def __init__(self, path):
        self.path = path
        self.size = None
        self.mod_time = None
        self.hash_value = None
        self.is_directory = os.path.isdir(path)
        self.get_file_info()

    def get_file_info(self):
        """
        获取文件的基本信息。
        """
        if not self.is_directory:
            self.size = os.path.getsize(self.path)
            self.mod_time = os.path.getmtime(self.path)

    def compute_hash(self):
        """
        计算文件的哈希值。
        """
        if not self.is_directory:
            hasher = hashlib.md5()
            with open(self.path, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
            self.hash_value = hasher.hexdigest()

def scan_directory(path):
    """
    递归扫描目录，返回FileEntry对象的列表。
    """
    file_entries = [FileEntry(path)]
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            full_path = os.path.join(root, name)
            file_entry = FileEntry(full_path)
            file_entries.append(file_entry)
    return file_entries

def compare_directories(src_entries, dst_entries):
    """
    比较源和目标目录的文件列表，返回差异信息。
    """
    # 将列表转换为字典，键为相对路径
    src_dict = {os.path.relpath(entry.path, src_entries[0].path): entry for entry in src_entries}
    dst_dict = {os.path.relpath(entry.path, dst_entries[0].path): entry for entry in dst_entries}

    differences = []

    # 遍历源目录的文件
    for rel_path, src_entry in src_dict.items():
        dst_entry = dst_dict.get(rel_path)
        if not dst_entry:
            # 目标目录中不存在，表示新增
            differences.append(('new', src_entry))
        else:
            # 比较哈希值或修改时间，判断是否修改
            src_entry.compute_hash()
            dst_entry.compute_hash()
            if src_entry.hash_value != dst_entry.hash_value:
                differences.append(('modified', src_entry))
            # 已处理的文件从目标字典中移除
            dst_dict.pop(rel_path)

    # 剩下的dst_dict中的文件是源目录中没有的，表示删除
    for rel_path, dst_entry in dst_dict.items():
        differences.append(('deleted', dst_entry))

    return differences

