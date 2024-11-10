# src/sync_logic.py
"""
同步逻辑模块，负责决策同步操作。
"""

def determine_sync_actions(differences, sync_strategy='two_way'):
    """
    根据差异列表和同步策略，生成同步操作列表。
    """
    actions = []
    for diff_type, file_entry in differences:
        if diff_type == 'new':
            actions.append(('copy', file_entry))
        elif diff_type == 'modified':
            actions.append(('update', file_entry))
        elif diff_type == 'deleted':
            actions.append(('delete', file_entry))
    return actions

def resolve_conflicts(conflicts):
    """
    处理冲突文件，根据策略决定保留版本。
    """
    pass  # 后续实现
