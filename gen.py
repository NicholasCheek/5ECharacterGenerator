#!/usr/bin/env python
"""Quickly roll a new character for both players and Game Masters"""

# gen.py
# D20 Character Generator v 1.0.0
# Nicholas Cheek

# Copyright (C) 2020  Nicholas Cheek.
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
RACES = [
    "dragonborn",
    "dwarf",
    "elf",
    "gnome",
    "halfling",
    "half-orc",
    "human",
    "tiefling",
]
CHAR_CLASSES = [
    "barbarian",
    "bard",
    "cleric",
    "druid",
    "fighter",
    "monk",
    "paladin",
    "ranger",
    "rogue",
    "sorcerer",
    "warlock",
    "wizard",
]
# Dragonborn
DRACONIC_ANCESTRY = [
    "Black",
    "Blue",
    "Brass",
    "Bronze",
    "Copper",
    "Gold",
    "Green",
    "Red",
    "Silver",
    "White",
]
DRAGONBORN_MALE = [
    "Arjhan",
    "Balasar",
    "Bharash",
    "Donaar",
    "Ghesh",
    "Heskan",
    "Kriv",
    "Medrash",
    "Mehen",
    "Nadar",
    "Pandjed",
    "Patrin",
    "Rhogar",
    "Shamash",
    "Shedinn",
    "Tarhun",
    "Torinn",
]
DRAGONBORN_FEMALE = [
    "Akra",
    "Biri",
    "Daar",
    "Farideh",
    "Harann",
    "Havilar",
    "Jheri",
    "Kava",
    "Korinn",
    "Mishann",
    "Nala",
    "Perra",
    "Raiann",
    "Sora",
    "Surina",
    "Thava",
    "Uadjit",
]
DRAGONBORN_CLAN = [
    "Clethtinthiallor",
    "Daardendrian",
    "Delmirev",
    "Drachedandion",
    "Fenkenkabradon",
    "Kepeshkmolik",
    "Kerrhylon",
    "Kimbatuul",
    "Linxakasendalor",
    "Myastan",
    "Nemmonis",
    "Norixius",
    "Ophinshtalajiir",
    "Prexijandilin",
    "Shestendeliath",
    "Turnuroth",
    "Verthisathurgiesh",
    "Yarjerit",
]
# Dwarf
DWARF_MALE = [
    "Adrik",
    "Alberich",
    "Baern",
    "Barendd",
    "Brottor",
    "Bruenor",
    "Dain",
    "Darrak",
    "Delg",
    "Eberk",
    "Einkil",
    "Fargrim",
    "Flint",
    "Gardain",
    "Harbek",
    "Kildrak",
    "Morgran",
    "Orsik",
    "Oskar",
    "Rangrim",
    "Rurik",
    "Taklinn",
    "Thoradin",
    "Thorin",
    "Tordek",
    "Traubon",
    "Travok",
    "Ulfgar",
    "Veit",
    "Vondal",
]
DWARF_FEMALE = [
    "Amber",
    "Artin",
    "Audhild",
    "Bardryn",
    "Dagnal",
    "Diesa",
    "Eldeth",
    "Falkrunn",
    "Finellen",
    "Gunnloda",
    "Gurdis",
    "Helja",
    "Hlin",
    "Kathra",
    "Kristyd",
    "Ilde",
    "Liftrasa",
    "Mardred",
    "Riswynn",
    "Sannl",
    "Torbera",
    "Torgga",
    "Vista",
]
DWARF_CLAN = [
    "Balderk",
    "Battlehammer",
    "Brawnanvil",
    "Dankil",
    "Fireforge",
    "Frostbeard",
    "Gorunn",
    "Holderhek",
    "Ironfist",
    "Loderr",
    "Lutgehr",
    "Rumnaheim",
    "Strakeln",
    "Torunn",
    "Ungart",
]
# Elf
ELF_MALE = [
    "Adran",
    "Aelar",
    "Aramil",
    "Arannis",
    "Aust",
    "Beiro",
    "Berrian",
    "Carric",
    "Enialis",
    "Erdan",
    "Erevan",
    "Galinndan",
    "Hadarai",
    "Heian",
    "Himo",
    "Immeral",
    "Ivellios",
    "Laucian",
    "Mindartis",
    "Paelias",
    "Peren",
    "Quarion",
    "Riardon",
    "Rolen",
    "Soveliss",
    "Thamior",
    "Tharivol",
    "Theren",
    "Varis",
]
ELF_FEMALE = [
    "Adrie",
    "Althaea",
    "Anastianna",
    "Andraste",
    "Antinua",
    "Bethrynna",
    "Birel",
    "Caelynn",
    "Drusilia",
    "Enna",
    "Felosial",
    "Ielenia",
    "Jelenneth",
    "Keyleth",
    "Leshanna",
    "Lia",
    "Meriele",
    "Mialee",
    "Naivara",
    "Quelenna",
    "Quillathe",
    "Sariel",
    "Shanairra",
    "Shava",
    "Silaqui",
    "Theirasta",
    "Thia",
    "Vadania",
    "Valanthe",
    "Xanaphia",
]
ELF_FAMILY = [
    "Amakiir (Gemflower)",
    "Amastacia (Starflower)",
    "Galanodel (Moonwhisper)",
    "Holimion (Diamonddew)",
    "Ilphelkiir (Gemblossom)",
    "Liadon (Silverfrond)",
    "Meliamne (Oakenheel)",
    "Na&iuml;lo (Nightbreeze)",
    "Siannodel (Moonbrook)",
    "Xiloscient (Goldpetal)",
]
# Gnome
GNOME_MALE = [
    "Alston",
    "Alvyn",
    "Boddynock",
    "Brocc",
    "Burgell",
    "Dimble",
    "Eldon",
    "Erky",
    "Fonkin",
    "Frug",
    "Gerbo",
    "Gimble",
    "Glim",
    "Jebeddo",
    "Kellen",
    "Namfoodle",
    "Orryn",
    "Roondar",
    "Seebo",
    "Sindri",
    "Warryn",
    "Wrenn",
    "Zook",
]
GNOME_FEMALE = [
    "Bimpnottin",
    "Breena",
    "Caramip",
    "Carlin",
    "Donella",
    "Duvamil",
    "Ella",
    "Ellyjobell",
    "Ellywick",
    "Lilli",
    "Loopmottin",
    "Lorilla",
    "Mardnab",
    "Nissa",
    "Nyx",
    "Oda",
    "Orla",
    "Roywyn",
    "Shamil",
    "Tana",
    "Waywocket",
    "Zanna",
]
GNOME_NICKNAME = [
    "'Aleslosh'",
    "'Ashhearth'",
    "'Badger'",
    "'Cloak'",
    "'Doublelock'",
    "'Filchbatter'",
    "'Fnipper'",
    "'Ku'",
    "'Nim'",
    "'Oneshoe'",
    "'Pock'",
    "'Sparklegem'",
    "'Stumbleduck'",
]
GNOME_CLAN = [
    "Beren",
    "Daergel",
    "Folkor",
    "Garrick",
    "Nackle",
    "Murnig",
    "Ningel",
    "Raulnor",
    "Scheppen",
    "Timbers",
    "Turren",
]
# Halfling
HALFLING_MALE = [
    "Alton",
    "Ander",
    "Cade",
    "Corrin",
    "Eldon",
    "Errich",
    "Finnan",
    "Garret",
    "Lindal",
    "Lyle",
    "Merric",
    "Milo",
    "Osborn",
    "Perrin",
    "Reed",
    "Roscoe",
    "Wellby",
]
HALFLING_FEMALE = [
    "Andry",
    "Bree",
    "Callie",
    "Cora",
    "Euphemia",
    "Jillian",
    "Kithri",
    "Lavinia",
    "Lidda",
    "Merla",
    "Nedda",
    "Paela",
    "Portia",
    "Seraphina",
    "Shaena",
    "Trym",
    "Vani",
    "Verna",
]
HALFLING_FAMILY = [
    "Brushgather",
    "Goodbarrel",
    "Greenbottle",
    "High-hill",
    "Hilltopple",
    "Leagallow",
    "Tealeaf",
    "Thorngage",
    "Tosscobble",
    "Underbough",
]
# Half Orc
HALF_ORC_MALE = [
    "Dench",
    "Feng",
    "Gell",
    "Henk",
    "Holg",
    "Imsh",
    "Keth",
    "Krusk",
    "Mhurren",
    "Ront",
    "Shump",
    "Thonk",
]
HALF_ORC_FEMALE = [
    "Baggi",
    "Emen",
    "Engong",
    "Kansif",
    "Myev",
    "Neega",
    "Ovak",
    "Ownka",
    "Shautha",
    "Sutha",
    "Vola",
    "Volen",
    "Yevelda",
]
# Human
HUMAN_ETHNICITIES = [
    "calishite",
    "chondathian",
    "damaran",
    "illuskan",
    "mulan",
    "rashemi",
    "shou",
    "tethyrian",
    "turami",
]
# Tiefling
TIEFLING_MALE = [
    "Akmenos",
    "Amnon",
    "Barakas",
    "Damakos",
    "Ekemon",
    "Iados",
    "Kairon",
    "Leucis",
    "Melech",
    "Mordai",
    "Morthos",
    "Pelaios",
    "Skamos",
    "Therai",
]
TIEFLING_FEMALE = [
    "Akta",
    "Anakis",
    "Bryseis",
    "Criella",
    "Damaia",
    "Ea",
    "Kallista",
    "Lerissa",
    "Makaria",
    "Nemeia",
    "Orianna",
    "Phelaia",
    "Rieta",
]


