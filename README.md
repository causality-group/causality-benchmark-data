# causality-forecast-darts
Showcasing time series forecasting and machine learning optimization with Darts.

# Installation
Follow these steps to set up the project on your local machine for development and testing purposes.

## Prerequisites
Ensure you have the following installed on your local setup
- Python 3.9
- Poetry

## Steps
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

# Available Scripts
- `poetry run pytest`: Run the tests.
- `poetry run black`: Run the code formatter.
- `poetry run lint`: Run the linter.
- `poetry run install-ipykernel`: Install the causality kernel for Jupyter.
- `poetry run uninstall-ipykernel`: Uninstall the causality kernel for Jupyter.

> **Note:** Remember, you need to install the optional `ipykernel` group of dependencies to run the ipykernel scripts. Use `poetry install --with jupyter`.
