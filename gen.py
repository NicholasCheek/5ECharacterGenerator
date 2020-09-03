from random import randint, choice

def generate_race():
    races = ['human', 'elf', 'dwarf', 'halfling']
    race = choice(races)
    return race

def generate_class():
    char_classes = ['barbarian', 'bard']
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
    
def generate_character_stats():
    character_stats = []
    count = 0
    while count < 7:
        roll = generate_stat()
        character_stats.append(roll)
        count += 1
    character_stats.sort(reverse=True)
    character_stats.pop()
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


new_character = Character()


print('Race:', new_character.race.capitalize())
print('Class:', new_character.char_class.capitalize())
print('STR:', new_character.strength)
print('DEX:', new_character.dexterity)
print('CON:', new_character.constitution)
print('INT:', new_character.intelligence)
print('WIS:', new_character.wisdom)
print('CHA:', new_character.charisma)
