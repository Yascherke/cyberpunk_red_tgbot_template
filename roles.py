from pymongo import MongoClient
from mongodb import Finder
from programs import Interface

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
lvls = db["lvls"]

class Role:

    def __init__(self, uid):
        self.uid = uid

    def rocker(self):
        finder = Finder(self.uid)
        gen_info = finder.rockerboy()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            rockerboys.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            rockerboys.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
    
    def solo(self):
        finder = Finder(self.uid)
        gen_info = finder.solo()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            solos.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            solos.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
    
    def media(self):
        finder = Finder(self.uid)
        gen_info = finder.media()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            medias.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            medias.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
    
    def police(self):
        finder = Finder(self.uid)
        gen_info = finder.police()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            police.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            police.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
    
    def fixer(self):
        finder = Finder(self.uid)
        gen_info = finder.fixer()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            fixer.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            fixer.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
    
    def nomad(self):
        finder = Finder(self.uid)
        gen_info = finder.nomad()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            nomads.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            nomads.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
    
    def ekzek(self):
        finder = Finder(self.uid)
        gen_info = finder.ekzek()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            ekzeks.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            ekzeks.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            return True
        
    def reaper(self):
        finder = Finder(self.uid)
        gen_info = finder.reaper()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            reapers.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            reapers.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": gen_info[4] + 2}})
            return True
    
    def tech(self):
        finder = Finder(self.uid)
        gen_info = finder.tech()
        
        ulvl = gen_info[2] + 1
        for lvl in lvls.find({"_id": ulvl}):
            print("Lvl finder done")

        check = gen_info[3] - lvl['cost']

        if gen_info[3] < lvl['cost'] or check < 0:
            return False
        else:
            techs.update_one({"_id": self.uid}, {
                             "$set": {"exp": gen_info[3] - lvl['cost']}})
            techs.update_one({"_id": self.uid}, {
                             "$set": {"lvl": gen_info[2] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": gen_info[4] + 2}})
            return True

    def lvlUp(self):
        finder = Finder(self.uid)
        gen = finder.generalInfo()
        nr = Interface(self.uid)

        if gen[1] == 'Рокербой':
            self.rocker()
        if gen[1] == 'Соло':
            self.solo()
        if gen[1] == 'Фиксер':
            self.fixer()
        if gen[1] == 'Медиа':
            self.media()
        if gen[1] == 'Экзек':
            self.ekzek()
        if gen[1] == 'Медтехник':
            self.reaper()
        if gen[1] == 'Техник':
            self.tech()
        if gen[1] == 'Кочевник':
            self.nomad()
        if gen[1] == 'Законник':
            self.police()
        if gen[1] == 'Нетраннер':
            nr.lvlUp()
    
    
    def techPoint(self, msg):
        find = Finder(self.uid)
        role = find.tech()

        if role[4] != 0 and msg == "Модернизация":
            techs.update_one({"_id": self.uid}, {"$set": {"modern": role[5] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Изготовитель":
            techs.update_one({"_id": self.uid}, {"$set": {"crafter": role[6] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Изобретатель":
            techs.update_one({"_id": self.uid}, {"$set": {"creator": role[7] + 1}})
            techs.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        else:
            False

    def medPoint(self, msg):

        find = Finder(self.uid)
        role = find.reaper()

        if role[4] != 0 and msg == "Хирургия":
            reapers.update_one({"_id": self.uid}, {"$set": {"surgeon": role[5] + 2}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Фармацевтика":
            reapers.update_one({"_id": self.uid}, {"$set": {"pharmacist": role[6] + 1}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        elif role[4] != 0 and msg == "Изобретатель":
            reapers.update_one({"_id": self.uid}, {"$set": {"Криосистемы": role[7] + 1}})
            reapers.update_one({"_id": self.uid}, {"$set": {"points": role[4] - 1}})
            return True
        else:
            False