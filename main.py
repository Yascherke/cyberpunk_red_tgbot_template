import asyncio
import logging
from math import ceil
from statistics import mean
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pymongo import MongoClient
from aiogram.utils import executor
import re
import d20

from hero import Hero as hero
from mongodb import Finder
from view import View
from programs import Interface
from admin import Admin
from roles import Role
from implants import Implants

import markups as nav
from system import getRole, getSkill, send_money, send_exp, bank_gm, output, giveItem, equip_wp, equip_armor, buyWp, buyArmor, bank_pl
from fight import getDamage, getHealth

from ws import keep_alive

# Единственное для чего я использую фласк, так это эта функция, она держит мой пиратский корабль на плаву,
# поскольку деняк на платный хостинг нет и я обхожу ограничения как только могу
keep_alive()

logging.basicConfig(level=logging.INFO)

API_TOKEN = "tg bot token"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Туть у нас подключение к монго дб и основные таблицы используемые в боте.
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


def findUserParamByID(uid):
  for player in players.find({"_id": uid}):
    pid = player['_id']
    return pid


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
  uid = message.from_user.id
  p_id = findUserParamByID(uid)
  if p_id is None:
    await hero.name.set()
    await message.answer(
      "Как зовут вашего персонажа(ПУНКТ 2 АНКЕТЫ, ЕСЛИ ВЫ НЕ ЭКЗЕК)")

    @dp.message_handler(state=hero.name)
    async def cmd_name(message: types.Message, state: FSMContext):
      await hero.name.set()

      async with state.proxy() as data:
        data['Name'] = message.text
        uid = message.from_user.id
        name = data['Name']
        money = hero.moneyRoll()
        view = View(uid)

        players.insert_one({
          "_id": uid,
          "name": name,
          "intelligence": 0,
          "reaction": 0,
          "dexterity": 0,
          "technics": 0,
          "cool": 0,
          "will": 0,
          "luck": 0,
          "speed": 0,
          "bodytype": 0,
          "empathy": 0,
          "hero_class": hero.hero_class,
          "car": hero.car,
          "car_info": hero.car_info,
          "home": hero.home,
          "trauma": hero.trauma,
          "max_hp": 0,
          "hp": 0,
          "severe_injury": 0,
          "die_dice": 0,
          "crit_dmg": hero.crit_dmg,
          "rank": hero.rank,
          "rank_exp": hero.rank_exp,
          "weapon": hero.weapon,
          "mag_mod": 0,
          "scope": 0,
          "barrel": 0,
          "connector": 0,
          "armor": hero.armor,
          "main_sp": hero.main_sp,
          "sp": hero.sp,
          "money": money,
          "gang": hero.gang,
          "corp": hero.corp,
          "organ": hero.organ,
          "traits": hero.traits,
          "implants": uid,
          "programs": hero.programs,
          "notes": hero.notes,
          "admin": hero.admin,
          "gm": hero.gm,
          "humanity": 0,
          "status": hero.status,
          "trauma": hero.trauma,
          "role_name": hero.role_name,
          "ammo_bb": hero.ammo_bb,
          "ammo_toxin": hero.ammo_toxin,
          "ammo_emp": hero.ammo_emp,
          "ammo_expansive": hero.ammo_expansive,
          "ammo_stun": hero.ammo_stun,
          "ammo_fire": hero.ammo_fire,
          "ammo_poison": hero.ammo_poison,
          "ammo_rubber": hero.ammo_rubber,
          "ammo_sleep": hero.ammo_sleep,
          "ammo_smart": hero.ammo_smart,
          "ammo_smoke": hero.ammo_smoke,
          "ammo_eye": hero.ammo_eye,
          "magazine": hero.magazine,
          "max_magazine": hero.max_magazine,
          "ammo": hero.ammo,
          "ammo_type": hero.ammo_type,
          "rocket_ammo": hero.rocket_ammo,
          "main_int": 0,
          "main_rea": 0,
          "main_dex": 0,
          "main_tec": 0,
          "main_coo": 0,
          "main_wil": 0,
          "main_luc": 0,
          "main_spe": 0,
          "main_bod": 0,
          "main_emp": 0,
          "slot1": 0,
          "slot2": 0,
          "slot3": 0,
          "slot4": 0,
          "slot5": 0,
          "slot6": 0,
          "slot7": 0,
          "slot8": 0,
          "slot9": 0,
          "slot10": 0,
          "slot11": 0,
          "slot12": 0,
          "slot13": 0,
          "slot14": 0,
          "slot15": 0,
        })
        implants.insert_one({
          "_id": uid,
          "name": name,
          "audio": "Мясо",
          "audio_slot1": 0,
          "audio_slot2": 0,
          "audio_slot3": 0,
          "right_eye": "Мясо",
          "right_eye_slot1": 0,
          "right_eye_slot2": 0,
          "right_eye_slot3": 0,
          "left_eye": "Мясо",
          "left_eye_slot1": 0,
          "left_eye_slot2": 0,
          "left_eye_slot3": 0,
          "neural": "Мясо",
          "neural_slot1": 0,
          "neural_slot2": 0,
          "neural_slot3": 0,
          "neural_slot4": 0,
          "neural_slot5": 0,
          "right_arm": "Мясо",
          "right_arm_slot1": 0,
          "right_arm_slot2": 0,
          "right_arm_slot3": 0,
          "right_arm_slot4": 0,
          "left_arm": "Мясо",
          "left_arm_slot1": 0,
          "left_arm_slot2": 0,
          "left_arm_slot3": 0,
          "left_arm_slot4": 0,
          "right_leg": "Мясо",
          "right_leg_slot1": 0,
          "right_leg_slot2": 0,
          "right_leg_slot3": 0,
          "left_leg": "Мясо",
          "left_leg_slot1": 0,
          "left_leg_slot2": 0,
          "left_leg_slot3": 0,
          "inside_slot1": 0,
          "inside_slot2": 0,
          "inside_slot3": 0,
          "inside_slot4": 0,
          "inside_slot5": 0,
          "inside_slot6": 0,
          "inside_slot7": 0,
          "outside_slot1": 0,
          "outside_slot2": 0,
          "outside_slot3": 0,
          "outside_slot4": 0,
          "outside_slot5": 0,
          "outside_slot6": 0,
          "outside_slot7": 0,
          "style_slot1": 0,
          "style_slot2": 0,
          "style_slot3": 0,
          "style_slot4": 0,
          "style_slot5": 0,
          "style_slot6": 0,
          "style_slot7": 0,
          "borg_slot1": 0,
          "borg_slot2": 0,
          "borg_slot3": 0,
          "borg_slot4": 0,
          "borg_slot5": 0,
          "borg_slot6": 0,
          "borg_slot7": 0,
        })

        await state.finish()
      await asyncio.sleep(1)
      await message.answer(f'Удачной игры!')
      await message.answer(view.myProfile(), reply_markup=nav.profileMenu)

  else:
    await bot.send_message(message.chat.id, "У вас уже есть персонаж!")


