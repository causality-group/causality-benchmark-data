<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** We're using the README template at: https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![BSD3 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.linkedin.com/company/causality-group">
    <img src="images/logo.png" alt="Logo" width="600" height="160">
  </a>

<h3 align="center">Causality Benchmark Data</h3>

  <p align="center">
    Showcasing Causality Group's benchmark data through a data loading library and a signal backtesting example.
    <!-- <br />
    <a href="https://github.com/causality-group/causality-benchmark-dataset"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <!-- <a href="https://github.com/causality-group/causality-benchmark-dataset">View Demo</a>
    · -->
    <a href="https://github.com/causality-group/causality-benchmark-data/issues">Report Bug</a>
    ·
    <a href="https://github.com/causality-group/causality-benchmark-data/issues/new">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#backtesting-and-data-layout">Backtesting and Data Layout</a>
      <ul>
        <li><a href="#backtesting">Backtesting</a></li>
        <li><a href="#data-layout">Data Layout</a></li>
        <li><a href="#file-description">File Description</a></li>
      </ul>
    </li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Have you ever found yourself struggling to prepare clean financial data for analysis? Have you attempted to align data from various sources?

With this repository you can explore Causality Group's curated historical dataset for academic and non-commercial use, covering the 1500 most liquid stocks in the US equities markets.

Features include:
* Liquid universe of 1500 stocks, updated monthly
* Free from survivorship bias
* Daily Open, High, Low, Close, VWAP, and Volume
* Overnight returns adjusted for splits, dividends, mergers and acquisitions
* Intraday 5-minute VWAP, spread, and volume snapshots
* SPY ETF data for hedging
* CAPM betas and residuals for market-neutral analysis

