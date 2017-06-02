__version__ = '0.0.1'

from sqlwhat.sct_syntax import *

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
