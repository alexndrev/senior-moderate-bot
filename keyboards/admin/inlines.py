from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnAddPhoto = InlineKeyboardButton('📸 Додати фото', callback_data='add_photo')
btnNext = InlineKeyboardButton('Відправити 😎', callback_data='next')
btnQuit = InlineKeyboardButton('Відміна 🚫', callback_data='quit')
btnGitHub = InlineKeyboardButton('Source on GitHub ⚙', url='')
btnCommands = InlineKeyboardButton('Команды', url='https://teletype.in/@alexndrev/TA8LkHJBbGR')

menuMailing = InlineKeyboardMarkup(resize_keyboard=True).add(btnAddPhoto, btnNext).add(btnQuit)
menuMailing2 = InlineKeyboardMarkup(resize_keyboard=True).add(btnNext, btnQuit)
menuCancel = InlineKeyboardMarkup(resize_keyboard=True).add(btnQuit)
