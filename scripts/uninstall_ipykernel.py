"""Script to uninstall causality ipykernel."""

import logging
from jupyter_client.kernelspec import KernelSpecManager

# Set up logging
logging.basicConfig(level=logging.INFO)


def uninstall_ipykernel():
    """Uninstalls causality ipykernel."""
    try:
        KernelSpecManager().remove_kernel_spec("causality-forecast-darts-p3.9")
        logging.info("Successfully uninstalled causality ipykernel.")
    except Exception as e:
        logging.error("Failed to uninstall causality ipykernel.")
        logging.error(repr(e))


if __name__ == "__main__":
    uninstall_ipykernel()
