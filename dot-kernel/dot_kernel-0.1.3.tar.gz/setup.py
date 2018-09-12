# -*- coding: utf-8 -*-

import subprocess
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


class DevelopJupyterKernel(develop):
    """
    Install jupyter kernel.
    To verify your installation:
        jupyter kernelspec list

    Should print your "Avalkiable kernels"
    """

    def run(self):
        develop.run(self)
        subprocess.check_output(
            "jupyter kernelspec install dot_kernel_spec",
            stderr=subprocess.STDOUT,
            shell=True,
        )


class InstallJupyterKernel(install):
    """
    Install jupyter kernel.
    To verify your installation:
        jupyter kernelspec list

    Should print your "Avalkiable kernels"
    """

    def run(self):
        install.run(self)
        subprocess.check_output(
            "jupyter kernelspec install dot_kernel_spec",
            stderr=subprocess.STDOUT,
            shell=True,
        )


setup(
    name="dot_kernel",
    version="0.1.3",
    url="https://github.com/laixintao/jupyter-dot-kernel",
    author="laixintao",
    author_email="laixintao1995@163.com",
    description="Writing dot language and render in jupyter.",
    cmdclass={"install": InstallJupyterKernel, "develop": DevelopJupyterKernel},
    packages=find_packages(),
    install_requires=["graphviz", "jupyter"],
)
