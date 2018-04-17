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
from sqlwhat_ext import pof

def test_pof_chain():
    state = prepare_state({'a': [1,2,3]}, {'a': [1,2,3]})
    Ex(state) >> pof()

@pytest.mark.parametrize('sol_res, stu_res', [        # pass cases where...
    ( {'a': [1,2,3]}, {'a': [1,2,3]} ),              # identical
    ( {'a': [1,2,3]}, {'b': [1,2,3]} ),              # diff colnames
    ( {'a': [1,2,3]}, {'b': [3,2,1]} ),              # diff colnames + reordered
    ( {'a': [1]}    , {'a': [1], 'b': [2]} )         # extra cols in student result
    ])

def test_pof_pass(sol_res, stu_res):
    state = prepare_state(sol_res, stu_res)
    pof(state)

@pytest.mark.parametrize('sol_res, stu_res', [        # fail cases where...
    ( {'a': [1,2,3]}, {'a': [1,2]} ),                # too few rows
    ( {'a': [1,2,3]}, {'a': [1,2,2]} )               # values mismatch
    ])

def test_check_pof_match_fail(sol_res, stu_res):
    state = prepare_state(sol_res, stu_res)
    with pytest.raises(TF):
        pof(state)