@dp.message_handler(commands=['роль'])
async def cmd_start(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  getter = msg.replace(' для ', ',').split(',')
  player_role = getRole(getter)
  find = Finder(uid)
  p_name = str(getter[1])
  pid = find.getIdByName(p_name)
  status = find.status()
  if status[0] == True:
    players.update_one({"name": p_name}, {"$set": {"hero_class": player_role}})

    if getter[0] == "Рокербой":
      rockerboys.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Харизма",
        "lvl": 1,
        "exp": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Рокербой"}})

    if getter[0] == "Соло":
      solos.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Боевое чутьё",
        "lvl": 1,
        "exp": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Соло"}})

    if getter[0] == "Нетраннер":
      netrunners.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Интерфейс",
        "lvl": 1,
        "exp": 0,
        "action": 2,
        "deka": "Отсутствует",
        "program1": 0,
        "program2": 0,
        "program3": 0,
        "program4": 0,
        "program5": 0,
        "program6": 0,
        "program7": 0,
        "program8": 0,
        "program9": 0,
        "program10": 0,
        "program11": 0,
        "program12": 0,
        "program13": 0,
        "program14": 0,
        "program15": 0,
        "equip1": 0,
        "equip2": 0,
        "equip3": 0,
        "equip4": 0,
        "equip5": 0,
        "equip6": 0,
        "equip7": 0,
        "equip8": 0,
        "equip9": 0,
        "equip10": 0,
      })
      players.update_one({"name": p_name},
                         {"$set": {
                           "role_name": "Нетраннер"
                         }})

    if getter[0] == "Техник":
      techs.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Мастер",
        "lvl": 1,
        "exp": 0,
        "points": 2,
        "modern": 0,
        "crafter": 0,
        "creator": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Техник"}})

    if getter[0] == "Медтехник":
      reapers.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Медицина",
        "lvl": 1,
        "exp": 0,
        "points": 2,
        "surgeon": 0,
        "pharmacist": 0,
        "сryo": 0,
      })
      players.update_one({"name": p_name},
                         {"$set": {
                           "role_name": "Медтехник"
                         }})

    if getter[0] == "Медиа":
      medias.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Убедительность",
        "lvl": 1,
        "exp": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Медиа"}})

    if getter[0] == "Экзек":
      ekzeks.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Командная Работа",
        "lvl": 1,
        "exp": 0,
        "slave1": 0,
        "slave2": 0,
        "slave3": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Экзек"}})

    if getter[0] == "Законник":
      police.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Подкрепление",
        "lvl": 1,
        "exp": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Законник"}})

    if getter[0] == "Фиксер":
      fixer.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Делец",
        "lvl": 1,
        "exp": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Фиксер"}})

    if getter[0] == "Кочевник":
      nomads.insert_one({
        "_id": pid,
        "player": getter[1],
        "name": "Мото",
        "lvl": 1,
        "exp": 0,
      })
      players.update_one({"name": p_name}, {"$set": {"role_name": "Кочевник"}})

    await message.answer("Роль выдана")
    await message.delete()
  else:
    await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['выдать'])
