from mongodb import Finder
from update import updateRank
from system import catchSkill
from programs import Interface
from roles import Role

class View:

    def __init__(self, uid):
        self.uid = uid

    def myStats(self):
        finder = Finder(self.uid)
        stats = finder.stats()
        skills = finder.skills()
        text = f"""
------------------------------------------------
            Характеристики

    Интеллект: {stats[0]}
    Реакция: {stats[1]}
    Ловкость: {stats[2]}
    Техника: {stats[3]}
    Крутость: {stats[4]}
    Воля: {stats[5]}
    Удача: {stats[6]}
    Скорость: {stats[7]}
    Телосложение: {stats[8]}
    Эмпатия: {stats[9]}

    Человечность: {skills[3]} из 100
------------------------------------------------
    """
        return text

    def myProfile(self):
        finder = Finder(self.uid)
        gen_info = finder.generalInfo()
        money = finder.money()
        hp = finder.hpInfo()
        other = finder.otherInfo()
        role = finder.skills()
        rank = finder.ranks(gen_info[2])
        status = finder.status()
        updateRank(self.uid)
        text = f"""
------------------------------------------------
    {role[4]} {gen_info[0]}

    Известность: {rank[0]}
    Очки известности: {gen_info[3]}

    Здоровье: {hp[1]} из {hp[0]}
    Лёгкое ранение: {hp[2]}
    Тяжёлое ранение: {hp[3]}

    Trauma Team: {status[3]}

    Евродоллары: {money}
------------------------------------------------
    """
        return text

    def myProperty(self):
        finder = Finder(self.uid)
        geninf = finder.generalInfo()
        bp = finder.backpack()

        text = f"""
------------------------------------------------
                Иммущество

    Слот 1: {bp[0]}
    Слот 2: {bp[1]}
    Слот 3: {bp[2]}
    Слот 4: {bp[3]}
    Слот 5: {bp[4]}
    Слот 6: {bp[5]}
    Слот 7: {bp[6]}
    Слот 8: {bp[7]}
    Слот 9: {bp[8]}
    Слот 10: {bp[9]}
    Слот 11: {bp[10]}
    Слот 12: {bp[11]}
    Слот 13: {bp[12]}
    Слот 14: {bp[13]}
    Слот 15: {bp[14]}
------------------------------------------------
    """
        return text

    def myEquip(self):
        finder = Finder(self.uid)
        equip = finder.equipment()
        
        mods = finder.weapMods()
      
        if equip[0] == 0:
            weap = "Отсутствует"
        else:
            weap = equip[0]

        text = f"""
------------------------------------------------
                    Экипировка

    Оружие: {weap}

    Обвесы:
    Прицел: {mods[1]}
    Коннектор: {mods[3]}
    Насадка: {mods[2]}

    Защита: {equip[1]} | {equip[2]}

------------------------------------------------
        """
        return text

    def mySkills(self):
        
        catch = catchSkill(self.uid)
        def slist(prop):
            text = ''
            for x in prop:
                text += f"""{x}\n\n"""
            return text
        text = f"""
------------------------------------------------
                    Навыки

{slist(catch)}           
------------------------------------------------
        """
        return text

    def netrunner(self):
        finder = Finder(self.uid)
        bp = finder.nrPrograms()
        equip = finder.nrEquip()
        inter = Interface(self.uid)
        inter.updateAction()
        deka = finder.getNRunner()
        text = f"""
------------------------------------------------
                ИНТЕРФЕЙС
------------------------------------------------
                {deka[5]}

    Программа 1: {bp[0]}
    Программа 2: {bp[1]}
    Программа 3: {bp[2]}
    Программа 4: {bp[3]}
    Программа 5: {bp[4]}
    Программа 6: {bp[5]}
    Программа 7: {bp[6]}
    Программа 8: {bp[7]}
    Программа 9: {bp[8]}
    Программа 10: {bp[9]}
    Программа 11: {bp[10]}
    Программа 12: {bp[11]}
    Программа 13: {bp[12]}
    Программа 14: {bp[13]}
    Программа 15: {bp[14]}

********************************

    Оборудывание 1: {equip[0]}
    Оборудывание 2: {equip[1]}
    Оборудывание 3: {equip[2]}
    Оборудывание 4: {equip[3]}
    Оборудывание 5: {equip[4]}
    Оборудывание 6: {equip[5]}
    Оборудывание 7: {equip[6]}
    Оборудывание 8: {equip[7]}
    Оборудывание 9: {equip[8]}
    Оборудывание 10: {equip[9]}

------------------------------------------------
    
    Ранг навыка: {deka[2]}
    Опыт: {deka[3]}

    Действий в системе: {deka[4]}  
------------------------------------------------
    """
        return text
    
    def rockeboy(self):
        finder = Finder(self.uid)
        info = finder.rockerboy()
        text = f"""
------------------------------------------------
                ХАРИЗМА
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def solo(self):
        finder = Finder(self.uid)
        info = finder.solo()
        text = f"""
