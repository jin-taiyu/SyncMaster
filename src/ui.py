# ui.py
"""
用户界面模块，处理用户输入和输出。
"""

import argparse

def parse_arguments():
    """
    解析命令行参数。
    """
    parser = argparse.ArgumentParser(description='文件同步工具')
    parser.add_argument('--src', required=True, help='源目录路径')
    parser.add_argument('--dst', required=True, help='目标目录路径')
    parser.add_argument('--strategy', choices=['one_way', 'two_way'], default='two_way', help='同步策略')
    args = parser.parse_args()
    return args
