from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo_router(message: types.Message):
    await message.reply("Я вас не понимаю, вот команды которые я понимаю: \n/start\n/picture")

