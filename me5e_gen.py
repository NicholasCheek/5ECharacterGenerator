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
    "experiment",
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
        self.weapons = []
        self.armor = []



        # Hit Die
        hit_die_sizes = {
            "adept": 6,
            "engineer": 8,
            "infiltrator": 8,
            "sentinel": 10,
            "soldier": 10,
            "vanguard": 12
        }
        self.hit_die = hit_die_sizes[self.char_class]


        #Adept
        if self.char_class == "adept":
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            self.charisma = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dexterity = randint(0, 2)
            self.dexterity = self.stats[dexterity]
            self.stats.pop(dexterity)
            constitution = randint(0, 1)
            self.constitution = self.stats[constitution]
            self.stats.pop(constitution)
            self.intelligence = self.stats[0]
            weapon1 = randint(0, 1)
            if weapon1 == 0:
                self.weapons.append("M-3 Predator")
            else:
                self.weapons.append("M-4 Shuriken")
            weapon2 = randint(0, 1)
            if weapon2 == 0:
                self.weapons.append("Omni-Blade")
            else:
                self.weapons.append("Monomolecular Blade")
            self.armor.append("Stock Light Armor")
        #Engineer
        elif self.char_class == "engineer":
            self.intelligence = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dexterity = randint(0, 2)
            self.dexterity = self.stats[dexterity]
            self.stats.pop(dexterity)
            wisdom = randint(0, 1)
            self.wisdom = self.stats[wisdom]
            self.stats.pop(wisdom)
            self.charisma = self.stats[0]
            weapon1 = randint(0, 2)
            if weapon1 == 0:
                self.weapons.append("M-3 Predator")
            elif weapon1 == 1:
                self.weapons.append("M-4 Shuriken")
            else:
                self.weapons.append("M-8 Avenger")
            weapon2 = randint(0, 2)
            if weapon2 == 0:
                self.weapons.append("Omni-Blade")
            elif weapon2 == 1:
                self.weapons.append("Omni-Taser")
            else:
                self.weapons.append("Omni-Torch")
            armor1 = randint(0, 1)
            if armor1 == 0:
                self.armor.append("Stock Light Armor")
            else:
                self.armor.append("Stock Medium Armor")
        #Infiltrator
        elif self.char_class == "infiltrator":
            dexterity = randint(0, 1)
            self.dexterity = self.stats[dexterity]
            self.stats.pop(dexterity)
            self.intelligence = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            constitution = randint(0, 2)
            self.constitution = self.stats[constitution]
            self.stats.pop(constitution)
            wisdom = randint(0, 1)
            self.wisdom = self.stats[wisdom]
            self.stats.pop(wisdom)
            self.charisma = self.stats[0]
            weapon1 = randint(0, 2)
            if weapon1 == 0:
                self.weapons.append("M-3 Predator")
            elif weapon1 == 1:
                self.weapons.append("M-4 Shuriken")
            else:
                self.weapons.append("M-92 Mantis")
            weapon2 = randint(0, 2)
            if weapon2 == 0:
                self.weapons.append("Omni-Blade")
            elif weapon2 == 1:
                self.weapons.append("Omni-Taser")
            else:
                self.weapons.append("Monomolecular Blade")
            self.armor.append("Stock Light Armor")
        #Sentinel
        elif self.char_class == "sentinel":
            intelligence = randint(0, 2)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            wisdom =randint(0, 1)
            self.wisdom = self.stats[wisdom]
            self.stats.pop(wisdom)
            self.charisma = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 2)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dexterity = randint(0, 1)
            self.dexterity = self.stats[dexterity]
            self.stats.pop(dexterity)
            self.constitution = self.stats[0]
            weapon1 = randint(0, 2)
            if weapon1 == 0:
                self.weapons.append("M-3 Predator")
            elif weapon1 == 1:
                self.weapons.append("M-4 Shuriken")
            else:
                self.weapons.append("M-8 Avenger")
            weapon2 = randint(0, 3)
            if weapon2 == 0:
                self.weapons.append("Omni-Blade")
            elif weapon2 == 1:
                self.weapons.append("Omni-Hammer")
            elif weapon2 == 2:
                self.weapons.append("Monomolecular Blade")
            else:
                self.weapons.append("Riot Shield")
            armor1 = randint(0, 2)
            if armor1 == 0:
                self.armor.append("Stock Light Armor")
            elif armor1 == 1:
                self.armor.append("Stock Medium Armor")
            else:
                self.armor.append("Stock Heavy Armor")
        #Soldier
        elif self.char_class == "soldier":
            strength = randint(0, 1)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dexterity = randint(0, 1)
            self.dexterity = self.stats[dexterity]
            self.stats.pop(dexterity)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            intelligence = randint(0, 2)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            wisdom = randint(0, 1)
            self.wisdom = self.stats[wisdom]
            self.stats.pop(wisdom)
            self.charisma = self.stats[0]
            weapon1 = randint(0, 4)
            if weapon1 == 0:
                self.weapons.append("M-3 Predator")
            elif weapon1 == 1:
                self.weapons.append("M-4 Shuriken")
            elif weapon1 == 2:
                self.weapons.append("M-8 Avenger")
            elif weapon1 == 3:
                self.weapons.append("M-92 Mantis")
            else:
                self.weapons.append("M-23 Katana")
            weapon2 = randint(0, 1)
            if weapon2 == 0:
                self.weapons.append("Omni-Blade")
            else:
                self.weapons.append("Omni-Hammer")
            armor1 = randint(0, 2)
            if armor1 == 0:
                self.armor.append("Stock Light Armor")
            elif armor1 == 1:
                self.armor.append("Stock Medium Armor")
            else:
                self.armor.append("Stock Heavy Armor")
        #Vanguard
        elif self.char_class == "vanguard":
            strength = randint(0, 1)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            intelligence = randint(0, 2)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            dexterity = randint(0, 1)
            self.dexterity = self.stats[dexterity]
            self.stats.pop(dexterity)
            self.charisma = self.stats[0]
            weapon1 = randint(0, 2)
            if weapon1 == 0:
                self.weapons.append("M-3 Predator")
            elif weapon1 == 1:
                self.weapons.append("M-4 Shuriken")
            else:
                self.weapons.append("M-23 Katana")
            weapon2 = randint(0, 3)
            if weapon2 == 0:
                self.weapons.append("Omni-Blade")
            elif weapon2 == 1:
                self.weapons.append("Omni-Hammer")
            elif weapon2 == 2:
                self.weapons.append("Monomolecular Blade")
            else:
                self.weapons.append("Riot Shield")
            armor1 = randint(0, 1)
            if armor1 == 0:
                self.armor.append("Stock Light Armor")
            else:
                self.armor.append("Stock Medium Armor")

            
        self.hit_points = self.hit_die + stat_mod(self.constitution)
            
        



NEW_CHARACTER = Character()

print("Species:", NEW_CHARACTER.species.capitalize())
print("Class:", NEW_CHARACTER.char_class.capitalize())
print("Background:", NEW_CHARACTER.background.capitalize())
print("Hit Points:", NEW_CHARACTER.hit_points)
print("STR:", NEW_CHARACTER.strength)
print("DEX:", NEW_CHARACTER.dexterity)
print("CON:", NEW_CHARACTER.constitution)
print("INT:", NEW_CHARACTER.intelligence)
print("WIS:", NEW_CHARACTER.wisdom)
print("CHA:", NEW_CHARACTER.charisma)
print("Weapons:", NEW_CHARACTER.weapons)
print("Armor:", NEW_CHARACTER.armor)
