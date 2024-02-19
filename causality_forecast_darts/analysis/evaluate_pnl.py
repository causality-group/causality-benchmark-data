import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from typing import List, Optional, Tuple


def plot_pnl(
    pnl_df: pd.DataFrame,
    xlabel: Optional[str] = "Time",
    ylabel: Optional[str] = "Cumulative PnL",
    title: Optional[str] = "Profit and Loss Curve",
    append_legends: Optional[List[str]] = None,
    figure_size: Tuple[int, int] = (10, 6),
):
    """
    Plots a PnL DataFrame.

    Args:
        pnl_df: DataFrame with PnL values for each trading period
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        title: Title of the plot
        append_legends: List of strings to append to the legend of each line
        figure_size: Size of the figure (width, height)
    """
    plt.figure(figsize=figure_size)
    plt.plot(pnl_df.index, pnl_df.cumsum().values)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    legends = pnl_df.columns.tolist()
    if append_legends is not None:
        new_legend = []
        for i, item in enumerate(legends):
            new_legend += [legends[i] + item]
        legends = new_legend
    plt.legend(legends, bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.show()


def calculate_performance_df(
    pnl_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculates performance metrics for a PnL DataFrame:
     - Cumulative PnL
     - Daily PnL
     - Average PnL
     - Maximum PnL
     - Minimum PnL
     - PnL Standard Deviation
     - Sharpe Ratio
     - Sortino Ratio
     - Maximum Drawdown
     - Calmar Ratio
     - Matrin Ratio

    Args:
        pnl_df: DataFrame with PnL values for each trading period
        signal_df: DataFrame with trading signals for each trading period

    Returns:
        pd.DataFrame with performance metrics.
        Performance metrics are rows of the DataFrame, and column names match column names in the pnl_df argument.
    """

    num_periods_per_year = len(pnl_df.index) / (
        (pnl_df.index[-1].year + (pnl_df.index[-1].month - 1) / 12)
        - (pnl_df.index[0].year + (pnl_df.index[0].month - 1) / 12)
    )

    performance_df = pd.DataFrame()

    # Cumulative PnL
    performance_df["Cumulative PnL"] = pnl_df.sum()

    # Daily PnL
    performance_df["Annual PnL"] = pnl_df.mean() * num_periods_per_year

    # Average PnL
    performance_df["Average PnL"] = pnl_df.mean()

    # Maximum PnL
    performance_df["Maximum PnL"] = pnl_df.max()

    # Minimum PnL
    performance_df["Minimum PnL"] = pnl_df.min()

    # PnL Standard Deviation
    performance_df["Annual Standard Deviation"] = pnl_df.std() * np.sqrt(
        num_periods_per_year
    )

    # Sharpe Ratio
    performance_df["Annual Sharpe Ratio"] = (
        pnl_df.mean() / pnl_df.std() * np.sqrt(num_periods_per_year)
    )

    # Sortino Ratio
    downside_returns = pnl_df[pnl_df < 0]
    downside_std = downside_returns.std()
    performance_df["Sortino Ratio"] = (
        pnl_df.mean() / downside_std * np.sqrt(num_periods_per_year)
    )

    # Maximum Drawdown
    cumulative_returns = pnl_df.cumsum()
    rolling_max = cumulative_returns.cummax()
    drawdown = cumulative_returns - rolling_max
    performance_df["Maximum Drawdown"] = drawdown.min()

    # Calmar Ratio
    performance_df["Calmar Ratio"] = pnl_df.mean() / abs(drawdown.min())

    # Martin Ratio
    performance_df["Martin Ratio"] = pnl_df.mean() / pnl_df.std() * np.sqrt(len(pnl_df))

    # # Statistical significance of the null-hypothesis that the mean PnL is zero or negative, using one sided t-test
    # t_stat, p_value = stats.ttest_1samp(pnl_df, 0, alternative='less')
    # performance_df['T-Test p-value'] = p_value

    return performance_df.T
