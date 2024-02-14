import pandas as pd


def compound_ret_df(
    df1: pd.DataFrame, 
    df2: pd.DataFrame
) -> pd.DataFrame:
    """Compounds arithmetic returns.
    
    Args:
        df1: DataFrame with arithmetic returns
        df2: DataFrame with arithmetic returns

    Returns:
        DataFrame with compounded returns
    """
    return (1.0 + df1) * (1.0 + df2) - 1.0