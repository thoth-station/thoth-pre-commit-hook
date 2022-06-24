"""This file sets up the thoth-pre-commit-hook module."""

import os
from setuptools import setup
from pathlib import Path


def get_install_requires():
    """Get thoth pre-commit hook installation requirements."""
    with open("requirements.txt", "r") as requirements_file:
        return [req for req in requirements_file.readlines() if req]


def get_version():
    """Get thoth pre-commit hook version."""
    with open(os.path.join("thoth/thoth_pre_commit_hook", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


VERSION = get_version()
setup(
    name="thoth_pre_commit_hook",
    entry_points={
        "console_scripts": ["thoth-advise = thoth_pre_commit_hook.thoth_advise:main"]
    },
    version=VERSION,
    url="https://github.com/thoth-station/thoth-pre-commit-hook",
    description="Get Thoth recommendations in a pre-commit hook.",
    long_description=Path("README.md").read_text(),
    author="Maya Costantini",
    author_email="mcostant@redhat.com",
    license="GPLv3+",
    packages=["thoth_pre_commit_hook"],
    package_dir={
        "thoth_pre_commit_hook": "./thoth/thoth_pre_commit_hook",
    },
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": "https://github.com/thoth-station/thoth-pre-commit-hook/",
        "Issues": "https://github.com/thoth-station/thoth-pre-commit-hook/issues",
        "Changelog": "https://github.com/thoth-station/thoth-pre-commit-hook/blob/master/CHANGELOG.md",
    },
    install_requires=get_install_requires(),
    command_options={
        "build_sphinx": {
            "version": ("setup.py", VERSION),
            "release": ("setup.py", VERSION),
        }
    },
)
