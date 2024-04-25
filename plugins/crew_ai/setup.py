"""
Setup configuration for Composio CrewAI plugin
"""

import os
from pathlib import Path

from setuptools import setup


version = os.environ.get("RELEASE_VERSION", "0.2.15")

setup(
    name="composio_crewai",
    version=version,
    author="Himanshu",
    author_email="himanshu@composio.dev",
    description="Use Composio to get an array of tools with your CrewAI agent.",
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/SamparkAI/composio_sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9,<4",
    install_requires=[
        "composio_langchain==0.2.16",
    ],
    include_package_data=True,
)