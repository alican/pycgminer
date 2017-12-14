import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pycgminer",
    version="0.1.2",
    author="Alican Toprak",
    author_email="mail@alican.eu",
    description="Cgminer RPC API wrapper.",
    license="MIT",
    keywords="cgminer",
    url="https://github.com/tsileo/pycgminer",
    py_modules=["pycgminer"],
    long_description=read("README.rst"),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
    ],
#    test_suite="test_globster",
)