async def cmd_start(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  rep = {" для ": ",", " на ": ","}
  rep = dict((re.escape(k), v) for k, v in rep.items())
  pattern = re.compile("|".join(rep.keys()))
  msg = pattern.sub(lambda m: rep[re.escape(m.group(0))], msg)
  getter = msg.replace(',', ',').split(',')
  name = getter[0]
  perk = getSkill(name)
  p_name = str(getter[2])
  finder = Finder(uid)
  status = finder.status()
  if status[0] == True:
    players.update_one({"name": p_name}, {
      "$push": {
        "traits": {
          "name": perk[0],
          "lvl": int(getter[1]),
          "base": perk[1]
        }
      }
    })
    await message.answer("Навык выдан")
    await message.delete()
  else:
    await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['считать_статы'])
async def sendfame(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  finder = Finder(uid)
  plr = finder.generalByName(msg)
  find = Finder(plr[6])
  status = finder.status()
  stats = find.stats()

  hp = 10 + (5 * (ceil(mean([stats[8], stats[5]]))))
  severe_injury = round(hp / 2)
  die_dice = round(hp / 5)
  humanity = stats[9] * 10
  if status[0] != False or status[1] != False:
    players.update_one({"name": msg}, {"$set": {"max_hp": hp}})
    players.update_one({"name": msg}, {"$set": {"hp": hp}})
    players.update_one({"name": msg},
                       {"$set": {
                         "severe_injury": severe_injury
                       }})
    players.update_one({"name": msg}, {"$set": {"die_dice": die_dice}})
    players.update_one({"name": msg}, {"$set": {"humanity": humanity}})

    await message.answer("Статы посчитаны")
  else:
    await message.answer("У вас нет прав")


@dp.message_handler(commands=['киберсчитать'])
async def sendfame(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  finder = Finder(uid)
  plr = finder.generalByName(msg)
  find = Finder(plr[6])
  status = finder.status()
  stats = find.stats()

  hp = 10 + (5 * (ceil(mean([stats[8], stats[5]]))))
  severe_injury = round(hp / 2)
  die_dice = round(hp / 5)
  if status[0] != False or status[1] != False:
    players.update_one({"name": msg}, {"$set": {"max_hp": hp}})
    players.update_one({"name": msg}, {"$set": {"hp": hp}})
    players.update_one({"name": msg},
                       {"$set": {
                         "severe_injury": severe_injury
                       }})
    players.update_one({"name": msg}, {"$set": {"die_dice": die_dice}})

    await message.answer("Статы посчитаны")
  else:
    await message.answer("У вас нет прав")


@dp.message_handler(commands=['стат'])
async def cmd_start(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  rep = {" для ": ",", " на ": ","}
  rep = dict((re.escape(k), v) for k, v in rep.items())
  pattern = re.compile("|".join(rep.keys()))
  msg = pattern.sub(lambda m: rep[re.escape(m.group(0))], msg)
  getter = msg.replace(',', ',').split(',')
  p_name = str(getter[2])
  stat = int(getter[1])
  finder = Finder(uid)
  status = finder.status()
  if status[0] is True or status[1] is True:

    if getter[0] == "Интеллект":
      players.update_one({"name": p_name}, {"$set": {"intelligence": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_int": stat}})

    if getter[0] == "Реакция":
      players.update_one({"name": p_name}, {"$set": {"reaction": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_rea": stat}})

    if getter[0] == "Ловкость":
      players.update_one({"name": p_name}, {"$set": {"dexterity": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_dex": stat}})

    if getter[0] == "Техника":
      players.update_one({"name": p_name}, {"$set": {"technics": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_tec": stat}})

    if getter[0] == "Крутость":
      players.update_one({"name": p_name}, {"$set": {"cool": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_coo": stat}})

    if getter[0] == "Воля":
      players.update_one({"name": p_name}, {"$set": {"will": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_wil": stat}})

    if getter[0] == "Удача":
      players.update_one({"name": p_name}, {"$set": {"luck": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_luc": stat}})

    if getter[0] == "Скорость":
      players.update_one({"name": p_name}, {"$set": {"speed": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_spe": stat}})

    if getter[0] == "Телосложение":
      players.update_one({"name": p_name}, {"$set": {"bodytype": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_bod": stat}})

    if getter[0] == "Эмпатия":
      players.update_one({"name": p_name}, {"$set": {"empathy": stat}})
      players.update_one({"name": p_name}, {"$set": {"main_emp": stat}})

    await message.answer("Навык выдан")
  else:
    await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['киберстат'])
async def cmd_start(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  rep = {" для ": ",", " на ": ","}
  rep = dict((re.escape(k), v) for k, v in rep.items())
  pattern = re.compile("|".join(rep.keys()))
  msg = pattern.sub(lambda m: rep[re.escape(m.group(0))], msg)
  getter = msg.replace(',', ',').split(',')
  p_name = str(getter[2])
  stat = int(getter[1])
  finder = Finder(uid)
  status = finder.status()
  if status[0] is True or status[1] is True:

    if getter[0] == "Интеллект":
      players.update_one({"name": p_name}, {"$set": {"intelligence": stat}})

    if getter[0] == "Реакция":
      players.update_one({"name": p_name}, {"$set": {"reaction": stat}})

    if getter[0] == "Ловкость":
      players.update_one({"name": p_name}, {"$set": {"dexterity": stat}})

    if getter[0] == "Техника":
      players.update_one({"name": p_name}, {"$set": {"technics": stat}})

    if getter[0] == "Крутость":
      players.update_one({"name": p_name}, {"$set": {"cool": stat}})

    if getter[0] == "Воля":
      players.update_one({"name": p_name}, {"$set": {"will": stat}})

    if getter[0] == "Удача":
      players.update_one({"name": p_name}, {"$set": {"luck": stat}})

    if getter[0] == "Скорость":
      players.update_one({"name": p_name}, {"$set": {"speed": stat}})

    if getter[0] == "Телосложение":
      players.update_one({"name": p_name}, {"$set": {"bodytype": stat}})

    if getter[0] == "Эмпатия":
      players.update_one({"name": p_name}, {"$set": {"empathy": stat}})

    await message.answer("Навык выдан")
  else:
    await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['навык'])
async def cmd_start(message: types.Message):
  msg = message.get_args()
  perk = getSkill(msg)
  await message.answer(f"""
Навык: {perk[0]}

Характеристика: {perk[1]}

Описание: {perk[2]}
    """)


@dp.message_handler(commands=['перечислить'])
async def sendmon(message: types.Message):
  uid = message.from_user.id
  find = Finder(uid)
  userMon = find.money()
  msg = message.get_args()
  getter = msg.replace(' для ', ',').split(',')
  money = int(getter[0])
  if userMon >= money:
    send_money(uid, msg)
    await message.answer("Перевод проведен успешно")
  else:
    await message.answer("У вас недостаточно эдди")


@dp.message_handler(commands=['известность'])
async def sendfame(message: types.Message):
  uid = message.from_user.id
  find = Finder(uid)
  status = find.status()
  msg = message.get_args()
  if status[0] != False or status[1] != False:
    send_exp(uid, msg)
    await message.answer("Известность повышена")
  else:
    await message.answer("У вас нет прав")


@dp.message_handler(commands=['банк'])
async def bank(message: types.Message):
  uid = message.from_user.id
  find = Finder(uid)
  status = find.status()
  msg = message.get_args()
  if status[0] != False or status[1] != False:
    bank_gm(uid, msg)
    await message.answer("Средства перечислены")
  else:
    await message.answer("У вас нет прав")


@dp.message_handler(commands=['оплатить'])
async def bank(message: types.Message):
  uid = message.from_user.id
  find = Finder(uid)
  status = find.money()
  msg = message.get_args()
  if int(msg) <= status:
    bank_pl(uid, msg)
    await message.answer("Средства перечислены")
  else:
    await message.answer("У вас недостаточно средств")


@dp.message_handler(commands=['оружие'])
async def equipwp(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  slot = int(msg)
  owner = find.backpack()
  for_key = slot - 1
  owner_item = owner[for_key]
  func = equip_wp(uid, msg)

  if func is True:
    await message.answer(f"Вы экипировали {owner_item}")
  else:
    await message.answer("Это не оружие")


@dp.message_handler(commands=['броня'])
async def equipwp(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  slot = int(msg)
  owner = find.backpack()
  for_key = slot - 1
  owner_item = owner[for_key]
  func = equip_armor(uid, msg)

  if func is True:
    await message.answer(f"Вы экипировали {owner_item}")
  else:
    await message.answer("Это не броня")


@dp.message_handler(commands=['снять'])
async def output_eq(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  print(uid, msg)
  func = output(uid, msg)

  if func is True:
    await message.answer(f"Вы cняли предмет")
  else:
    await message.answer("Слот пуст")


@dp.message_handler(commands=['выдать_программу'])
async def cmd_prog(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  status = find.status()
  inter = Interface(uid)
  func = inter.buyProgram(msg)

  if status[0] != False or status[1] != False and func is True:

    await message.answer(f"Программа выдана")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['выдать_предмет'])
async def cmd_prog(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  status = find.status()
  func = buyWp(uid, msg)

  if status[0] != False or status[1] != False and func is True:

    await message.answer(f"Предмет выдана")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['опыт'])
async def cmd_start(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  getter = msg.replace(' для ', ',').split(',')
  finder = Finder(uid)
  status = finder.status()
  adm = Admin(uid)
  func = adm.giveExp(msg)
  if status[0] == True:
    await message.answer(f"{getter[1]} получил {func} опыта")

  else:
    await message.answer("У вас недостаточно прав.")


@dp.message_handler(commands=['дать'])
async def give(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  getter = msg.replace(' для ', ',').split(',')
  slot = int(getter[0])
  owner = find.backpack()
  for_key = slot - 1
  owner_item = owner[for_key]
  func = giveItem(uid, msg)

  if func is True:
    await message.answer(f"Вы передали {owner_item} в руки {getter[1]}")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['купить_броню'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  func = buyArmor(uid, msg)
  find = Finder(uid)
  status = find.status()

  if func is True and status[0] is True or status[1] is True:
    await message.answer(f"Вы купили броню")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['дать'])
async def give(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  getter = msg.replace(' для ', ',').split(',')
  slot = int(getter[0])
  owner = find.backpack()
  for_key = slot - 1
  owner_item = owner[for_key]
  func = giveItem(uid, msg)

  if func is True:
    await message.answer(f"Вы передали {owner_item} в руки {getter[1]}")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['прокачать'])
async def give(message: types.Message):
  uid = message.from_user.id
  role = Role(uid)
  msg = message.get_args()

  if msg == "Модернизация" or msg == "Изготовитель" or msg == "Изобретатель":
    role.techPoint(msg)
    await message.answer(f"Вы улучшили навык")
  elif msg == "Хирургия" or msg == "Фармацевтика" or msg == "Изобретатель":
    role.medPoint(msg)
    await message.answer(f"Вы улучшили навык")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['r'])
async def cmd_wp(message: types.Message):
  name = message.from_user.first_name
  msg = message.get_args()
  dice = d20.roll(str(msg))
  await message.answer(f"{name}: {dice}")


@dp.message_handler(commands=['вычесть'])
async def give(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  func = getDamage(uid, msg)

  if func is False:
    await message.answer(f"Урон вычтен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['уровень'])
async def lup(message: types.Message):
  uid = message.from_user.id
  role = Role(uid)
  a = role.lvlUp()
  if a is True:
    await message.answer(f"Команда выполнена успешно")
  else:
    await message.answer(f"У вас недостаточно опыта")


@dp.message_handler(commands=['лечить'])
async def cmd_heal(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    getHealth(uid, msg)
    await message.answer(f"Вы успешно вылечили")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['человечность'])
async def cmd_hum(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  status = find.status()
  admin = Admin(uid)

  if status[0] is True or status[1] is True:
    admin.humman(msg)
    await message.answer(f"Вы успешно лишили человечности")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['кибеимплант'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.setupPorts(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['купить_деку'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  deka = Interface(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    deka.deka(msg)
    await message.answer(f"Дека куплена")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['нейролинк'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.neur(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['правый_глаз'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.reye(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['левый_глаз'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.leye(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['правая_рука'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.rarm(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['левая_рука'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.larm(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['правая_нога'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.rleg(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['левая_нога'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.lleg(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['внутри'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.inside(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['снаружи'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.outs(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['стиль'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.style(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['борг'])
async def cmd_armor(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.borg(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['аудио'])
async def cmd_audio(message: types.Message):
  uid = message.from_user.id
  msg = message.get_args()
  find = Finder(uid)
  imp = Implants(uid)
  status = find.status()

  if status[0] is True or status[1] is True:
    imp.audio(msg)
    await message.answer(f"Имплант установлен")
  else:
    await message.answer("У вас не вышло")


@dp.message_handler(commands=['get'])
async def cmd_get(message: types.Message):
  pass


@dp.message_handler()
async def cmd_prof(message: types.Message):
  user_id = message.from_user.id
  find = Finder(user_id)
  view = View(user_id)
  role = find.skills()

  if message.text == 'Профиль' or message.text == 'Вернуться назад':
    await message.delete()
    await message.answer(view.myProfile(), reply_markup=nav.profileMenu)

  if message.text == 'Характеристики':
    await message.delete()
    await message.answer(view.myStats(), reply_markup=nav.back)

  if message.text == 'Имущество':
    await message.delete()
    await message.answer(view.myProperty(), reply_markup=nav.back)

  if message.text == 'Экипировка':
    await message.delete()
    await message.answer(view.myEquip(), reply_markup=nav.back)

  if message.text == 'Навыки':
    await message.delete()
    await message.answer(view.mySkills(), reply_markup=nav.back)

  if message.text == 'Импланты':
    await message.delete()
    await message.answer(view.implants(), reply_markup=nav.back)

  if message.text == 'Способность':
    await message.delete()
    if role[4] == "Рокербой":
      await message.answer(view.rockeboy(), reply_markup=nav.back)
    if role[4] == "Соло":
      await message.answer(view.solo(), reply_markup=nav.back)
    if role[4] == "Нетраннер":
      await message.answer(view.netrunner(), reply_markup=nav.back)
    if role[4] == "Техник":
      await message.answer(view.tech(), reply_markup=nav.back)
    if role[4] == "Медтехник":
      await message.answer(view.reaper(), reply_markup=nav.back)
    if role[4] == "Медиа":
      await message.answer(view.media(), reply_markup=nav.back)
    if role[4] == "Законник":
      await message.answer(view.police(), reply_markup=nav.back)
    if role[4] == "Экзек":
      await message.answer(view.ekzek(), reply_markup=nav.back)
    if role[4] == "Фиксер":
      await message.answer(view.fixer(), reply_markup=nav.back)
    if role[4] == "Кочевник":
      await message.answer(view.nomad(), reply_markup=nav.back)


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
