from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileStats = ReplyKeyboardMarkup(resize_keyboard=True)
back = ReplyKeyboardMarkup(resize_keyboard=True)
btnStats = KeyboardButton(text="Характеристики")
btnEquip = KeyboardButton(text="Экипировка")
btnBp = KeyboardButton(text="Имущество")
btnSkills = KeyboardButton(text="Навыки")
btnRole = KeyboardButton(text="Способность")
btnImpl = KeyboardButton(text="Импланты")

btnBack = KeyboardButton(text="Вернуться назад")


profileMenu.add(btnStats, btnEquip, btnBp, btnSkills, btnRole, btnImpl)
back.add(btnBack)

