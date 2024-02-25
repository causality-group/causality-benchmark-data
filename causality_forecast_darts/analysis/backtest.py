

def signalbacktest_df(signal_df, upcoming_ret_df, enter_at_stdev=2.0):
    """A simple backtest, trading cross-sectional signals at a given standard deviation.

    Invests $0.5 both long and short, hence results can be interpreted as strategy returns.

    Args:
        signal_df: DataFrame with signals observable at the Timestamps in in its index.
        upcoming_ret_df: DataFrame with forward looking returns tradeable at the Timestamps in in its index.
        enter_at_stdev: Number of standard deviations to enter the trade both on long and short side.
    
    Returns:
        DataFrame with strategy returns.
    """
    is_long_df = signal_df.add(-(signal_df.mean(axis=1) + enter_at_stdev * signal_df.std(axis=1)), axis=0) > 0.0
    is_short_df = signal_df.add(-(signal_df.mean(axis=1) - enter_at_stdev * signal_df.std(axis=1)), axis=0) < 0.0

    signal_df = is_long_df.astype(int) - is_short_df.astype(int)
    # Demean cross-sectionally:
    signal_df = signal_df.add(-signal_df.mean(axis=1), axis=0)
    # Normalize cross-sectionally:
    signal_df = signal_df.div(signal_df.abs().sum(axis=1), axis=0)

    return signal_df * upcoming_ret_df