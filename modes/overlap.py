#    decklist_analyser - Magic: the Gathering analsyis with graph theory.
#    Copyright (C) 2019 John Blundell/Jlobblet
#    Contact: jlobblet-github@gmx.co.uk
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

from os import listdir, getcwd
from os.path import isfile, join

from config.CONFIG import CONFIG
from config.lands import BASICS
from .functions import create_set_from_file

decklist_directory = getcwd() + CONFIG["decklist_directory"]


def check_no_duplicates(*args):
    """Take any number of sets and return the duplicates, by pair, in
    all of the sets.

    *args is any number of sets containing any values. The union of each
    pair of sets is generated and if nonempty appended to a dictionary.
    These are numbered by the order the sets were provided in and then
    returned.
    Parameters:
    -----------
    *args: sets to check for duplicates.
    Returns:
    --------
    duplicates: dict - keys are string of the form f"{index1}, {index2}"
    and values are the union of those sets, if nonempty. Empty unions
    are omitted.
    """
    duplicates = {
        f"{index1}, {index2}": (args[index1] - BASICS)
        & (args[index2] - BASICS)
        for index1 in range(len(args) - 1)
        for index2 in range(index1 + 1, len(args))
        if (args[index1] - BASICS) & (args[index2] - BASICS)
    }
    return duplicates


def calculate_overlap():
    """Open all the files in a given directory and then check all of
    them for duplicate cards with each other.
    Returns:
    ------
    duplicates: dict - keys are string of the form f"{index1}, {index2}"
    and values are the union of those sets, if nonempty. Empty unions
    are omitted.
    See also:
    ------
    check_no_duplicates
    """
    decklists = [
        join(decklist_directory, _file)
        for _file in listdir(decklist_directory)
        if isfile(join(decklist_directory, _file))
    ]
    print(f"Found decklists: \n{decklists}")
    set_decklists = [
        create_set_from_file(decklist) for decklist in decklists
    ]
    print(check_no_duplicates(*set_decklists))
