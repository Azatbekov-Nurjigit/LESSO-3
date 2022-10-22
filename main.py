import logging
from aiogram.utils import executor
from coin import  dp
from handlers import client, callback, fsmAdminMentor, eztra



client.register_handler_client(dp)
callback.register_handler_callback(dp)
fsmAdminMentor.register_handler_fsmAdminMentor(dp)
eztra.register_handler_ezta(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



# Подключаем своего бота к базе данных.
# Создаем таблицу для добавления ментора,
# можете назвать mentors
# В таблице должно быть поля:
# - ID ментора.
# - Имя ментора.
# - Напрвление.
# - Возраст ментора.
# - Группа
# Добавить все sql команды которые
# рассмотрели на уроке









