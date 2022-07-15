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

import re
import subprocess
import sys


def main():
    """Entrypoint for thoth-pre-commit-hook."""
    subprocess.run(["thamos", "config", "--no-interactive"])
    subprocess.run(["thamos", "check"])

    thamos_args = sys.argv[1:]

    advise_subprocess = subprocess.run(
        ["thamos", "advise"] + thamos_args, stdout=subprocess.PIPE
    )
    stdout = advise_subprocess.stdout.decode(sys.getdefaultencoding())
    # let's print advise's output to the console nevertheless
    print(stdout)
    try:
        advise_id = re.findall(r"adviser-\w+-\w+", stdout)[0]
    except IndexError:
        advise_id = None

    if advise_id:
        print(f"Advise output: https://thoth-station.ninja/search/advise/{advise_id}/")
    return advise_subprocess.returncode


if __name__ == "__main__":
    sys.exit(main())
