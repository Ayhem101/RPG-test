import time
import sys
import random
from time import sleep
from math import floor

class player:
    def __init__(self, name, hp, max_hp, attack, defence, speed,  gold, exp, level, move1, move2, move3, move4, status, attack_modifier, defence_modifier):
        self.name  = name
        self.hp  = max_hp
        self.max_hp  = max_hp
        self.attack  = attack
        self.speed = speed
        self.defence = defence
        self.gold  = gold
        self.exp  = exp
        self.level = level
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.status = status
        self.attack_modifier = attack_modifier
        self.defence_modifier = defence_modifier
        self.ExpNeeded = 100 * (level ** 1.5)
    def player_take_damage(self, damage_source):
        self.hp -= damage_source
    def heal_player(self, heal_amount):
        self.hp += heal_amount
        if  self.hp > self.max_hp:
            self.hp = self.max_hp
    def is_player_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True
    def check_if_level(self):
        if self.exp > self.ExpNeeded:
            self.exp = 0
            self.level += 1
            self.ExpNeeded = 100 * (self.level + 1) ** 1.3
            self.level_up()
    def level_up(self):
        print("YOU LEVELED UP!")
        print(f"{self.name}: {self.level - 1} LV -> {self.name}: {self.level} LV")
        self.attack = self.attack + 3.0  * self.level
        self.defence = self.defence + 1.8 * self.level
        self.speed = self.speed + 1.2 * self.level
        print(f"""
Attack -> {self.attack}
Defence -> {self.defence}
Speed -> {self.speed}
""")
        if type(self.level / 10) == int:
            random_move = random.choice(moves)
            print(f"{self.name} Can now learn {random_move["name"]} !")
            print("What Move Will be Replaced? (move name or Number of the move)")
            while True:
                choice = input("> ")
                li_valid_options = [self.move1["name"] , self.move2["name"] , self.move3["name"] , self.move4["name"] , "1" , "2" , "3" , "4"]
                if choice not in li_valid_options:
                    print("Please Chose something Sane for once")
                    for i in li_valid_options:
                        print(i , end = "/")
                    continue
                else:
                    if choice == "1" or choice == self.move1["name"]:
                        self.move1 = moves[choice]
                    elif choice == "2" or choice == self.move2["name"]:
                        self.move2 = moves[choice]
                    elif choice == "3" or choice == self.move3["name"]:
                        self.move3 = moves[choice]
                    else:
                        self.move4 = moves[choice]








    def gain_experience(self, experience):
        print(f'{self.name} Has Gained {experience} EXP')
        self.exp += experience

class enemy:
    def __init__(self, name, hp, max_hp, base_attack, base_defence, base_speed, base_exp, status, attack_modifier, defence_modifier, level):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = base_attack * (level ** 1.4)
        self.speed = base_speed * (level ** 1.2)
        self.defence = base_defence * (level ** 1.1)      # ← corrected: base_defence, not base_speed
        self.exp = base_exp * (level ** 1.2)
        self.status = status
        self.attack_modifier = attack_modifier
        self.defence_modifier = defence_modifier
        self.level = level
    def enemy_take_damage(self, damage_source):
        self.hp -= damage_source
    def heal_enemy(self, heal_amount):
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    def is_enemy_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

#a BIG list OF moves , like REALLY big

