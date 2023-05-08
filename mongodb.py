from pymongo import MongoClient

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


class Finder:

    def __init__(self, uid):
        self.uid = uid

    def stats(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['intelligence'], player['reaction'], player['dexterity'], player['technics'], player['cool'], player['will'], player['luck'], player['speed'], player['bodytype'], player['empathy']]

    def mainStats(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['main_int'], player['main_rea'], player['main_dex'], player['main_tec'], player['main_coo'], player['main_wil'], player['main_luc'], player['main_spe'], player['main_bod'], player['main_emp']]

    def generalInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['name'], player['role_name'], player['rank'], player['rank_exp'], player['car'], player['home'], player['car_info']]

    def hpInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['max_hp'], player['hp'], player['severe_injury'], player['die_dice'], player['crit_dmg']]

    def equipment(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['weapon'], player['armor'], player['sp'], player['main_sp']]

    def backpack(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [
            player['slot1'],
            player['slot2'],
            player['slot3'],
            player['slot4'],
            player['slot5'],
            player['slot6'],
            player['slot7'],
            player['slot8'],
            player['slot9'],
            player['slot10'],
            player['slot11'],
            player['slot12'],
            player['slot13'],
            player['slot14'],
            player['slot15'],
        ]

    def backpackByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [
            player['slot1'],
            player['slot2'],
            player['slot3'],
            player['slot4'],
            player['slot5'],
            player['slot6'],
            player['slot7'],
            player['slot8'],
            player['slot9'],
            player['slot10'],
            player['slot11'],
            player['slot12'],
            player['slot13'],
            player['slot14'],
            player['slot15'],
        ]

    def money(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return player['money']

    def otherInfo(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['gang'], player['corp'], player['organ']]

    def status(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['admin'], player['gm'], player['status'], player['trauma']]

    def skills(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [player['traits'], player['implants'], player['programs'], player['humanity'],  player['role_name']]

    def roles(self, id):
        for role in roles.find({"_id": id}):
            return role["Name"]

    def corps(self, id):
        for corp in corps.find({"_id": id}):
            return corp["name"]

    def ranks(self, id):
        for rank in ranks.find({"_id": id}):
            print('Done')
        return [rank['name'], rank['rank_exp'], rank["_id"]]

    def cars(self, id):
        for car in cars.find({"_id": id}):
            print('Done')
        return [car['name'], car['cost']]

    def houses(self, id):
        for house in houses.find({"_id": id}):
            print('Done')
        return [house['name'], house['cost']]

    def moneyByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return player['money']

    def generalByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [
            player['name'],
            player['hero_class'],
            player['rank'],
            player['rank_exp'],
            player['car'],
            player['home'],
            player['_id']
        ]

    def backpackByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return [
            player['slot1'],
            player['slot2'],
            player['slot3'],
            player['slot4'],
            player['slot5'],
            player['slot6'],
            player['slot7'],
            player['slot8'],
            player['slot9'],
            player['slot10'],
            player['slot11'],
            player['slot12'],
            player['slot13'],
            player['slot14'],
            player['slot15'],
        ]

    def armor(self, name):
        for arm in armor.find({"name": name}):
            print('Done')
        return [arm['name'], arm['sp']]

    def getIdByName(self, name):
        for player in players.find({"name": name}):
            print('Done')
        return player['_id']

    def getNRunner(self):
        for nr in netrunners.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
            nr['action'],
            nr['deka'],
        ]

    def nrPrograms(self):
        for nr in netrunners.find({"_id": self.uid}):
            print('Done')
        return [
            nr['program1'],
            nr['program2'],
            nr['program3'],
            nr['program4'],
            nr['program5'],
            nr['program6'],
            nr['program7'],
            nr['program8'],
            nr['program9'],
            nr['program10'],
            nr['program11'],
            nr['program12'],
            nr['program13'],
            nr['program14'],
            nr['program15']
        ]

    def nrEquip(self):
        for nr in netrunners.find({"_id": self.uid}):
            print('Done')
        return [
            nr['equip1'],
            nr['equip2'],
            nr['equip3'],
            nr['equip4'],
            nr['equip5'],
            nr['equip6'],
            nr['equip7'],
            nr['equip8'],
            nr['equip9'],
            nr['equip10'],
        ]

    def getProgram(self, msg):
        for nr in programs.find({"name": msg}):
            print('Done')
        return [
            nr['name'],
            nr['class'],
            nr['atk'],
            nr['def'],
            nr['rez'],
            nr['effect'],
            nr['price'],
        ]

    def rockerboy(self):
        for nr in rockerboys.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
        ]

    def solo(self):
        for nr in solos.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
        ]

    def media(self):
        for nr in medias.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
        ]

    def police(self):
        for nr in police.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
        ]

    def fixer(self):
        for nr in fixer.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
        ]

    def nomad(self):
        for nr in nomads.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],

        ]

    def ekzek(self):
        for nr in ekzeks.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
            nr["slave1"],
            nr["slave2"],
            nr["slave3"],
        ]

    def reaper(self):
        for nr in reapers.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
            nr["points"],
            nr["surgeon"],
            nr["pharmacist"],
            nr["сryo"],
        ]

    def tech(self):
        for nr in techs.find({"_id": self.uid}):
            print('Done')
        return [
            nr['player'],
            nr['name'],
            nr['lvl'],
            nr['exp'],
            nr["points"],
            nr["modern"],
            nr["crafter"],
            nr["creator"],
        ]

    def storage(self):
        for player in players.find({"_id": self.uid}):
            print('Done')
        return [
            player['storage1'],
            player['storage2'],
            player['storage3'],
            player['storage4'],
            player['storage5'],
            player['storage6'],
            player['storage7'],
            player['storage8'],
            player['storage9'],
            player['storage10'],
        ]

    def audio(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['audio_slot1'],
            iml['audio_slot2'],
            iml['audio_slot3'],
        ]

    def right_eye(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['right_eye_slot1'],
            iml['right_eye_slot2'],
            iml['right_eye_slot3'],
        ]

    def left_eye(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['left_eye_slot1'],
            iml['left_eye_slot2'],
            iml['left_eye_slot3'],
        ]

    def neural(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['neural_slot1'],
            iml['neural_slot2'],
            iml['neural_slot3'],
            iml['neural_slot4'],
            iml['neural_slot5'],
        ]

    def right_arm(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['right_arm_slot1'],
            iml['right_arm_slot2'],
            iml['right_arm_slot3'],
            iml['right_arm_slot4'],
        ]

    def left_arm(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['left_arm_slot1'],
            iml['left_arm_slot2'],
            iml['left_arm_slot3'],
            iml['left_arm_slot4'],
        ]

    def right_leg(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['right_leg_slot1'],
            iml['right_leg_slot2'],
            iml['right_leg_slot3'],
        ]

    def left_leg(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['left_leg_slot1'],
            iml['left_leg_slot2'],
            iml['left_leg_slot3'],
        ]

    def inside(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['inside_slot1'],
            iml['inside_slot2'],
            iml['inside_slot3'],
            iml['inside_slot4'],
            iml['inside_slot5'],
            iml['inside_slot6'],
            iml['inside_slot7'],
        ]

    def outside(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['outside_slot1'],
            iml['outside_slot2'],
            iml['outside_slot3'],
            iml['outside_slot4'],
            iml['outside_slot5'],
            iml['outside_slot6'],
            iml['outside_slot7'],
        ]

    def style(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['style_slot1'],
            iml['style_slot2'],
            iml['style_slot3'],
            iml['style_slot4'],
            iml['style_slot5'],
            iml['style_slot6'],
            iml['style_slot7'],
        ]

    def borg(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['borg_slot1'],
            iml['borg_slot2'],
            iml['borg_slot3'],
            iml['borg_slot4'],
            iml['borg_slot5'],
            iml['borg_slot6'],
            iml['borg_slot7'],
        ]

    def ports(self):
        for iml in implants.find({"_id": self.uid}):
            print('Done')
        return [
            iml['audio'],
            iml['right_eye'],
            iml['left_eye'],
            iml['right_arm'],
            iml['left_arm'],
            iml['right_leg'],
            iml['left_leg'],
            iml['neural'],
        ]

    def weapMods(self):
        for wp in players.find({"_id": self.uid}):
            print('Done')
        return [
            wp["mag_mod"],
            wp["scope"],
            wp["barrel"],
            wp["connector"],
        ]
