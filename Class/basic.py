# Learning About Class

import random


class User:
    """This is User"""

    weapons = (
        {
            'Name': 'Pussy',
            'Damage': 20,
        },
        {
            'Name': 'Dick',
            'Damage': 40,
        },
        {
            'Name': 'Dick',
            'Damage': 40,
        },
        {
            'Name': 'Sword',
            'Damage': 80,
        },
        {
            'Name': 'Spear',
            'Damage': 84,
        },
        {
            'Name': 'Blade',
            'Damage': 84,
        },
    )
    
    # random.seed(1219941731998)

    def __init__(self, first_name='Tú Chi', last_name='Vương', race='Human', role='Slave', attitude='Absolute Loyalty',
                 sex='Female', level=0, pure_damage=10):
        attack_speed = random.randint(1, 4)
        weapon_selected = self.weapons[random.randint(0, len(self.weapons)) - 1]
        self.first_name = first_name
        self.last_name = last_name
        self.race = race
        self.role = role
        self.attitude = attitude
        self.sex = sex
        self.level = level
        self.hp = 10000
        self.status = 'Alive' if self.hp > 0 else 'Dead'
        self.base_damage = pure_damage
        self.weapon = weapon_selected['Name'] if self.first_name != 'Tú Chi' and self.last_name != 'Vương' and self.race != 'Slave' else self.weapons[0]['Name']
        self.damage = weapon_selected['Damage'] if self.first_name != 'Tú Chi' and self.last_name != 'Vương' and self.race != 'Slave' else self.weapons[0]['Damage']
        self.attack_speed = attack_speed

    def __str__(self):
        return f"Name: {self.last_name} {self.first_name} - Race: {self.race}"

    def information(self):
        print(" =========================Information========================= ")
        for attribute, data in self.__dict__.items():
            print(f"||{attribute.replace('_', ' ').strip().title():^28} - {data:^28}||")
        print(" ============================================================= ")
        return ''

    def attack(self, enemy):
        # print(self.damage*self.attack_speed)
        if enemy.hp > 0:
            enemy.hp = enemy.hp - (self.damage*self.attack_speed)
            print(self.damage*self.attack_speed)
            return enemy.hp


master = User(first_name='Đức Hoàng', last_name='Nguyễn', role='Master', race='Half Human', attitude='Chaos', sex='Male')
slave = User()

print(master.information())
print(master.attack(slave))
print(slave.information())

while master.hp > 0:
    if master.hp <= 0 or slave.hp <= 0:
        break
    else:
        master.attack(slave)
        # slave.attack(master)
        print(f"Master Hp: {master.hp} - Slave Hp: {slave.hp} - Damage: {master.damage}")