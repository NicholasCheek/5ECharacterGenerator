from random import randint, choice

def generate_race():
    races = ['dragonborn', 'dwarf', 'elf', 'gnome', 'halfling', 'half-orc', 'human', 'tiefling']
    race = choice(races)
    return race

def generate_class():
    char_classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
    char_class = choice(char_classes)
    return char_class

def generate_sex():
    sex = ['male', 'female']
    char_sex = choice(sex)
    return char_sex

def generate_stat():
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

def stat_mod(x):
    if x == 8 or x == 9:
        return -1
    elif x == 10 or x == 11:
        return 0
    elif x == 12 or x == 13:
        return 1
    elif x == 14 or x == 15:
        return 2
    elif x == 16 or x == 17:
        return 3
    elif x == 18 or x == 19:
        return 4
    else:
        return 5
    
def generate_character_stats():
    character_stats = []
    count = 0
    while count < 6:
        roll = generate_stat()
        character_stats.append(roll)
        count += 1
    character_stats.sort(reverse=True)
    return character_stats

class Character():
    def __init__(self):
        self.sex = generate_sex()
        self.race = generate_race()
        self.char_class = generate_class()
        self.stats = generate_character_stats()

        if self.char_class == 'barbarian':
            self.strength = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            d = randint(0,3)
            self.dexterity = self.stats[d]
            self.stats.pop(d)
            i = randint(0,2)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            w = randint(0,1)
            self.wisdom = self.stats[w]
            self.stats.pop(w)
            self.charisma = self.stats[0]
            self.hit_die = 12
        elif self.char_class == 'bard':
            self.charisma = self.stats[0]
            self.stats.pop(0)
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            s = randint(0,3)
            self.strength = self.stats[s]
            self.stats.pop(s)
            c = randint(0,2)
            self.constitution = self.stats[c]
            self.stats.pop(c)
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.wisdom = self.stats[0]
            self.hit_die = 8
        elif self.char_class == 'cleric':
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            s = randint(0,1)
            self.strength = self.stats[s]
            self.stats.pop(s)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            d = randint(0,2)
            self.dexterity = self.stats[d]
            self.stats.pop(d)
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.charisma = self.stats[0]
            self.hit_die = 8
        elif self.char_class == 'druid':
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            s = randint(0,3)
            self.strength = self.stats[s]
            self.stats.pop(s)
            d = randint(0,2)
            self.dexterity = self.stats[d]
            self.stats.pop(d)
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.charisma = self.stats[0]
            self.hit_die = 8
        elif self.char_class == 'fighter':
            n = randint(0,1)
            if n == 0:
                self.strength = self.stats[0]
                self.stats.pop(0)
                n2 = randint(0,2)
                if n2 == 0:
                    self.intelligence = self.stats[0]
                    self.stats.pop(0)
                    c = randint(0,3)
                    self.constitution = self.stats[c]
                    self.stats.pop(c)
                    d = randint(0,2)
                    self.dexterity = self.stats[d]
                    self.stats.pop(d)
                    w = randint(0,1)
                    self.wisdom = self.stats[w]
                    self.stats.pop(w)
                    self.charisma = self.stats[0]
                else:
                    self.constitution = self.stats[0]
                    self.stats.pop(0)
                    d = randint(0,3)
                    self.dexterity = self.stats[d]
                    self.stats.pop(d)
                    i = randint(0,2)
                    self.intelligence = self.stats[i]
                    w = randint(0,1)
                    self.wisdom = self.stats[w]
                    self.stats.pop(w)
                    self.charisma = self.stats[0]
            else:
                self.dexterity = self.stats[0]
                self.stats.pop(0)
                n2 = randint(0,2)
                if n2 == 0:
                    self.intelligence = self.stats[0]
                    self.stats.pop(0)
                    s = randint(0,3)
                    self.strength = self.stats[s]
                    self.stats.pop(s)
                    c = randint(0,2)
                    self.constitution = self.stats[c]
                    self.stats.pop(c)
                    w = randint(0,1)
                    self.wisdom = self.stats[w]
                    self.stats.pop(w)
                    self.charisma = self.stats[0]
                else:
                    self.constitution = self.stats[0]
                    self.stats.pop(0)
                    s = randint(0,3)
                    self.strength = self.stats[s]
                    self.stats.pop(s)
                    i = randint(0,2)
                    self.intelligence = self.stats[i]
                    w = randint(0,1)
                    self.wisdom = self.stats[w]
                    self.stats.pop(w)
                    self.charisma = self.stats[0]
            self.hit_die = 10
        elif self.char_class == 'monk':
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            s = randint(0,3)
            self.strength = self.stats[s]
            self.stats.pop(s)
            c = randint(0,2)
            self.constitution = self.stats[c]
            self.stats.pop(c)
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.charisma = self.stats[0]
            self.hit_die = 8
        elif self.char_class == 'paladin':
            self.strength = self.stats[0]
            self.stats.pop(0)
            self.charisma = self.stats[0]
            self.stats.pop(0)
            d = randint(0,3)
            self.dexterity = self.stats[d]
            self.stats.pop(d)
            c = randint(0,2)
            self.constitution = self.stats[c]
            self.stats.pop(c)
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.wisdom = self.stats[0]
            self.hit_die = 10
        elif self.char_class == 'ranger':
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            self.wisdom = self.stats[0]
            self.stats.pop(0)
            s = randint(0,3)
            self.strength = self.stats[s]
            self.stats.pop(s)
            c = randint(0,2)
            self.constitution = self.stats[c]
            self.stats.pop(c)
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.charisma = self.stats[0]
            self.hit_die = 10
        elif self.char_class == 'rogue':
            self.dexterity = self.stats[0]
            self.stats.pop(0)
            n = randint(0,1)
            if n == 0:
                self.intelligence = self.stats[0]
                self.stats.pop(0)
                s = randint(0,3)
                self.strength = self.stats[s]
                self.stats.pop(s)
                c = randint(0,2)
                self.constitution = self.stats[c]
                self.stats.pop(c)
                w = randint(0,1)
                self.wisdom = self.stats[w]
                self.stats.pop(w)
                self.charisma = self.stats[0]
            else:
                self.charisma = self.stats[0]
                self.stats.pop(0)
                s = randint(0,3)
                self.strength = self.stats[s]
                self.stats.pop(s)
                c = randint(0,2)
                self.constitution = self.stats[c]
                self.stats.pop(c)
                w = randint(0,1)
                self.wisdom = self.stats[w]
                self.stats.pop(w)
                self.intelligence = self.stats[0]
            self.hit_die = 8
        elif self.char_class == 'sorcerer':
            self.charisma = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            s = randint(0,3)
            self.strength = self.stats[s]
            self.stats.pop(s)
            d = randint(0,2)
            self.dexterity = self.stats[d]
            self.stats.pop()
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.wisdom = self.stats[0]
            self.hit_die = 6
        elif self.char_class == 'warlock':
            self.charisma = self.stats[0]
            self.stats.pop(0)
            self.constitution = self.stats[0]
            self.stats.pop(0)
            s = randint(0,3)
            self.strength = self.stats[s]
            self.stats.pop(s)
            d = randint(0,2)
            self.dexterity = self.stats[d]
            self.stats.pop()
            i = randint(0,1)
            self.intelligence = self.stats[i]
            self.stats.pop(i)
            self.wisdom = self.stats[0]
            self.hit_die = 6
        elif self.char_class == 'wizard':
            self.intelligence = self.stats[0]
            self.stats.pop(0)
            n = randint(0,1)
            if n == 0:
                self.constitution = self.stats[0]
                self.stats.pop(0)
                n2 = randint(0,7)
                if n2 == 0:
                    self.charisma = self.stats[0]
                    self.stats.pop(0)
                    s = randint(0,2)
                    self.strength = self.stats[s]
                    self.stats.pop(s)
                    d = randint(0,1)
                    self.dexterity = self.stats[d]
                    self.stats.pop(d)
                    self.wisdom = self.stats[0]
                else:
                    s = randint(0,3)
                    self.strength = self.stats[s]
                    self.stats.pop(s)
                    d = randint(0,2)
                    self.dexterity = self.stats[d]
                    self.stats.pop(d)
                    w = randint(0,1)
                    self.wisdom = self.stats[w]
                    self.stats.pop(w)
                    self.charisma = self.stats[0]
            else:
                self.dexterity = self.stats[0]
                self.stats.pop(0)
                n2 = randint(0,7)
                if n2 == 0:
                    self.charisma = self.stats[0]
                    self.stats.pop(0)
                    s = randint(0,2)
                    self.strength = self.stats[s]
                    self.stats.pop(s)
                    c = randint(0,1)
                    self.constitution = self.stats[c]
                    self.stats.pop(c)
                    self.wisdom = self.stats[0]
                else:
                    s = randint(0,3)
                    self.strength = self.stats[s]
                    self.stats.pop(s)
                    c = randint(0,2)
                    self.constitution = self.stats[c]
                    self.stats.pop(c)
                    w = randint(0,1)
                    self.wisdom = self.stats[w]
                    self.stats.pop(w)
                    self.charisma = self.stats[0]
            self.hit_die = 6

        if self.race == 'dragonborn':
            self.strength += 2
            self.charisma += 1
            draconic_ancestry = ['black', 'blue', 'brass', 'bronze', 'copper', 'gold', 'green', 'red', 'silver', 'white']
            self.subrace = choice(draconic_ancestry)
            dragonborn_male = ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadar", "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn"]
            dragonborn_female = ["Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"]
            dragonborn_clan = ["Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Kimbatuul", "Linxakasendalor", "Myastan", "Nemmonis", "Norixius", "Ophinshtalajiir", "Prexijandilin", "Shestendeliath", "Turnuroth", "Verthisathurgiesh", "Yarjerit"]
            if self.sex == 'male':
                self.name = choice(dragonborn_male) + ' ' + choice(dragonborn_clan)
            else:
                self.name = choice(dragonborn_female) + ' ' + choice(dragonborn_clan)
        elif self.race == 'dwarf':
            self.constitution += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'hill dwarf'
                self.wisdom += 1
            else:
                self.subrace = 'mountain dwarf'
                self.strength += 2
            dwarf_male = [ "Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
            dwarf_female = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
            dwarf_clan = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
            if self.sex == 'male':
                self.name = choice(dwarf_male) + ' ' + choice(dwarf_clan)
            else:
                self.name = choice(dwarf_female) + ' ' + choice(dwarf_clan)
        elif self.race == 'elf':
            self.dexterity += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'high elf'
                self.intelligence += 1
            else:
                self.subrace = 'wood elf'
                self.wisdom += 1
            elf_male = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
            elf_female = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirasta", "Thia", "Vadania", "Valanthe", "Xanaphia"]
            elf_family = ["Amakiir (Gemflower)", "Amastacia (Starflower)", "Galanodel (Moonwhisper)", "Holimion (Diamonddew)", "Ilphelkiir (Gemblossom)", "Liadon (Silverfrond)", "Meliamne (Oakenheel)", "Na&iuml;lo (Nightbreeze)", "Siannodel (Moonbrook)", "Xiloscient (Goldpetal)"]
            if self.sex == 'male':
                self.name = choice(elf_male) + ' ' + choice(elf_family)
            else:
                self.name = choice(elf_female) + ' ' + choice(elf_family)
        elif self.race == 'gnome':
            self.intelligence += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'deep gnome'
                self.dexterity += 1
            else:
                self.subrace = 'rock gnome'
                self.constitution += 1
            gnome_male = [ "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook"]
            gnome_female = ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna"]
            gnome_nickname = ["'Aleslosh'", "'Ashhearth'", "'Badger'", "'Cloak'", "'Doublelock'", "'Filchbatter'", "'Fnipper'", "'Ku'", "'Nim'", "'Oneshoe'", "'Pock'", "'Sparklegem'", "'Stumbleduck'"]
            gnome_clan = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers", "Turren"]
            if self.sex == 'male':
                self.name = choice(gnome_male) + ' ' + choice(gnome_nickname) + ' ' + choice(gnome_clan)
            else:
                self.name = choice(gnome_female) + ' ' + choice(gnome_nickname) + ' ' + choice(gnome_clan)
        #elif self.race = 'half elf'
        elif self.race == 'halfling':
            self.dexterity += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'lightfoot halfling'
                self.charisma += 1
            else:
                self.subrace = 'stout halfling'
                self.constitution += 1
            halfling_male = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
            halfling_female = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
            halfling_family = ["Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
            if self.sex == 'male':
                self.name = choice(halfling_male) + ' ' + choice(halfling_family)
            else:
                self.name = choice(halfling_female) + ' ' + choice(halfling_family)
        elif self.race == 'half-orc':
            self.subrace = 'n/a'
            self.strength += 2
            self. constitution += 1
            half_orc_male = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thonk"]
            half_orc_female = ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"]
            if self.sex == 'male':
                self.name = choice(half_orc_male)
            else:
                self.name = choice(half_orc_female)
        elif self.race == 'human':
            human_ethnicities = ['calishite', 'chondathian', 'damaran', 'illuskan', 'mulan', 'rashemi', 'shou', 'tethyrian', 'turami']
            self.subrace = 'n/a'
            self.strength += 1
            self.constitution += 1
            self.dexterity += 1
            self.intelligence += 1
            self.wisdom += 1
            self.charisma += 1
            self.name = 'n/a'
        elif self.race == 'tiefling':
            self.subrace = 'n/a'
            self.charisma += 2
            self.intelligence += 1
            tiefling_male = ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai", "Morthos", "Pelaios", "Skamos", "Therai"]
            tiefling_female = ["Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia", "Orianna", "Phelaia", "Rieta"]
            if self.sex == 'male':
                self.name = choice(tiefling_male)
            else:
                self.name = choice(tiefling_female)

        self.hit_points = self.hit_die + stat_mod(self.constitution)
        if self.subrace == 'hill dwarf':
            self.hit_points += 1

        

new_character = Character()

print('Name:', new_character.name)
print('Race:', new_character.race.capitalize())
print('Subrace:', new_character.subrace.capitalize())
print('Class:', new_character.char_class.capitalize())
print('STR:', new_character.strength)
print('DEX:', new_character.dexterity)
print('CON:', new_character.constitution)
print('INT:', new_character.intelligence)
print('WIS:', new_character.wisdom)
print('CHA:', new_character.charisma)
print('Hit Points:', new_character.hit_points)
