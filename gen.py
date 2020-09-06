from random import randint, choice

def generate_race():
    races = ['dragonborn', 'dwarf', 'elf', 'gnome', 'halfling', 'half-orc', 'human', 'tiefling']
    race = choice(races)
    return race

def generate_class():
    char_classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
    char_class = choice(char_classes)
    return char_class

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
        elif self.race == 'dwarf':
            self.constitution += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'hill dwarf'
                self.wisdom += 1
            else:
                self.subrace = 'mountain dwarf'
                self.strength += 2
        elif self.race == 'elf':
            self.dexterity += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'high elf'
                self.intelligence += 1
            else:
                self.subrace = 'wood elf'
                self.wisdom += 1
        elif self.race == 'gnome':
            self.intelligence += 2
            sr = randint(0,1)
            if sr == 0:
                self.subrace = 'deep gnome'
                self.dexterity += 1
            else:
                self.subrace = 'rock gnome'
                self.constitution += 1
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
        elif self.race == 'half-orc':
            self.subrace = 'n/a'
            self.strength += 2
            self. constitution += 1
        elif self.race == 'human':
            human_ethnicities = ['calishite', 'chondathian', 'damaran', 'illuskan', 'mulan', 'rashemi', 'shou', 'tethyrian', 'turami']
            self.subrace = 'n/a'
            self.strength += 1
            self.constitution += 1
            self.dexterity += 1
            self.intelligence += 1
            self.wisdom += 1
            self.charisma += 1
        elif self.race == 'tiefling':
            self.subrace = 'n/a'
            self.charisma += 2
            self.intelligence += 1

        self.hit_points = self.hit_die + stat_mod(self.constitution)
        if self.subrace == 'hill dwarf':
            self.hit_points += 1

        

new_character = Character()


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
