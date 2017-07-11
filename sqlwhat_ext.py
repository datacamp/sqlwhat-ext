__version__ = '0.2.0'

from sqlwhat.sct_syntax import *
from sqlwhat.checks.check_result import TinyNone

@state_dec
def check_result2(state, col_names = None, sort = False, match = 'exact'):
    """High level SCT for testing submission results.

    Args:
        col_names: names of columns to test for equality. Defaults to all.
        sort:      whether to sort the rows of the results.
        match:     argument passed to test_column.
    """
    col_names = list(state.solution_result.keys()) if col_names is None else col_names

    # test that results contain any columns
    test_has_columns(state)

    # test number of columns
    test_ncols(state)
    # test number of rows
    test_nrows(state)

    # sort rows so that order doesn't matter
    child = sort_rows(state) if sort else state

    # test column names and values
    for k in col_names:
        if not match == 'any': test_column_name(child, k)
        test_column(child, k, match = match)

    # return state in case another SCT is used after
    return state

@state_dec
def check_result_tsql(state, msg="Incorrect result."):
    """High level function which wraps other SCTs for checking results."""

    stu_res = state.student_result
    sol_res = state.solution_result

    # empty test
    test_has_columns(state)
    # row test
    test_nrows(state)
    # column tests
    child = _sort_columns_indiv(state)
    for k in sol_res:
        msg = "Column `{}` in the solution does not have a column with matching values in your results."
        test_column(child, k, msg, match = 'any')

    return state

@state_dec
def pof(state, msg='Your submission is incorrect.'):
    """High level function wrapping other SCTs, giving a pass or fail result."""
    Ex(state).test_correct(check_result_tsql(), fail(msg=msg))
    return state

def _sort_columns_indiv(state):
    tiny_none = TinyNone()
    sorted_columns = lambda res: {k: sorted(col, key = lambda el: el or tiny_none) for k, col in res.items()}

    stu_res = sorted_columns(state.student_result)
    sol_res = sorted_columns(state.solution_result)

    return state.to_child(
                student_result = stu_res,
                solution_result = sol_res)
