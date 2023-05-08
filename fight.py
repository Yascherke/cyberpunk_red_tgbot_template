import d20
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

#  Перезарядка, я в ролевой данную функцию отключил в угоду казуальности для новых игроков, но свой говнокод оставлю туть
# def reloading(uid):
#     find = Finder(uid)
#
#     magazine = find.magazine()
#     ammo = find.ammo()
#
#     if ammo[13] == 'Стандартные':
#         if ammo[0] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo": ammo[0] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Бронебойные':
#         if ammo[1] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_bb": ammo[1] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Биотоксин':
#         if ammo[2] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_toxin": ammo[2] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'ЭМИ':
#         if ammo[3] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_emp": ammo[3] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Экспансивные':
#         if ammo[4] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_expansive": ammo[4] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Светошумовые':
#         if ammo[5] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_stun": ammo[5] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Зажигательные':
#         if ammo[6] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_fire": ammo[6] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Ядовитые':
#         if ammo[7] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_poison": ammo[7] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Резиновые':
#         if ammo[8] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_rubber": ammo[8] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Усыпляющие':
#         if ammo[9] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_sleep": ammo[9] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Умные':
#         if ammo[10] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_smart": ammo[10] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Дымовые':
#         if ammo[11] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_smoke": ammo[11] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     elif ammo[13] == 'Слезоточивый газ':
#         if ammo[12] != 0:
#             players.update_one({"_id": uid}, {
#                 "$set": {"ammo_eye": ammo[12] - 1}})
#             players.update_one({"_id": uid}, {
#                 "$set": {"magazine": magazine[1]}})
#             return True
#         else:
#             return False
#     else:
#         return False

def getDamage(uid, msg):
    find = Finder(uid)
    getHp = find.hpInfo()
    dmg = int(msg)

    if dmg <= 0:
        return True
    else:
        hp = getHp[1] - dmg

        players.update_one({"_id": uid}, {
                "$set": {"hp": int(hp)}})
        return False

def getHealth(uid, msg):
    getter = msg.replace(' для ', ',').split(',')
    find = Finder(uid)
    getHp = find.hpInfo()
    dmg = int(getter[0]) + int(getHp[1])
    if dmg <= getHp[0]:
        players.update_one({"name": getter[1]}, {
                "$set": {"hp": int(dmg)}})
    else:
        players.update_one({"name": getter[1]}, {
                "$set": {"hp": int(getHp[0])}})
        

# Раньше это было автоматизировано пока народ машин не восстал и в итоге воть(трата пуль после выстрела)
# def hit(uid, msg):
#     find = Finder(uid)
#     magazine = find.magazine()
#
#     if magazine[0] != 0:
#         players.update_one({"_id": uid}, {
#             "$set": {"magazine": magazine[0] - int(msg)}})
#
#         return True
#     else:
#         return False
    

