#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="zops.codegen",
    use_scm_version=True,
    author="Alexandre Andrade",
    author_email="kaniabi@gmail.com",
    url="https://github.com/zerotk/zops.codegen",
    description="Generic code generation tool.",
    long_description="Generic code generation tool.",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="development environment, shell, operations, code generation",
    include_package_data=True,
    packages=["zops", "zops.codegen"],
    entry_points="""
        [zops.plugins]
        main=zops.codegen.cli:main
    """,
    install_requires=[
        "zerotk.lib",
        "zerotk.zops",
    ],
    dependency_links=[],
    setup_requires=["setuptools_scm"],
    tests_require=[
        "pytest",
        "datadiff",
    ],
    license="MIT license",
)
