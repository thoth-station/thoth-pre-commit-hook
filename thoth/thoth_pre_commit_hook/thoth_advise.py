#!/usr/bin/env python3
# thoth-pre-commit-hook
# Copyright(C) 2022 Maya Costantini
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Thoth pre-commit hook entrypoint."""

import configparser
import os
import re
import subprocess
import sys

from typing import List


def _setupcfg_to_requirementstxt(requirement: str) -> str:
    """Parse requirements.txt dependencies to setup.cfg format."""
    requirement_parts = requirement.split(" ")
    if len(requirement_parts) >= 1:
        version_parts = re.split(r"(^[^\d]+)", requirement_parts[-1].strip('"'))[1:]
        print(version_parts)
        requirement = requirement_parts[0] + version_parts[0] + version_parts[1]
    return requirement


def _prepare_requirementstxt_file() -> None:
    """Write a temporary requirements.txt file if requirements format is setup.cfg."""
    cfgparser = configparser.ConfigParser()
    cfgparser.read("setup.cfg")

    with open("requirements.txt", "w") as requirements_txt_file:
        for line in cfgparser["options"]["install_requires"]:
            requirements_txt_file.write(_setupcfg_to_requirementstxt(line))


def _cleanup_requirementstxt_file() -> None:
    """Clean up requirements.txt created for dependency resolution."""
    if os.path.isfile("requirements.txt"):
        os.remove("requirements.txt")


def _run_advise() -> int:
    """Run thamos advise on the current repository."""
    # thamos doesn't accept actual paths and that's what pre-commit is passing
    thamos_args: List = []
    for a in sys.argv:
        if not os.path.exists(a):
            thamos_args += a

    advise_subprocess = subprocess.run(["thamos", "advise"] + thamos_args)
    return advise_subprocess.returncode


def main():
    """Entrypoint for thoth-pre-commit-hook."""
    subprocess.run(["thamos", "config", "--no-interactive"])
    subprocess.run(["thamos", "check"])

    if os.path.isfile("setup.cfg") and not os.path.isfile("requirements.txt"):
        _prepare_requirementstxt_file()
        _run_advise()
        _cleanup_requirementstxt_file()

    else:
        _run_advise()


if __name__ == "__main__":
    sys.exit(main())
