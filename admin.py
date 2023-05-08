from pymongo import MongoClient
from mongodb import Finder
import d20
import collections


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

class Admin:

    def __init__(self, uid):
        self.uid = uid

    def giveExp(self, msg):
        find = Finder(self.uid)
        getter = msg.replace(' для ', ',').split(',')
        role_id = find.getIdByName(getter[1])
        finder = Finder(role_id)
        status = finder.skills()
        print(getter[0])
        reward = int(getter[0])
        print(reward)

        if status[4] == "Рокербой":
            rocker = finder.rockerboy()
            rockerboys.update_one({"_id": role_id}, {
                    "$set": {"exp": rocker[3] + reward}})
            return reward
        elif status[4] == "Соло":
            sl = finder.solo()
            solos.update_one({"_id": role_id}, {
                    "$set": {"exp": sl[3] + reward}})
            return reward
        elif status[4] == "Нетраннер":
            netr = finder.getNRunner()
            netrunners.update_one({"_id": role_id}, {
                    "$set": {"exp": netr[3] + reward}})
            return reward
        elif status[4] == "Техник":
            tech = finder.tech()
            techs.update_one({"_id": role_id}, {
                    "$set": {"exp": tech[3] + reward}})
            return reward
        elif status[4] == "Медтехник":
            reaper = finder.reaper()
            reapers.update_one({"_id": role_id}, {
                    "$set": {"exp": reaper[3] + reward}})
            return reward
        elif status[4] == "Медиа":
            media = finder.media()
            medias.update_one({"_id": role_id}, {
                    "$set": {"exp": media[3] + reward}})
            return reward
        elif status[4] == "Законник":
            pol = finder.police()
            police.update_one({"_id": role_id}, {
                    "$set": {"exp": pol[3] + reward}})
            return reward
        elif status[4] == "Экзек":
            ekzek = finder.ekzek()
            ekzeks.update_one({"_id": role_id}, {
                    "$set": {"exp": ekzek[3] + reward}})
            return reward
        elif status[4] == "Фиксер":
            fix = finder.fixer()
            fixer.update_one({"_id": role_id}, {
                    "$set": {"exp": fix[3] + reward}})
            return reward
        elif status[4] == "Кочевник":
            nom = finder.nomad()
            nomads.update_one({"_id": role_id}, {
                    "$set": {"exp": nom[3] + reward}})
            return reward

    def humman(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        getInf = finder.skills()
        hum = int(getInf[3]) - int(getter[0]) 
        players.update_one({"name": getter[1]}, {
            "$set": {"humanity": int(hum)}})
    
    def emp(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
        getInf = finder.stats()
        hum = int(getInf[9]) - int(getter[0]) 
        players.update_one({"name": getter[1]}, {
            "$set": {"empathy": int(hum)}})
    
    def stat(self, msg):
        getter = msg.replace(' для ', ',').split(',')
        find = Finder(self.uid)
        rid = find.getIdByName(getter[1])
        finder = Finder(rid)
      
