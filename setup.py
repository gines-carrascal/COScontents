# coding: utf-8

"""
    IBM COS JupyterLab Contents Manager
"""

from setuptools import setup, find_namespace_packages

NAME = "coscontents"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "ibm-cos-sdk>=2.13.0",
    "s3fs",
    "jupyter_server",
    "nbformat",
    "numpy",
    "setuptools-scm-git-archive",
    "setuptools-scm>=1.5.4",
    "setuptools>=45",
    "tornado",
    "traitlets",
]

setup(
    name=NAME,
    description="COS Contents Manage for storing Jupyterlab Notebooks in IBM Cloud Object Storage",
    author_email="gines_carrascal@es.ibm.com",
    url="https://www.ibm.com",
    keywords=["IBM", "COS", "cloud", "jupyter", "notebook"],
    install_requires=REQUIRES,
    packages=find_namespace_packages(include=["coscontents"]),
    include_package_data=True,
    zip_safe=False,
    use_scm_version={
        "version_scheme": "guess-next-dev",
        "local_scheme": "dirty-tag",
        "write_to": "coscontents/version.py",
    },
    long_description="""\
    COS Contents Manage for storing Jupyterlab Notebooks in IBM Cloud Object Storage
    """,
)
