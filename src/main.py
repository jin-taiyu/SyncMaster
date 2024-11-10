# src/main.py
"""
程序的主入口模块。
"""

from ui import parse_arguments
from file_scan import scan_directory, compare_directories
from sync_logic import determine_sync_actions
from file_ops import copy_file, delete_file

def main():
    """
    主函数，负责启动程序。
    """
    args = parse_arguments()

    src_entries = scan_directory(args.src)
    dst_entries = scan_directory(args.dst)

    differences = compare_directories(src_entries, dst_entries)

    actions = determine_sync_actions(differences, args.strategy)

    for action, file_entry in actions:
        if action == 'copy':
            copy_file(file_entry.path, args.dst)
        elif action == 'update':
            copy_file(file_entry.path, args.dst)
        elif action == 'delete':
            delete_file(file_entry.path)

if __name__ == "__main__":
    main()

