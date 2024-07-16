import asyncio
import time
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

bot = Bot(token='7439070470:AAGGfljGb7OSZodWOQU_9oWOO1_fOg8tiuI')
dp = Dispatcher()

eslatmalar = []

class Eslatma(StatesGroup):
    eslatma_info = State()

main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='➕Eslatma yaratish')],
    [KeyboardButton(text='📋Eslatmalar')]
])

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('🔽O\'zingizga kerakli bo\'limni tanlang:', reply_markup=main_button)

@dp.message(F.text=='📋Eslatmalar')
async def eslatmalar_info(message: Message):
    if len(eslatmalar) == 0:
        await message.answer('Hali eslatmalar yo\'q🤷‍♂️')
    else:
        eslatmalar_text='\n\n'.join(eslatmalar)
        await message.answer('📋Eslatmalar:\n\n'+eslatmalar_text)

@dp.message(F.text=='➕Eslatma yaratish')
async def new_eslatma(message: Message, state: FSMContext):
    await state.set_state(Eslatma.eslatma_info)
    await message.answer('❗️Eslatmani huddi shunday tarzda yozib qoldiring:\n\nEslatmaNomi-EslatmaHaqidaMa\'lumot')

@dp.message(Eslatma.eslatma_info)
async def set_eslatma(message: Message, state: FSMContext):
    global eslatmalar
    await state.update_data(eslatma=message.text)
    data = await state.get_data()
    eslatmalar.append(data['eslatma'])
    await message.answer('✏️')
    time.sleep(1)
    await message.answer(f'✅Yangi eslatma yaratildi\n\n{data["eslatma"]}')
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
