from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient("coonection with mongodb",
                      connect=False)

db = cluster["WoE"]
players = db["players"]
roles = db["class"]
ranks = db["rank"]
armor = db["armor"]
skills = db["skills"]
rockerboys = db["rockerboys"]
solos = db["solos"]
netrunners = db["netrunners"]
techs = db["techs"]
reapers = db["reapers"]
medias = db["medias"]
ekzeks = db["ekzeks"]
police = db["police"]
fixer = db["fixer"]
nomads = db["nomads"]
programs = db["programs"]

implants = db["implants"]
inventory = db["inventory"]


def getRole(getter):
    for role in roles.find({"Name": getter[0]}):
        rid = role['_id']
        return rid


def getSkill(getter):
    for skill in skills.find({"name": getter}):
        print("Done")
    return [skill['name'],  skill['base'], skill['desc']]


def catchSkill(uid):
    skill_base = []
    for player in players.find({"_id": uid}):
        traits = player["traits"]
        for n in traits:
            print(n)
            x = list(n.values())
            skill_base.append(x)
    return skill_base


def send_money(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player2 = find.money()
    player1 = find.moneyByName(getter[1])
    before = int(player1)
    before1 = int(player2)
    money = int(getter[0])
    players.update_one({"_id": uid}, {"$set": {"money": before1 - money}})
    players.update_one({"name": getter[1]}, {
                       "$set": {"money": before + money}})


def send_exp(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player = find.generalByName(getter[1])
    exp = int(getter[0])
    players.update_one({"name": getter[1]}, {
                       "$set": {"rank_exp": player[3] + exp}})


def bank_gm(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    player = find.moneyByName(getter[1])
    money = int(getter[0])
    players.update_one({"name": getter[1]},
                       {"$set": {
                           "money": player + money
                       }})

def bank_pl(uid, msg):
    find = Finder(uid)
    player = find.money()
    money = int(msg)
    players.update_one({"_id": uid},
                       {"$set": {
                           "money": player - money
                       }})


def output(uid, msg):

    find = Finder(uid)
    player_armor = find.equipment()
    player_wp = find.equipment()
    player_bpack = find.backpack()
    msg = msg

    if msg == "Броню" or msg == "броню":
        if player_armor[2] != 0:
            players.update_one({"_id": uid}, {
                "$set": {"armor": 0}})
            players.update_one({"_id": uid}, {
                "$set": {"sp": 0}})
            players.update_one({"_id": uid}, {
                "$set": {"main_sp": 0}})
        else:
            return False

    if msg == "Оружие" or msg == "оружие":
        if player_wp[0] != 0:
            count = 0
            for item in player_bpack:
                if item == 0:
                    players.update_one({"_id": uid}, {"$set": {"slot"+str(count+1): player_wp[0]}})
                else:
                    if count < 15:
                        count += 1
                    else:
                        return False
            players.update_one({"_id": uid}, {
                "$set": {"weapon": 0}})
            return True
        else:
            return False


def giveItem(uid, msg):
    find = Finder(uid)
    getter = msg.replace(' для ', ',').split(',')
    slot = int(getter[0])

    player_bp = find.backpackByName(getter[1])
    owner = find.backpack()

    for_key = slot-1
    owner_item = owner[for_key]

    count = 0
    for item in player_bp:
        if item == 0 and owner_item != 0:
            print(owner_item)
            players.update_one({"name": getter[1]}, {
                "$set": {"slot"+str(count+1): owner_item}})
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(slot): 0}})
            return True
        elif owner_item == 0:
            return False
        else:
            if count < 15:
                count += 1
            else:
                return False


def equip_wp(uid, msg):
    find = Finder(uid)
    slot = int(msg)
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    player_wp = find.equipment()

    if owner_item != 0 and player_wp[0] == 0:

        players.update_one({"_id": uid}, {
            "$set": {"weapon": owner[slot-1]}})
        players.update_one({"_id": uid}, {
            "$set": {"slot"+str(slot): 0}})
        print(owner[slot-1])
        return True
    else:
        print(owner[slot-1])
        return False


def equip_armor(uid, msg):

    find = Finder(uid)
    slot = int(msg)
    owner = find.backpack()
    for_key = slot-1
    owner_item = owner[for_key]
    player_armor = find.equipment()

    getArmor = find.armor(owner_item)

    if owner_item != 0 and player_armor[1] == 0:
        if player_armor[1] != 0:
            return 1
        else:
            players.update_one({"_id": uid}, {
                "$set": {"armor": getArmor[0]}})
            players.update_one({"_id": uid}, {
                "$set": {"sp": getArmor[1]}})
            players.update_one({"_id": uid}, {
                "$set": {"main_sp": getArmor[1]}})
            players.update_one({"_id": uid}, {
                "$set": {"slot"+str(slot): 0}})
            return True
    else:
        return False


def buyWp(uid, msg):
    find = Finder(uid)
    getter = msg.replace(' для ', ',').split(',')
    player_bp = find.backpackByName(getter[1])

    count = 0
    for item in player_bp:
        if item == 0:
            players.update_one({"name": getter[1]}, {
                "$set": {"slot"+str(count+1): getter[0]}})
            return True
        else:
            if count < 15:
                count += 1
            else:
                return False


def buyArmor(uid, msg):
    find = Finder(uid)
    getter = msg.replace(' для ', ',').split(',')
    player_bp = find.backpackByName(getter[1])
  
    getArmor = find.armor(getter[0])
    print(getArmor[0], getter[0], getter[1])
    count = 0
    for item in player_bp:
        if item == 0:
            players.update_one({"name": getter[1]}, {
                "$set": {"slot"+str(count+1): getArmor[0]}})
                
            return True
        else:
            if count < 15:
                count += 1
            else:
                return False
