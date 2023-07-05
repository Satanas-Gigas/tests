# -*- coding: windows-1251 -*-
import pytest
import old_hw

def test_task_1():
    ref = [
        {'visit1': ['������', '������']},
        {'visit3': ['��������', '������']},
        {'visit7': ['����', '������']},
        {'visit8': ['����', '������']},
        {'visit9': ['�����', '������']},
        {'visit10': ['�����������', '������']}
    ]
    res = old_hw.task_1()
    assert res == ref

def test_task_2():
    ref = [98, 35, 15, 213, 54, 119]
    res = old_hw.task_2()
    assert res == ref

def test_task_3():
    ref = {3: 57.14, 2: 42.86}
    res = old_hw.task_3()
    assert res == ref