from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔗 Добавить рефссылку", callback_data="add_link")],
        [InlineKeyboardButton(text="📝 Ввести промпт", callback_data="enter_prompt")],
        [InlineKeyboardButton(text="🎬 Генерация видео", callback_data="gen_video")],
        [InlineKeyboardButton(text="📸 Генерация фото/карусели", callback_data="gen_carousel")],
        [InlineKeyboardButton(text="📄 Текст к фото/видео", callback_data="gen_description")],
        [InlineKeyboardButton(text="📋 Список партнёров", callback_data="list_partners")],
        [InlineKeyboardButton(text="📤 Экспорт контента", callback_data="export_content")]
    ])
    return keyboard

def select_partner_keyboard(partners_list):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for partner in partners_list:
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(text=f"✅ {partner}", callback_data=f"use_partner_{partner}")
        ])
    return keyboard
