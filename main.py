#    decklist_analyser - Magic: the Gathering analsyis with graph theory.
#    Copyright (C) 2019 John Blundell/Jlobblet
#    Contact: 37539527+Jlobblet@users.noreply.github.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

import argparse

from modes import overlap, analysis

FUNCTION_MAP = {
    "overlap": overlap.calculate_overlap,
    "analysis": analysis.main,
}

parser = argparse.ArgumentParser()
parser.add_argument(
    "--mode", "-m", type=str, required=True, choices=FUNCTION_MAP.keys()
)
group = parser.add_mutually_exclusive_group()
group.add_argument("--profile", "-p", type=float, nargs=2)
group.add_argument("--resolution_parameter", "-r", type=float)
parser.add_argument("--graph", "-g", action="store_true")
parser.add_argument("--no-lands", action="store_true")

args = parser.parse_args()
ARG_MAP = {
    "overlap": tuple(),
    "analysis": (
        args.profile,
        args.resolution_parameter,
        args.graph,
        args.no_lands,
    ),
}
print(
    """
    decklist_analyser  Copyright (C) 2019 John Blundell/Jlobblet
    This program comes with ABSOLUTELY NO WARRANTY; license is included
    as LICENSE.
    """
)
FUNCTION_MAP[args.mode](*ARG_MAP[args.mode])
