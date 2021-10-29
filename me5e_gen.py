#!/usr/bin/env python
"""Quickly roll a new character for both players and Game Masters"""

# gen.py
# Mass Effect 5e Character Generator v 1.0.0
# Nicholas Cheek

# Copyright (C) 2021  Nicholas Cheek.
#
# This program is free software: you can redistibute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Imports
from math import floor
from random import choice, randint

# Variables
SPECIES = [
    "angara",
    "asari",
    "batarian",
    "drell",
    "elcor",
    "geth",
    "hanar",
    "human",
    "krogan",
    "prothean",
    "quarian",
    "salarian",
    "turian",
    "volus",
    "vorcha",
]
CHAR_CLASSES = [
    "adept",
    "engineer",
    "infiltrator",
    "sentinel",
    "soldier",
    "vanguard"
]
BACKGROUNDS = [
    "artisan",
    "bureaucrat",
    "colonist",
    "crewman",
    "criminal",
    "doctor",
    "entertainer",
    "escort",
    "experient",
    "faction agent",
    "pilot",
    "scholar",
    "scrapper",
    "sys op",
    "urchin",
    "veteran"
]

#Functions
def generate_species():
    """Generate a species"""
    species = choice(SPECIES)
    return species


def generate_class():
    """Generate a class"""
    char_class = choice(CHAR_CLASSES)
    return char_class


def generate_background():
    """Generate a background"""
    background = choice(BACKGROUNDS)
    return background


def generate_stat():
    """Generate a stat block"""
    stat_array = []
    count = 0
    while count < 4:
        roll = randint(1, 6)
        stat_array.append(roll)
        count += 1
    stat_array.sort(reverse=True)
    stat_array.pop()
    stat = sum(stat_array)
    if stat < 8:
        stat = 8
    return stat


def stat_mod(mod):
    """Generate stat modifiers"""
    # Modifier = (Stat / 2) - 5 rounded down
    return int(floor((mod / 2) - 5))


def generate_character_stats():
    """Generate character stats"""
    character_stats = []
    count = 0
    while count < 6:
        roll = generate_stat()
        character_stats.append(roll)
        count += 1
    character_stats.sort(reverse=True)
    return character_stats


class Character:
    """Generate character"""

    def __init__(self):
        self.species = generate_species()
        self.char_class = generate_class()
        self.background = generate_background()
        self.stats = generate_character_stats()


NEW_CHARACTER = Character()

print("Species:", NEW_CHARACTER.species.capitalize())
print("Class:", NEW_CHARACTER.char_class.capitalize())
print("Background:", NEW_CHARACTER.background.capitalize())
print("Stats:", NEW_CHARACTER.stats)