moves = {
    # Basic physical
    "Slash":           {"name": "Slash",           "damage_amount": 15,  "attack_type": "physical"},
    "Pierce":          {"name": "Pierce",          "damage_amount": 18,  "attack_type": "physical"},
    "Strike":          {"name": "Strike",          "damage_amount": 22,  "attack_type": "physical"},
    "Kick":            {"name": "Kick",            "damage_amount": 16,  "attack_type": "physical"},
    "Uppercut":        {"name": "Uppercut",        "damage_amount": 24,  "attack_type": "physical"},
    "Hammer Smash":    {"name": "Hammer Smash",    "damage_amount": 32,  "attack_type": "physical"},
    "Crushing Blow":   {"name": "Crushing Blow",   "damage_amount": 40,  "attack_type": "physical"},
    "Sword Flurry":    {"name": "Sword Flurry",    "damage_amount": 45,  "attack_type": "physical"},

    # Fire
    "Fireball":        {"name": "Fireball",        "damage_amount": 25,  "attack_type": "fire"},
    "Flame Blast":     {"name": "Flame Blast",     "damage_amount": 30,  "attack_type": "fire"},
    "Inferno":         {"name": "Inferno",         "damage_amount": 70,  "attack_type": "fire"},
    "Fire Nova":       {"name": "Fire Nova",       "damage_amount": 65,  "attack_type": "fire"},
    "Volcanic Crush":  {"name": "Volcanic Crush",  "damage_amount": 80,  "attack_type": "fire"},

    # Ice
    "Frost Bolt":      {"name": "Frost Bolt",      "damage_amount": 24,  "attack_type": "ice"},
    "Icy Slash":       {"name": "Icy Slash",       "damage_amount": 27,  "attack_type": "ice"},
    "Blizzard":        {"name": "Blizzard",        "damage_amount": 75,  "attack_type": "ice"},
    "Glacial Crash":   {"name": "Glacial Crash",   "damage_amount": 42,  "attack_type": "ice"},
    "Polar Blast":     {"name": "Polar Blast",     "damage_amount": 60,  "attack_type": "ice"},

    # Lightning
    "Shock Bolt":      {"name": "Shock Bolt",      "damage_amount": 23,  "attack_type": "lightning"},
    "Thunder Strike":  {"name": "Thunder Strike",  "damage_amount": 34,  "attack_type": "lightning"},
    "Lightning Bolt":  {"name": "Lightning Bolt",  "damage_amount": 68,  "attack_type": "lightning"},
    "Volt Tackle":     {"name": "Volt Tackle",     "damage_amount": 52,  "attack_type": "lightning"},
    "Storm Burst":     {"name": "Storm Burst",     "damage_amount": 80,  "attack_type": "lightning"},

    # Dark / poison
    "Poison Fang":     {"name": "Poison Fang",     "damage_amount": 18,  "attack_type": "poison"},
    "Venom Strike":    {"name": "Venom Strike",    "damage_amount": 32,  "attack_type": "poison"},
    "Shadow Claw":     {"name": "Shadow Claw",     "damage_amount": 35,  "attack_type": "dark"},
    "Dark Blast":      {"name": "Dark Blast",      "damage_amount": 44,  "attack_type": "dark"},
    "Dark Nova":       {"name": "Dark Nova",       "damage_amount": 85,  "attack_type": "dark"},

    # Light
    "Holy Bolt":       {"name": "Holy Bolt",       "damage_amount": 26,  "attack_type": "light"},
    "Divine Smite":    {"name": "Divine Smite",    "damage_amount": 58,  "attack_type": "light"},
    "Sunbeam":         {"name": "Sunbeam",         "damage_amount": 50,  "attack_type": "light"},
    "Heavenly Nova":   {"name": "Heavenly Nova",   "damage_amount": 78,  "attack_type": "light"},
}

#Damage Calculating
#----------------------------------------------------------------------------------------
def calc_damage(move_attack, attacker, defender):
    damage = move_attack * (attacker.attack * attacker.attack_modifier / max(defender.defence * defender.defence_modifier, 1))
    damage = round(damage)
    print(f"{attacker.name} dealt {damage} damage")
    return damage
#------------------------------------------------------------------------------------
#Status Effects
#------------------------------------------------------------------------------------
def poison_chance(victim):
    if random.randint(0,100) < 30:
        print(f"---{victim.name} got poisoned!!---")
        victim.status.append("poison")
    else:
        return
