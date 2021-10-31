from aiogram import executor #В ней лежит старт пулинг, с помощью которого мы запускаем бота

from loader import dp #С лоадера в этом проекте испортируем диспатчер - доставщика наших обновлений
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup) #Эта функция запускает бота

