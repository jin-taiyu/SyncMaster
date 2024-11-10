# tests/test_sync_logic.py
"""
针对sync_logic.py模块的测试用例。
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sync_logic import determine_sync_actions

def test_determine_sync_actions():
    """
    测试determine_sync_actions函数。
    """
    differences = [('new', 'file1'), ('modified', 'file2'), ('deleted', 'file3')]
    actions = determine_sync_actions(differences)
    assert len(actions) == 3
    assert actions[0][0] == 'copy'
    assert actions[1][0] == 'update'
    assert actions[2][0] == 'delete'
