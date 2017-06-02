from sqlwhat.Reporter import Reporter
from sqlwhat.State import State

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


from sct_syntax import Ex
from sqlwhat_ext import check_result2

def test_check_result2_chain():
    state = prepare_state({'a': [1,2,3]}, {'a': [1,2,3]})
    Ex(state).test_check_result2()

def test_check_result2_match_pass():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2,3]})
    check_result2(state, match = 'any')

def test_check_result2_match_fail():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2]})
    check_result2(state, match = 'any')
