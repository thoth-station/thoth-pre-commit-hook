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

import subprocess
import sys


def main():
    """Entrypoint for thoth-pre-commit-hook."""
    subprocess.run(["thamos", "check"])
    advise_subprocess = subprocess.run(["thamos", "advise", *sys.argv[1:]])
    return advise_subprocess.returncode


if __name__ == "__main__":
    sys.exit(main())