Please contact us on [LinkedIn](https://www.linkedin.com/in/markhorvath-ai) for access to the dataset!

More details [here](#usage)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]
* [![Poetry][Poetry.org]][Poetry-url]
* [![Jupyter][Jupyter.org]][Jupyter-url]
* [![Matplotlib][Matplotlib.org]][Matplotlib-url]
* [![Numpy][Numpy.org]][Numpy-url]
* [![Pandas][Pandas.org]][Pandas-url]
* [![Sklearn][Sklearn.org]][Sklearn-url]
* [![Scipy][Scipy.org]][Scipy-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow these steps to set up the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local setup:
- Python 3.9.5
- Poetry (see [installation instructions](https://python-poetry.org/docs/#installation))

### Installation

1. Clone the repository
2. Install the dependencies
```bash
poetry install
```
3. Install the pre-commit hooks
```bash
poetry run pre-commit install
```

You're all set! Pre-commit hooks will run on git commit. Ensure your changes pass all checks before pushing.

### Available Scripts
- `poetry run black`: Run the code formatter.
- `poetry run lint`: Run the linter.
- `poetry run install-ipykernel`: Install the causality kernel for Jupyter.
- `poetry run uninstall-ipykernel`: Uninstall the causality kernel for Jupyter.

> **Note:** Remember, you need to install the optional `ipykernel` group of dependencies to run the ipykernel scripts. Use `poetry install --with jupyter`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- BACKTESTING AND DATA -->
## Backtesting and Data Layout

### Backtesting

[01-Backtesting-Signals.ipynb](https://github.com/causality-group/causality-benchmark-data/blob/main/causalitydata/notebook/01-Backtesting-Signals.ipynb) serves as a minimal example of utilizing the dataset and library for quantitative analysis, alpha signal research, and backtesting.

The example showcases a daily backtest, relying on close-to-close adjusted returns of the 1500 most liquid companies in the US since 2007. Since the most liquid companies change constantly, we update our liquid universe at the start of each month. This dynamic universe is already pre-calculated in the `universe.csv` data file.

Assuming trading at the 16:00 close auction in the US, our example only uses features for alpha creation that are observable by 15:45. We plot the performance of some well-known alpha factors and invite you to experiment with building your quantitative investment model from there!

### Data Layout

All data files in the benchmark dataset have the same structure:

* Data files are in `.csv` format.
* The first row contains the header.
* Rows represent different dates in an increasing order. There is only one row per date, i.e. there is no intraday granularity inside each file.
* The first column corresponds to the index and contains the date information, at which the given value is observable:
  * Date format: `YYYY-MM-DD`.
* Every other column represents an individual asset in the universe:
  * Asset identifier format: `<ticker>_<exchange>_<CFI>`. E.g. `AAPL_XNAS_ESXXXX`.
* All files have the same number of rows and columns.

There are two types of files in the dataset, *daily* and *intraday*. *Daily* files contain data whose characteristic is that there can only be one datapoint per day, e.g. open auction price, daily volume, GICS sector information, ... . *Intraday* files contain information about the market movements during the US trading session, e.g. intraday prices and volumes. We accumulate this data in 5 minute bars. The name of *intraday* files starts with a integer identifying the bar time.

#### File Description

Here we detail the data contained in some files that might not be trivial by their name.

* **Daily**
  * `universe.csv`: Mask of the tradable universe at each date. The universe is rebalanced at the beginning of each month.
  * `ret_<cc, co, oc, oo>.csv`: Adjusted asset returns calculated on different time periods:
    * `cc`: Close-to-Close, the position is entered at the close auction and exited at the following day's close auction.
    * `co`: Close-to-Open, the position is entered at the close auction and exited at the following day's open auction.
    * `oc`: Open-to-Close, the position is entered at the open auction and exited at the same day's close auction.
    * `oo`: Open-to-Open, the position is entered at the open auction and exited at the following day's open auction.
  * `SPY_ret_<cc, co, oc, oo>.csv`: SPY ETF return. The SPY time series is placed in all asset columns for convenience.
  * `beta_<cc, co, oc, oo>.csv`: CAPM betas between assets and the SPY ETF for different time periods.
  * `resid_<cc, co, oc, oo>.csv`: CAPM residual returns on different time periods. `resid = ret - beta * SPY_ret`
* **Intraday**
  * `<hhmmss>_<close, cost, return, volume, vwas, vwap>_5m.csv`: Intraday market data snapshots at <i>hhmmss</i> bar. These backward looking bars are calculated on the time range `[t-5min, t)`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<!--
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/causality-group/causality-benchmark-dataset/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTRIBUTING -->
<!--
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- LICENSE -->
## License

Distributed under the BSD-3 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Please reach us at [LinkedIn](https://www.linkedin.com/in/markhorvath-ai) or visit our [website](https://www.causalitygroup.com)!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!--
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/causality-group/causality-benchmark-data?style=for-the-badge
[contributors-url]: https://github.com/causality-group/causality-benchmark-data/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/causality-group/causality-benchmark-data.svg?style=for-the-badge
[forks-url]: https://github.com/causality-group/causality-benchmark-data/network/members
[stars-shield]: https://img.shields.io/github/stars/causality-group/causality-benchmark-data?style=for-the-badge
[stars-url]: https://github.com/causality-group/causality-benchmark-data/stargazers
[issues-shield]: https://img.shields.io/github/issues/causality-group/causality-benchmark-data.svg?style=for-the-badge
[issues-url]: https://github.com/causality-group/causality-benchmark-data/issues
[license-shield]: https://img.shields.io/github/license/causality-group/causality-benchmark-data.svg?style=for-the-badge
[license-url]: https://github.com/causality-group/causality-benchmark-data/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/company/causality-group
<!-- [product-screenshot]: images/screenshot.png -->
[Python.org]: https://img.shields.io/badge/Python-3.9.5-blue?style=for-the-badge&logo=python&logoColor=ffdd54&labelColor=3776ab&color=3776ab
[Python-url]: https://python.org/
[Poetry.org]: https://img.shields.io/badge/Poetry-1.7.1-%233B82F6?style=for-the-badge&logo=poetry&logoColor=0B3D8D&labelColor=%233B82F6
[Poetry-url]: https://python-poetry.org/
[Jupyter.org]: https://img.shields.io/badge/jupyter-8.6.0-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white&labelColor=%23FA0F00
[Jupyter-url]: https://jupyter.org/
[Pandas.org]: https://img.shields.io/badge/pandas-2.2.0-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white&labelColor=%23150458&color=%23150458
[Pandas-url]: https://pandas.pydata.org/
[Matplotlib.org]: https://img.shields.io/badge/Matplotlib-3.8.3-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black&labelColor=%23ffffff
[Matplotlib-url]: https://matplotlib.org
[Numpy.org]: https://img.shields.io/badge/numpy-1.26.4-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white&labelColor=%23013243
[Numpy-url]: https://numpy.org
[Sklearn.org]: https://img.shields.io/badge/scikit--learn-1.0.1-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white&labelColor=%23F7931E
[Sklearn-url]: http://scikit-learn.org
[SciPy.org]: https://img.shields.io/badge/SciPy-1.12.0-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white&labelColor=%230C55A5
[Scipy-url]: https://scipy.org
