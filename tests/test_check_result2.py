from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF
from sqlwhat.State import State

import pytest

def prepare_state(sol_result, stu_result):
    return State(
        student_code = "",
        solution_code = "",
        reporter = Reporter(),
        # args below should be ignored
        pre_exercise_code = "",
        student_result = stu_result, solution_result = sol_result,
        student_conn = None, solution_conn = None)


from sqlwhat.sct_syntax import Ex
from sqlwhat_ext import check_result2

def test_check_result2_chain():
    state = prepare_state({'a': [1,2,3]}, {'a': [1,2,3]})
    Ex(state) >> check_result2()

def test_check_result2_match_pass():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2,3]})
    check_result2(state, match = 'any')

def test_check_result2_match_fail():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2]})
    with pytest.raises(TF):
        check_result2(state, match = 'any')
