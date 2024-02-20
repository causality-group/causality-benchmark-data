"""Script to install causality ipykernel."""

from ipykernel.kernelspec import install


def install_ipykernel():
    """Installs causality ipykernel."""
    install(user=True, kernel_name="cauality-forecast-darts-p3.9")


if __name__ == "__main__":
    install_ipykernel()
