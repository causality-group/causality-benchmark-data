import os

import numpy as np
import pandas as pd
from typing import Tuple, Optional


def load_field_df(
    field_name: str,
    data_root_path: str,
    shift: int = 0,
    end_ts: Optional[pd.Timestamp] = None,
) -> pd.DataFrame:
    """
    Loads data fields into DataFrame with DateTimeIndex.
    
    Args:
        field_name: name of the field to load
        data_root_path: path to the data root directory
        shift: number of periods to shift the data by. Positive shift lags, negative shift peeks into the future.
        end_ts: end date of the DataFrame. If None, the whole DataFrame is returned.

    Returns:
        DataFrame with DateTimeIndex. 
        Columns are strings including ticker symbol, exchange and CFI category, while rows are dates of the observations.
    """
    df = load_path_df(os.path.join(data_root_path, field_name+'.csv'))
    df.index = pd.DatetimeIndex(pd.to_datetime(df.index))
    df = df.shift(shift)
    if end_ts is not None:
        df = df.loc[:end_ts, :]
    return df


def load_path_df(
    csvfile_path: str, 
    exclude_tickers: Tuple = (), 
    dtype: type = np.float64,
) -> pd.DataFrame:
    """
    Reads data into pandas from csv files.

    Args:
        csvfile_path: path to csv file
        exclude_tickers: list of tickers to exclude
        dtype: data type to read in

    Returns:
        pd.DataFrame with time index and columns for each ticker
    """
    if 'str' in str(dtype):
        df = pd.read_csv(
            csvfile_path,
            # avoid DtypeWarning: Columns (1..1330) have mixed types. Specify dtype option on import or set low_memory=False
            low_memory=False,
            index_col=0,
            header=0,
            parse_dates=False,
            dtype=dtype,
        )
    else:   # numeric type
        df = pd.read_csv(
            csvfile_path,
            # avoid DtypeWarning: Columns (1..1330) have mixed types. Specify dtype option on import or set low_memory=False
            low_memory=False,
            index_col=0,
            header=0,
            parse_dates=False,
        )

    if len(exclude_tickers):
        for ex in exclude_tickers:
            df = df[[s for s in df.columns if ex not in s]]
    if 'str' in str(dtype):
        return df
    else:  # numeric type
        return df.astype(dtype=dtype, copy=False)