def burn_chance(victim):
    if random.randint(0,100) < 30:
        print(f"---{victim.name} got burned!!---")
        victim.status.append("burn")
    else:
        return
def sleep_chance(victim):
    if random.randint(0,100) < 25:
        print(f"---{victim.name} got sleepy!!---")
        victim.status.append("sleep")
    else:
        return
def paralyze_chance(victim):
    if random.randint(0,100) < 20:
        print(f"---{victim.name} got paralyzed!!---")
        victim.status.append("paralyze")
    else:
        return
def freeze_chance(victim):
    if random.randint(0,100) < 10:
        print(f"---{victim.name} got freezed!!---")
        victim.status.append("freeze")
    else:
        return

def weakness_chance(victim):
    if random.randint(0,100) < 37:
        print(f"---{victim.name} got weakness!!---")
        victim.status.append("weakness")
    else:
        return
#------------------------------------------------------------------
#Status Checker
def status_check(object):
    for i in object.status:
        if i == "poison":
            poison_damage(object)
        elif i == "burn":
            burn_damage(object)
        elif i == "sleep":
            sleep_damage(object)
        elif i == "paralyze":
            paralyze_damage(object)
        elif i == "freeze":
            freeze_damage(object)
        elif i == "weakness":
            weakness_damage(object)
        else:
            return
#--------------------------------------------------------------------------
#Status_effects

def poison_damage(victim):
    print(f"{victim.name} is suffering from poison..")
    poison_dam = 5 + (victim.attack * 0.5)
    victim.hp = victim.hp - poison_dam
    return

def burn_damage(victim):
    print(f"{victim.name} is burning alive and it's affecting His attack Power!")
    victim.attack_modifier = 0.7
    return
def sleep_damage(victim):
    print(f"{victim.name} is Dozy , He Is Defenseless!")
    victim.defence_modifier = 0
    return
def paralyze_damage(victim):
    print(f"{victim.name} is paralyzed , his Speed is cooked")
    victim.speed = victim.speed * 0.4
    return
def freeze_damage(victim):
    print(f"{victim.name} is freezing solid , He cant Attack!!!")
    victim.attack_modifier = 0
    return
def weakness_damage(victim):
    print(f"{victim.name} is weak , both of his Defense and Attack stats are Halved!!")
    victim.defence_modifier = 0.5
    victim.attack_modifier = 0.5
    return
def status_remover(victim):
        for i in victim.status:
            if random.randint(0,100) < 25:
                victim.status.remove(i)
                print(f"{victim.name} has been healed from {i}")













warrior = player("Ayhem" , 100 , 100 , 50 , 17 , 20 , 0 , 0 , 0 , moves["Slash"] , moves["Pierce"] , moves["Strike"] , moves["Kick"] , [] , 1.0 , 1.0 )
zombie = enemy("Zombie" , 100 , 100 , 10 , 17 , 23 , 30 , [] , 1.0 , 1.0 , 1)

