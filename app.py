from aiogram import executor #В ней лежит старт пулинг, с помощью которого мы запускаем бота

from loader import dp #С лоадера в этом проекте испортируем диспатчер - доставщика наших обновлений, сообщений и проч к обработчику
import middlewares, filters, handlers #Импортируются с нашего проекта, модули в таком порядке, чтобы они корректно работали
from utils.notify_admins import on_startup_notify #Оповещение администраторов, что бот запущен
from utils.set_bot_commands import set_default_commands #Функция установки дефолтных команд для бота


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup) #Эта функция запускает бота

