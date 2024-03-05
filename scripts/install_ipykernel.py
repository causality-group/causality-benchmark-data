"""Script to install causality ipykernel."""

import logging
from ipykernel.kernelspec import install

# Set up logging
logging.basicConfig(level=logging.INFO)


def install_ipykernel():
    """Installs causality ipykernel."""
    try:
        install(user=True, kernel_name="causalitydata-p3.9")
        logging.info("Successfully installed causality ipykernel.")
    except Exception as e:
        logging.error("Failed to install causality ipykernel.")
        logging.error(repr(e))


if __name__ == "__main__":
    install_ipykernel()