def player_turn(player, enemy):
    if player.is_player_alive():
        sleep(0.5)
        valid_options = ["1" , "2" , "attack" , "heal"]
        print(f"{player.name}: {hp_bar(player.hp, player.max_hp)} | {player.status}")
        print(f"{enemy.name}: {hp_bar(enemy.hp, enemy.max_hp)} | {enemy.status}")
        print("--------------------")
        print("""1-Attack | 2-Heal""")
        print("--------------------")
        while True:
            sleep(0.5)
            choice = input("-> ").lower()
            if choice not in valid_options:
                print("Not time for Nonsense")
                for i in valid_options:
                    print(i , end="/")
                continue
            else:
                if choice == "1" or choice == "attack":
                    move_list = [player.move1["name"], player.move2["name"], player.move3["name"], player.move4["name"]]
                    for i in move_list:
                        print("--",i)
                    while True:
                        print("What's the Move?")
                        move_choice = input("-> ")
                        if move_choice != player.move1["name"] and move_choice != player.move2["name"] and move_choice != player.move3["name"] and move_choice != player.move4["name"] and move_choice not in ["1", "2", "3", "4"]:
                            print("Not a Valid Move , enter the number or the Name")
                            continue
                        else:
                            if move_choice == "1" or move_choice == player.move1["name"]:
                                if player.move1["attack_type"] == "poison":
                                    poison_chance(enemy)      # typo fixed: should be enemy, not player
                                elif player.move1["attack_type"] == "fire":
                                    burn_chance(enemy)
                                elif player.move1["attack_type"] == "ice":
                                    freeze_chance(enemy)

                                print(f"{player.name} used {move_choice}!")
                                enemy.enemy_take_damage(calc_damage(player.move1["damage_amount"], player, enemy))
                                return
                            elif move_choice == "2" or move_choice == player.move2["name"]:
                                if player.move2["attack_type"] == "poison":
                                    poison_chance(enemy)
                                elif player.move2["attack_type"] == "fire":
                                    burn_chance(enemy)
                                elif player.move2["attack_type"] == "ice":
                                    freeze_chance(enemy)

                                print(f"{player.name} used {move_choice}!")
                                enemy.enemy_take_damage(calc_damage(player.move2["damage_amount"], player, enemy))
                                return
                            elif move_choice == "3" or move_choice == player.move3["name"]:
                                if player.move3["attack_type"] == "poison":
                                    poison_chance(enemy)
                                elif player.move3["attack_type"] == "fire":
                                    burn_chance(enemy)
                                elif player.move3["attack_type"] == "ice":
                                    freeze_chance(enemy)

                                print(f"{player.name} used {move_choice}!")
                                enemy.enemy_take_damage(calc_damage(player.move3["damage_amount"], player, enemy))
                                return
                            else:
                                if player.move4["attack_type"] == "poison":
                                    poison_chance(enemy)
                                elif player.move4["attack_type"] == "fire":
                                    burn_chance(enemy)
                                elif player.move4["attack_type"] == "ice":
                                    freeze_chance(enemy)
                                print(f"{player.name} used {move_choice}!")
                                enemy.enemy_take_damage(calc_damage(player.move4["damage_amount"], player, enemy))
                                return
                else:
                    print("Healed Successfully")
                    player.heal_player(100)
                    break
    else:
        pass

def hp_bar(current_hp, max_hp):
    ratio = current_hp / max_hp
    filled_char = floor(20 * ratio)
    bar = f"[{filled_char * '█'}{(20-filled_char) * '*'}]"  # ← fixed quotes
    return bar

def enemy_turn(player, enemy):
    x = random.randint(1,10)
    if x == 10:
        sleep(0.5)
        print(f"{enemy.name} Healed by 100")
        enemy.heal_enemy(100)
    else:
        sleep(0.5)
        # ensure printed damage is integer
        actual_damage = round(enemy.attack)
        player.player_take_damage(actual_damage)
        print(f"{enemy.name} dealt {actual_damage} damage!")

def combat(player, enemy):
    print(f"Be Aware a {enemy.name} is Approaching!!!")
    sleep(0.5)
    print("--What Will you do?")
    while True:
        status_check(player)
        status_check(enemy)
        status_remover(player)
        status_remover(enemy)
        print(f"{player.name}: {hp_bar(player.hp, player.max_hp)}")
        print(f"{enemy.name}: {hp_bar(enemy.hp, enemy.max_hp)}")
        if player.is_player_alive() and enemy.is_enemy_alive():
            if player.speed > enemy.speed:
                sleep(0.5)
                player_turn(player, enemy)
                enemy_turn(player, enemy)
            else:
                sleep(0.5)
                enemy_turn(player, enemy)
                player_turn(player, enemy)
        else:
            if player.is_player_alive():
                sleep(0.2)
                print(f"{player.name} Have Won!")
                player.gain_experience(enemy.exp)
            else:
                print("You lost..")
            break

combat(warrior, zombie)