# Functions
def generate_race():
    """Generate a race"""
    race = choice(RACES)
    return race


def generate_class():
    """Generate a class"""
    char_class = choice(CHAR_CLASSES)
    return char_class


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
        self.race = generate_race()
        self.char_class = generate_class()
        self.stats = generate_character_stats()

        if self.char_class == "barbarian":
            self.strength = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            dex = randint(0, 3)
            self.dexterity = self.stats[dex]
            self.stats.pop(dex)
            intelligence = randint(0, 2)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            wis = randint(0, 1)
            self.wisdom = self.stats[wis]
            self.stats.pop(wis)
            self.charisma = self.stats[0]
            self.hit_die = 12
        elif self.char_class == "bard":
            self.charisma = self.stats[0]
            self.stats.pop(0)
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            con = randint(0, 2)
            self.constitution = self.stats[con]
            self.stats.pop(con)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.wisdom = self.stats[0]
            self.hit_die = 8
        elif self.char_class == "cleric":
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 1)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            dex = randint(0, 2)
            self.dexterity = self.stats[dex]
            self.stats.pop(dex)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.charisma = self.stats[0]
            self.hit_die = 8
        elif self.char_class == "druid":
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dex = randint(0, 2)
            self.dexterity = self.stats[dex]
            self.stats.pop(dex)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.charisma = self.stats[0]
            self.hit_die = 8
        elif self.char_class == "fighter":
            if randint(0, 1):  # Coin toss
                self.strength = self.stats[0]
                self.stats.pop(0)
                if randint(0, 2):  # 1 in 3
                    self.intelligence = self.stats[0]
                    self.stats.pop(0)
                    con = randint(0, 3)
                    self.constitution = self.stats[con]
                    self.stats.pop(con)
                    dex = randint(0, 2)
                    self.dexterity = self.stats[dex]
                    self.stats.pop(dex)
                    wis = randint(0, 1)
                    self.wisdom = self.stats[wis]
                    self.stats.pop(wis)
                    self.charisma = self.stats[0]
                else:
                    self.constitution = self.stats[0]
                    self.stats.pop(0)
                    dex = randint(0, 3)
                    self.dexterity = self.stats[dex]
                    self.stats.pop(dex)
                    intelligence = randint(0, 2)
                    self.intelligence = self.stats[intelligence]
                    wis = randint(0, 1)
                    self.wisdom = self.stats[wis]
                    self.stats.pop(wis)
                    self.charisma = self.stats[0]
            else:
                self.dexterity = self.stats[0]
                self.stats.pop(0)
                if randint(0, 2):  # 1 in 3
                    self.intelligence = self.stats[0]
                    self.stats.pop(0)
                    strength = randint(0, 3)
                    self.strength = self.stats[strength]
                    self.stats.pop(strength)
                    con = randint(0, 2)
                    self.constitution = self.stats[con]
                    self.stats.pop(con)
                    wis = randint(0, 1)
                    self.wisdom = self.stats[wis]
                    self.stats.pop(wis)
                    self.charisma = self.stats[0]
                else:
                    self.constitution = self.stats[0]
                    self.stats.pop(0)
                    strength = randint(0, 3)
                    self.strength = self.stats[strength]
                    self.stats.pop(strength)
                    intelligence = randint(0, 2)
                    self.intelligence = self.stats[intelligence]
                    wis = randint(0, 1)
                    self.wisdom = self.stats[wis]
                    self.stats.pop(wis)
                    self.charisma = self.stats[0]
            self.hit_die = 10
        elif self.char_class == "monk":
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            con = randint(0, 2)
            self.constitution = self.stats[con]
            self.stats.pop(con)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.charisma = self.stats[0]
            self.hit_die = 8
        elif self.char_class == "paladin":
            self.strength = self.stats[0]
            self.stats.pop(0)
            self.charisma = self.stats[0]
            self.stats.pop(0)
            dex = randint(0, 3)
            self.dexterity = self.stats[dex]
            self.stats.pop(dex)
            con = randint(0, 2)
            self.constitution = self.stats[con]
            self.stats.pop(con)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.wisdom = self.stats[0]
            self.hit_die = 10
        elif self.char_class == "ranger":
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            con = randint(0, 2)
            self.constitution = self.stats[con]
            self.stats.pop(con)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.charisma = self.stats[0]
            self.hit_die = 10
        elif self.char_class == "rogue":
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            if randint(0, 1):  # Coin toss
                self.intelligence = self.stats[0]
                self.stats.pop(0)
                strength = randint(0, 3)
                self.strength = self.stats[strength]
                self.stats.pop(strength)
                con = randint(0, 2)
                self.constitution = self.stats[con]
                self.stats.pop(con)
                wis = randint(0, 1)
                self.wisdom = self.stats[wis]
                self.stats.pop(wis)
                self.charisma = self.stats[0]
            else:
                self.charisma = self.stats[0]
                self.stats.pop(0)
                strength = randint(0, 3)
                self.strength = self.stats[strength]
                self.stats.pop(strength)
                con = randint(0, 2)
                self.constitution = self.stats[con]
                self.stats.pop(con)
                wis = randint(0, 1)
                self.wisdom = self.stats[wis]
                self.stats.pop(wis)
                self.intelligence = self.stats[0]
            self.hit_die = 8
        elif self.char_class == "sorcerer":
            self.charisma = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dex = randint(0, 2)
            self.dexterity = self.stats[dex]
            self.stats.pop(dex)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.wisdom = self.stats[0]
            self.hit_die = 6
        elif self.char_class == "warlock":
            self.charisma = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            strength = randint(0, 3)
            self.strength = self.stats[strength]
            self.stats.pop(strength)
            dex = randint(0, 2)
            self.dexterity = self.stats[dex]
            self.stats.pop(dex)
            intelligence = randint(0, 1)
            self.intelligence = self.stats[intelligence]
            self.stats.pop(intelligence)
            self.wisdom = self.stats[0]
            self.hit_die = 6
        elif self.char_class == "wizard":
            self.intelligence = self.stats[0]
            self.stats.pop(0)
            if randint(0, 1):  # Coin toss
                self.constitution = self.stats[0]
                self.stats.pop(0)
                if randint(0, 7):  # 1 in 8
                    self.charisma = self.stats[0]
                    self.stats.pop(0)
                    strength = randint(0, 2)
                    self.strength = self.stats[strength]
                    self.stats.pop(strength)
                    dex = randint(0, 1)
                    self.dexterity = self.stats[dex]
                    self.stats.pop(dex)
                    self.wisdom = self.stats[0]
                else:
                    strength = randint(0, 3)
                    self.strength = self.stats[strength]
                    self.stats.pop(strength)
                    dex = randint(0, 2)
                    self.dexterity = self.stats[dex]
                    self.stats.pop(dex)
                    wis = randint(0, 1)
                    self.wisdom = self.stats[wis]
                    self.stats.pop(wis)
                    self.charisma = self.stats[0]
            else:
                self.dexterity = self.stats[0]
                self.stats.pop(0)
                if randint(0, 7):  # 1 in 8
                    self.charisma = self.stats[0]
                    self.stats.pop(0)
                    strength = randint(0, 2)
                    self.strength = self.stats[strength]
                    self.stats.pop(strength)
                    con = randint(0, 1)
                    self.constitution = self.stats[con]
                    self.stats.pop(con)
                    self.wisdom = self.stats[0]
                else:
                    strength = randint(0, 3)
                    self.strength = self.stats[strength]
                    self.stats.pop(strength)
                    con = randint(0, 2)
                    self.constitution = self.stats[con]
                    self.stats.pop(con)
                    wis = randint(0, 1)
                    self.wisdom = self.stats[wis]
                    self.stats.pop(wis)
                    self.charisma = self.stats[0]
            self.hit_die = 6

        if self.race == "dragonborn":
            self.strength += 2
            self.charisma += 1
            self.subrace = choice(DRACONIC_ANCESTRY)
            self.name = (
                choice(DRAGONBORN_MALE + DRAGONBORN_FEMALE) + " "
                + choice(DRAGONBORN_CLAN)
            )
        elif self.race == "dwarf":
            self.constitution += 2
            sub_race = randint(0, 1)
            if sub_race == 0:
                self.subrace = "Hill dwarf"
                self.wisdom += 1
            else:
                self.subrace = "Mountain dwarf"
                self.strength += 2
            self.name = (
                choice(DWARF_MALE + DWARF_FEMALE) + " "
                + choice(DWARF_CLAN)
            )
        elif self.race == "elf":
            self.dexterity += 2
            sub_race = randint(0, 1)
            if sub_race == 0:
                self.subrace = "High elf"
                self.intelligence += 1
            else:
                self.subrace = "Wood elf"
                self.wisdom += 1
            self.name = (
                choice(ELF_MALE + ELF_FEMALE) + " "
                + choice(ELF_FAMILY)
            )
        elif self.race == "gnome":
            self.intelligence += 2
            sub_race = randint(0, 1)
            if sub_race == 0:
                self.subrace = "Deep gnome"
                self.dexterity += 1
            else:
                self.subrace = "Rock gnome"
                self.constitution += 1
            self.name = (
                choice(GNOME_MALE + GNOME_FEMALE) + " "
                + choice(GNOME_NICKNAME) + " "
                + choice(GNOME_CLAN)
            )
        # elif self.race = "half elf":
        elif self.race == "halfling":
            self.dexterity += 2
            sub_race = randint(0, 1)
            if sub_race == 0:
                self.subrace = "Lightfoot halfling"
                self.charisma += 1
            else:
                self.subrace = "Stout halfling"
                self.constitution += 1
            self.name = (
                choice(HALFLING_MALE + HALFLING_FEMALE) + " "
                + choice(HALFLING_FAMILY)
            )
        elif self.race == "half-orc":
            self.subrace = "N/A"
            self.strength += 2
            self.constitution += 1
            self.name = choice(HALF_ORC_MALE + HALF_ORC_FEMALE)
        elif self.race == "human":
            self.subrace = "N/A"
            self.strength += 1
            self.constitution += 1
            self.dexterity += 1
            self.intelligence += 1
            self.wisdom += 1
            self.charisma += 1
            self.name = "N/A"
        elif self.race == "tiefling":
            self.subrace = "N/A"
            self.charisma += 2
            self.intelligence += 1
            self.name = choice(TIEFLING_MALE + TIEFLING_FEMALE)

        self.hit_points = self.hit_die + stat_mod(self.constitution)
        if self.subrace == "Hill dwarf":
            self.hit_points += 1


NEW_CHARACTER = Character()

print("Name:", NEW_CHARACTER.name)
print("Race:", NEW_CHARACTER.race.capitalize())
print("Subrace:", NEW_CHARACTER.subrace)
print("Class:", NEW_CHARACTER.char_class.capitalize())
print("STR:", NEW_CHARACTER.strength)
print("DEX:", NEW_CHARACTER.dexterity)
print("CON:", NEW_CHARACTER.constitution)
print("INT:", NEW_CHARACTER.intelligence)
print("WIS:", NEW_CHARACTER.wisdom)
print("CHA:", NEW_CHARACTER.charisma)
print("Hit Points:", NEW_CHARACTER.hit_points)
