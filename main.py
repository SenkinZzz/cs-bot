from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
global i
global s
global x1
global x2
global x3
global x4
global a
global ans
i=' '
s=' '
x1=0
x2=0
x3=0
x4=0
a=0
ans=0
def tobase(num,base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b=alpha[num % base]
    while num>= base :
        num //=base
        b+= alpha[num % base]
    return b[::-1] 


button_hi= KeyboardButton('Привет ✌')
button_help= KeyboardButton('/help')
button_go= KeyboardButton('Погнали🚀')
button_plus= KeyboardButton('Сложение +')
button_minus= KeyboardButton('Вычитание -')
button_multiply= KeyboardButton('Умножение *')
button_divide1= KeyboardButton('Деление /')
button_divide2= KeyboardButton('Целочисленное деление //')
button_divide3= KeyboardButton('Остаток от деления %')
button_stepen= KeyboardButton('возведение в степень ^')
button_getsum= KeyboardButton('Получить значение суммы')
button_getrazn= KeyboardButton('Получить значение разности')
button_getpr= KeyboardButton('Получить значение произведения')
button_again= KeyboardButton('Начать заново')
button_back= KeyboardButton('Сделать шаг назад')

bot = Bot(token='2141769357:AAGTHpnRU5APhNLE-PNUD3MjmHCHT3oqtVQ')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('shjsnf',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi))

    
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("""Мой функционал относительно прост.
Я провожу математические оперции с числами.
Но доля оригинальности всё же присутствует✅✅✅
После каждого ввода числа, я запрашиваю значение системы счисления, которой принадлежит число.
Теперь, когда мы познакомились, нажми кнопку "Погнали🚀"   """)

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    global i
    global s
    global x1
    global x2
    global x3
    global x4
    global a
    global ans
    if message.text == 'Привет ✌':
        await message.answer(f"""Привет {message.chat.first_name}!!!🎉🎉🎉\nЯ телеграм бот Батуа🐗🐗🐗.
Меня создал ученик 10"З" класса, Сенькин Евгений🧠🧠🧠 @ukr_op.
Если ты не знаешь как я работаю, то для ознакомления с моим функционалом нажми кнопку /help.""",reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_help,button_go))
    elif message.text == 'Начать заново' or message.text == 'Погнали🚀':
        await message.answer('Выберите действие',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True)
                            .add(button_plus,button_minus)
                            .add(button_multiply,button_divide1)
                            .add(button_divide2)
                            .add(button_divide3)
                            .add(button_stepen))
    elif message.text =='Сложение +':
        s='+'
        await message.answer('Введите первое слагаемое',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='Вычитание -':
        s='-'
        await message.answer('Введите уменьшаемое число',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='Умножение *':
        s='*'
        await message.answer('Введите первый множитель',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='Деление /':
        pass
    elif message.text =='Целочисленное деление //':
        pass
    elif message.text =='Остаток от деления %':
        pass
    elif message.text =='Возведение в степень ^':
        pass
    elif message.text== 'Получить значение суммы' or message.text== 'Получить значение разности' or message.text== 'Получить значение произведения':
        await message.answer(ans,reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_again))
    elif message.text =='Сделать шаг назад':
        if i=='x1':
            await message.answer('Выберите действие',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True)
                            .add(button_plus,button_minus)
                            .add(button_multiply,button_divide1)
                            .add(button_divide2)
                            .add(button_divide3)
                            .add(button_stepen))
        elif i=='x2':
            i='x1'
            if s=='+':
                await message.answer('Введите первое слагаемое.')
            elif s=='-':
                await message.answer('Введите уменьшаемое число.')
            elif s=='*':
                await message.answer('Введите первый множитель.')
        elif i=='x3':
            i='x2'
            if s=='+':
                await message.answer('Введите значение системы счисления первого слагаемого.')
            elif s=='-':
                await message.answer('Введите значение системы счисления уменьшаемого числа.')
            elif s=='*':
                await message.answer('Введите значение системы счисления первого множителя.')
        elif i=='x4':
            i='x3'
            if s=='+':
                await message.answer('Введите второе слагаемое.')
            elif s=='-':
                await message.answer('Введите вычитаемое число.')
            elif s=='*':
                await message.answer('Введите второй множитель.')
        elif i=='a':
            i='x4'
            if s=='+':
                await message.answer('Введите значение системы счисления второго слагаемого.')
            elif s=='-':
                await message.answer('Введите значение системы счисления вычитаемого числа.')
            elif s=='*':
                await message.answer('Введите значение системы счисления второго множителя.')
        elif i=='ans':
            i='a'
            if s=='+':
                await message.answer('Введите значение системы счисления суммы.',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='-':
                await message.answer('Введите значение системы счисления разности.',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='*':
                await message.answer('Введите значение системы счисления произведения.',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
    elif s=='+' or s=='-' or s=='*' or s=='/' or s=='//' or s=='%' or s=='^':
        if i=='x1':
            x1=message.text
            i='x2'
            if s=='+':
                await message.answer('Введите значение системы счисления первого слагаемого.')
            elif s=='-':
                await message.answer('Введите значение системы счисления уменьшаемого числа.')
            elif s=='*':
                await message.answer('Введите значение системы счисления первого множителя.')
        elif i=='x2':
            try:
                x2=int(message.text)
                try:
                    x1=int(str(x1),x2)
                    i='x3'
                    if s=='+':
                        await message.answer('Введите второе слагаемое.')
                    elif s=='-':
                        await message.answer('Введите вычитаемое число.')
                    elif s=='*':
                        await message.answer('Введите второй множитель.')
                except ValueError:
                    i='x1'
                    if s=='+':
                        await message.answer('Ошибка конвертирования числа в СС.\nВведите первое слагаемое заново.')
                    elif s=='-':
                        await message.answer('Ошибка конвертирования числа в СС.\nВведите уменьшаемое число заново.')
                    elif s=='*':
                        await message.answer('Ошибка конвертирования числа в СС.\nВведите первый множитель заново.')
            except ValueError:
                if s=='+':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС первого слагаемого заново.')
                elif s=='-':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС уменьшаемого числа заново.')
                elif s=='*':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС первого множителя заново.')
        elif i=='x3':
            x3=message.text
            i='x4'
            if s=='+':
                await message.answer('Введите значение системы счисления второго слагаемого.')
            elif s=='-':
                await message.answer('Введите значение системы счисления вычитаемого числа.')
            elif s=='*':
                await message.answer('Введите значение системы счисления второго множителя.')
        elif i=='x4':
            try:
                x4=int(message.text)
                try:
                    x3=int(str(x3),x4)
                    i='a'
                    if s=='+':
                        await message.answer('Введите значение системы счисления суммы.')
                    elif s=='-':
                        await message.answer('Введите значение системы счисления разности.')
                    elif s=='*':
                        await message.answer('Введите значение системы счисления произведения.')
                except ValueError:
                    i='x3'
                    if s=='+':
                        await message.answer('Ошибка конвертирования числа в СС.\nВведите второе слагаемое заново.')
                    elif s=='-':
                        await message.answer('Ошибка конвертирования числа в СС.\nВведите вычитаемое число заново.')
                    if s=='*':
                        await message.answer('Ошибка конвертирования числа в СС.\nВведите второй множитель заново.')
            except ValueError:
                if s=='+':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС второго слагаемого заново.')
                elif s=='-':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС вычитаемого числа заново.')
                elif s=='*':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС второго множителя заново.')
        elif i=='a':
            try:
                a=int(message.text)
                b=int('1',a)
                i='ans'
                if s=='+':
                    ans=x1+x3
                    ans=tobase(ans,a)
                    await message.answer('Значение суммы посчитано.',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getsum,button_back))
                elif s=='-':
                    ans=x1-x3
                    if ans<0:
                        ans=int(tobase(0-ans,a))
                        ans=0-ans
                    else:
                        ans=tobase(ans,a)
                    await message.answer('Значение разности посчитано.',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getrazn,button_back))
                elif s=='*':
                    ans=x1*x3
                    ans=tobase(ans,a)
                    await message.answer('Значение произведения посчитано.',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getpr,button_back))
            except ValueError:
                if s=='+':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС суммы заново.')
                elif s=='-':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС разности заново.')
                elif s=='*':
                    await message.answer('Ошибка считывания значения СС.\nВведите значение СС произведения заново.')
    else:
        await message.answer('Ошибка!!!\nНеизвестная команда👺')


if __name__ == '__main__':
    executor.start_polling(dp)


