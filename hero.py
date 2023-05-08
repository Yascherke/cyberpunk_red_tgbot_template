from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint
from statistics import mean
import d20


class Hero(StatesGroup):

    # Характеристики нафуй никому не нужные, ну только если для любитивлей рандома
    # def getStats():
    #     def roll():
    #         n = True
    #         while n is True:
    #             dice = d20.roll("1d8")
    #             res = dice.total
    #             if res == 1:
    #                 dice = d20.roll("1d8")     
    #                 res = dice.total
    #             else:
    #                 n = False
    #         return res

    #     intelligence = roll()
    #     reaction = roll()
    #     dexterity = roll()
    #     technics = roll()
    #     charisma = roll()
    #     will = roll()
    #     luck = roll()
    #     speed = roll()
    #     bodytype = roll()
    #     empathy = roll()

    #     main_int = intelligence
    #     main_rea = reaction
    #     main_dex = dexterity
    #     main_tec = technics
    #     main_cha = charisma
    #     main_wil = will
    #     main_luc = luck
    #     main_spe = speed
    #     main_bod = bodytype
    #     main_emp = empathy

    #     max_hp = 10 + (5 * (round(mean([bodytype, will]))))
    #     hp = max_hp
    #     severe_injury = round(max_hp / 2)
    #     die_dice = round(max_hp / 5)
    #     humanity = empathy * 10

    #     return [
    #         intelligence,
    #         reaction,
    #         dexterity,
    #         technics,
    #         cool,
    #         will,
    #         luck,
    #         speed,
    #         bodytype,
    #         empathy,
    #         max_hp,
    #         hp,
    #         severe_injury,
    #         die_dice,
    #         humanity,

    #         main_int,
    #         main_rea,
    #         main_dex,
    #         main_tec,
    #         main_coo,
    #         main_wil,
    #         main_luc,
    #         main_spe,
    #         main_bod,
    #         main_emp,
    #     ]

    def moneyRoll():
        def roll():

            dice1 = d20.roll("1d100")
            dice2 = d20.roll("1d20")

            money = dice1.total
            mod = dice2.total

            res = money * mod
            return res
        money = roll()
        return money

    # Основная информация
    hero_class = 0
    rank = 0
    rank_exp = 0

    crit_dmg = 'Нет'

    car = 0
    home = 0

    car_info = []

    trauma = 'Отсутствует'

    # Экипировка
    weapon = 0

    magazine = 0
    max_magazine = 0

    ammo = 0
    ammo_bb = 0
    ammo_toxin = 0
    ammo_emp = 0
    ammo_expansive = 0
    ammo_stun = 0
    ammo_fire = 0
    ammo_poison = 0
    ammo_rubber = 0
    ammo_sleep = 0
    ammo_smart = 0
    ammo_smoke = 0
    ammo_eye = 0
    ammo_type = 'Стандартные'
    rocket_ammo = 0

    armor = 0
    main_sp = 0
    sp = main_sp

    # Дополнительная информация
    tokens = 0

    gang = 0
    corp = 0
    organ = 0

    admin = False
    gm = False
    status = 0
    trauma = 0

    mission = 0
    mission_reward = 0
    progress = 0
    mission_count = 0

    # Способности
    inventory = 0
    traits = []
    implants = 0
    programs = 0
    notes = []

    role_name = 0

    name = State()
