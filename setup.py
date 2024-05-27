#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="valkey",
    description="Python client for Valkey forked from redis-py",
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=["Valkey", "key-value store", "database"],
    license="MIT",
    version="5.1.0b5",
    packages=find_packages(
        include=[
            "valkey",
            "valkey._parsers",
            "valkey.asyncio",
            "valkey.commands",
            "valkey.commands.bf",
            "valkey.commands.json",
            "valkey.commands.search",
            "valkey.commands.timeseries",
            "valkey.commands.graph",
            "valkey.parsers",
        ]
    ),
    package_data={"valkey": ["py.typed"]},
    include_package_data=True,
    url="https://github.com/valkey-io/valkey-py",
    project_urls={
        "Documentation": "https://valkey-py.readthedocs.io/en/latest/",
        "Changes": "https://github.com/valkey-io/valkey-py/releases",
        "Code": "https://github.com/valkey-io/valkey-py",
        "Issue tracker": "https://github.com/valkey-io/valkey-py/issues",
    },
    author="placeholder",
    author_email="placeholder@valkey.io",
    python_requires=">=3.8",
    install_requires=[
        'async-timeout>=4.0.3; python_full_version<"3.11.3"',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    extras_require={
        "hiredis": ["hiredis>=1.0.0"],
        "ocsp": ["cryptography>=36.0.1", "pyopenssl==20.0.1", "requests>=2.26.0"],
    },
)
