from pymongo import MongoClient
from mongodb import Finder
import d20

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
lvls = db["lvls"]

class Implants:

    def __init__(self, uid):
        self.uid = uid

    def setupPorts(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        imp = getter[0]

        if imp == "Кибераудио":
            implants.update_one({"name": getter[1]}, {
                "$set": {"audio": getter[0]}})
        elif imp == "Нейролинк":
            implants.update_one({"name": getter[1]}, {
                "$set": {"neural": getter[0]}})
        elif imp == "Правый киберглаз":
            implants.update_one({"name": getter[1]}, {
                "$set": {"right_eye": getter[0]}})
        elif imp == "Левый киберглаз":
            implants.update_one({"name": getter[1]}, {
                "$set": {"left_eye": getter[0]}})
        elif imp == "Правая киберрука":
            implants.update_one({"name": getter[1]}, {
                "$set": {"right_arm": getter[0]}})
        elif imp == "Левая киберрука":
            implants.update_one({"name": getter[1]}, {
                "$set": {"left_arm": getter[0]}})
        elif imp == "Правая кибернога":
            implants.update_one({"name": getter[1]}, {
                "$set": {"right_leg": getter[0]}})
        elif imp == "Левая кибернога":
            implants.update_one({"name": getter[1]}, {
                "$set": {"left_leg": getter[0]}})

    def audio(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.audio()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"audio_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 3:
                    count += 1
                else:
                    return False
    
    def reye(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.right_eye()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"right_eye_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 3:
                    count += 1
                else:
                    return False
    
    def leye(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.left_eye()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"left_eye_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 3:
                    count += 1
                else:
                    return False
    
    def rarm(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.right_arm()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"right_arm_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 4:
                    count += 1
                else:
                    return False

    def larm(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.left_arm()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"left_arm_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 4:
                    count += 1
                else:
                    return False

    def rleg(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.right_leg()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"right_leg_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 3:
                    count += 1
                else:
                    return False
    
    def lleg(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.left_leg()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"left_leg_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 3:
                    count += 1
                else:
                    return False

    def neur(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.neural()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"neural_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 5:
                    count += 1
                else:
                    return False

    def inside(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.inside()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"inside_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 7:
                    count += 1
                else:
                    return False
    
    def style(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.style()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"style_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 7:
                    count += 1
                else:
                    return False

    def outs(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.outside()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"outside_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 7:
                    count += 1
                else:
                    return False

    def borg(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        audio = finder.borg()
        count = 0
        for item in audio:
            if item == 0:
                implants.update_one({"name": getter[1]}, {
                    "$set": {"borg_slot"+str(count+1): getter[0]}})
                return True
            else:
                if count < 7:
                    count += 1
                else:
                    return False