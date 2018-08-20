__version__ = '0.2.0'

from sqlwhat.sct_syntax import state_dec, Ex, fail
from sqlwhat.checks.check_funcs import has_result, has_nrows, check_column, has_equal_value, TinyNone

@state_dec
def check_result_tsql(state):
    """High level function which wraps other SCTs for checking results."""

    stu_res = state.student_result
    sol_res = state.solution_result

    # empty test
    has_result(state)

    # row test
    has_nrows(state)

    # column tests
    child = _sort_columns_indiv(state)
    for k in sol_res:
        msg = "Column `{}` in the solution does not have a column with matching values in your results."
        s = check_column(child, k)
        has_equal_value(s, incorrect_msg=msg)

    return state

@state_dec
def pof(state, msg='Your submission is incorrect.'):
    """High level function wrapping other SCTs, giving a pass or fail result."""
    Ex(state).check_correct(check_result_tsql(), fail(incorrect_msg=msg))
    return state

def _sort_columns_indiv(state):
    tiny_none = TinyNone()
    sorted_columns = lambda res: {k: sorted(col, key = lambda el: el or tiny_none) for k, col in res.items()}

    stu_res = sorted_columns(state.student_result)
    sol_res = sorted_columns(state.solution_result)

    return state.to_child(
                student_result = stu_res,
                solution_result = sol_res)
