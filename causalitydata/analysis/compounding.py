"""Functionality to compound returns."""

import numpy as np
import pandas as pd
from typing import List

EPSILON_TIME = pd.offsets.Micro()


def compound_ret_df(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Compounds arithmetic returns.

    Args:
        df1: DataFrame with arithmetic returns
        df2: DataFrame with arithmetic returns

    Returns:
        DataFrame with compounded returns
    """
    return (1.0 + df1) * (1.0 + df2) - 1.0


def _sum_nan_if_all_nan_df(df: pd.DataFrame) -> pd.Series:
    """
    If all values in a column are NaN, result will be NaN.
    Otherwise, the sum of the values.
    """
    sum_ser = df.sum(axis=0)
    all_nan_ser = df.count(axis=0) == 0
    sum_ser[all_nan_ser] = np.nan
    return sum_ser


def compound_upcoming_bar_return_cc_df(
    ret_cc_df: pd.DataFrame, bar_tss: List[pd.Timestamp]
) -> pd.DataFrame:
    """
    Compounds daily adjusted close to close returns for each Timestamp in bar_tss,
    such that we can trade those at the 16:00 auction.

    Returns bars do not overlap, each covers a time period from 16:00 between bar_tss[i] and bar_tss[i+1].
    """
    # Returns end on the index date, need to align to the start date of the return
    ret_cc_df = ret_cc_df.shift(-1)
    ret_cc_df = np.log(ret_cc_df + 1.0)  # convert to log returns
    bar_tss = bar_tss + [pd.Timestamp.max]
    log_bar_ret_df = pd.DataFrame(
        {
            # Indexing my Timestamp is inclusive, hence: -EPSILON_TIME
            ts: _sum_nan_if_all_nan_df(
                ret_cc_df.loc[ts : bar_tss[i + 1] - EPSILON_TIME, :]
            )
            for i, ts in enumerate(bar_tss[:-1])
        }
    ).T
    return np.exp(log_bar_ret_df) - 1.0


def compound_observable_bar_return_cc_df(
    ret_cc_df: pd.DataFrame,
    bar_tss: List[pd.Timestamp],
) -> pd.DataFrame:
    """
    Compounds daily adjusted close to close returns for each Timestamp in bar_tss,
    such that we can observe those at 15:45 to trade the 16:00 auction.

    This means in practice using close prices only until previous close.

    Returns bars do not overlap, each covers a time period from 16:00
    between bar_tss[i] and bar_tss[i+1].
    """
    ret_cc_df = np.log(ret_cc_df + 1.0)  # convert to log returns
    bar_tss = [pd.Timestamp.min] + bar_tss
    log_bar_ret_df = pd.DataFrame(
        {
            # Indexing my Timestamp is inclusive, hence: -EPSILON_TIME
            ts: _sum_nan_if_all_nan_df(
                ret_cc_df.loc[bar_tss[i - 1] : ts - EPSILON_TIME, :]
            )
            for i, ts in enumerate(bar_tss)
            if i > 0
        }
    ).T
    return np.exp(log_bar_ret_df) - 1.0