------------------------------------------------
                БОЕВОЕ ЧУТЬЁ
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def media(self):
        finder = Finder(self.uid)
        info = finder.media()
        text = f"""
------------------------------------------------
                ДОВЕРИЕ
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def police(self):
        finder = Finder(self.uid)
        info = finder.police()
        text = f"""
------------------------------------------------
                ПОДКРЕПЛЕНИЕ
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def fixer(self):
        finder = Finder(self.uid)
        info = finder.fixer()
        text = f"""
------------------------------------------------
                ВОРОТИЛА
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def ekzek(self):
        finder = Finder(self.uid)
        info = finder.ekzek()
        text = f"""
------------------------------------------------
                КОМАНДНАЯ РАБОТА
------------------------------------------------

    Подчиненный: {info[4]}
    Подчиненный: {info[5]}
    Подчиненный: {info[6]}

------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def nomad(self):
        finder = Finder(self.uid)
        info = finder.nomad()
        text = f"""
------------------------------------------------
                МОТО
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def tech(self):
        finder = Finder(self.uid)
        info = finder.tech()
        text = f"""
------------------------------------------------
                СОЗДАТЕЛЬ
------------------------------------------------

    Свободные очки: {info[4]}
    
    Мастер модернизации: {info[5]}
    Мастер изготовления: {info[6]}
    Мастер изобретатель: {info[7]}

------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def reaper(self):
        finder = Finder(self.uid)
        info = finder.reaper()
        text = f"""
------------------------------------------------
                Медицина
------------------------------------------------

    Свободные очки: {info[4]}
    
    Хирургия: {info[5]}
    МедТех(Фармацевтика): {info[6]}
    МедТех(Криосистемы): {info[7]}

------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def implants(self):
        find = Finder(self.uid)
        audio = find.audio()
        reye = find.right_eye()
        leye = find.left_eye()
        rarm = find.right_arm()
        larm = find.left_arm()
        rleg = find.right_leg()
        lleg = find.left_leg()
        neural = find.neural()
        inside = find.inside()
        outside = find.outside()
        style = find.style()
        borg = find.borg()
        port = find.ports()

        text = f"""
------------------------------------------------
                    Импланты

    Аудио разьем: {port[0]}
    Слот 1: {audio[0]}
    Слот 2: {audio[1]}
    Слот 3: {audio[2]}

    Правый глаз: {port[1]}
    Слот 1: {reye[0]}
    Слот 2: {reye[1]}
    Слот 3: {reye[2]}

    Левый глаз: {port[2]}
    Слот 1: {leye[0]}
    Слот 2: {leye[1]}
    Слот 3: {leye[2]}

    Нейроинтерфейс: {port[7]}
    Слот 1: {neural[0]}
    Слот 2: {neural[1]}
    Слот 3: {neural[2]}
    Слот 4: {neural[3]}
    Слот 5: {neural[4]}

    Правая рука: {port[3]}
    Слот 1: {rarm[0]}
    Слот 2: {rarm[1]}
    Слот 3: {rarm[2]}
    Слот 4: {rarm[3]}


    Левая рука: {port[4]}
    Слот 1: {larm[0]}
    Слот 2: {larm[1]}
    Слот 3: {larm[2]}
    Слот 4: {larm[3]}

    
    Правая нога: {port[5]}
    Слот 1: {rleg[0]}
    Слот 2: {rleg[1]}
    Слот 3: {rleg[2]}


    Левая нога: {port[6]}
    Слот 1: {lleg[0]}
    Слот 2: {lleg[1]}
    Слот 3: {lleg[2]}
  

    Внутр. импланты:
    Слот 1: {inside[0]}
    Слот 2: {inside[1]}
    Слот 3: {inside[2]}
    Слот 4: {inside[3]}
    Слот 5: {inside[4]}
    Слот 6: {inside[5]} 
    Слот 7: {inside[6]}

    Внешние импланты:
    Слот 1: {outside[0]}
    Слот 2: {outside[1]}
    Слот 3: {outside[2]}
    Слот 4: {outside[3]}
    Слот 5: {outside[4]}
    Слот 6: {outside[5]}
    Слот 7: {outside[6]}


    Стилевые импланты:
    Слот 1: {style[0]}
    Слот 2: {style[1]}
    Слот 3: {style[2]}
    Слот 4: {style[3]}
    Слот 5: {style[4]}
    Слот 6: {style[5]}
    Слот 7: {style[6]}


    Боргирование:
    Слот 1: {borg[0]}
    Слот 2: {borg[1]}
    Слот 3: {borg[2]}
    Слот 4: {borg[3]}
    Слот 5: {borg[4]}
    Слот 6: {borg[5]}
    Слот 7: {borg[6]}

------------------------------------------------
        """
        return text