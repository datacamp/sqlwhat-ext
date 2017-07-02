from sqlwhat.Reporter import Reporter
from sqlwhat.State import State
from sqlwhat.selectors import Dispatcher
from sqlwhat.Test import TestFail as TF

import pytest

def prepare_state(sol_result, stu_result):
    dispatcher = Dispatcher.from_dialect('postgresql')

    return State(
        student_code = "",
        solution_code = "",
        reporter = Reporter(),
        # args below should be ignored
        pre_exercise_code = "",
        student_result = stu_result, solution_result = sol_result,
        student_conn = None, solution_conn = None,
        ast_dispatcher = dispatcher)


from sqlwhat.sct_syntax import Ex
from sqlwhat_ext import check_result_tsql

def test_check_result_tsql_chain():
    state = prepare_state({'a': [1,2,3]}, {'a': [1,2,3]})
    Ex(state) >> check_result_tsql()

def test_check_result_tsql_match_pass():
    state = prepare_state({'a': [1,2,3]}, {'a': [1,2,3]})
    check_result_tsql(state)

def test_check_result_tsql_match_fail1():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2,3]})
    with pytest.raises(TF):
        check_result_tsql(state)

def test_check_result_tsql_match_fail2():
    state = prepare_state({'a': [1,2,3]}, {'a': [1,2]})
    with pytest.raises(TF):
        check_result_tsql(state)
