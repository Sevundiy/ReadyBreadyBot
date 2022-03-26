import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
file_photo = open('D:\Python\cacao.png','rb')
file_photo1 = open('D:\Python\cherni.png','rb')
file_photo2 = open('D:\Python\milkulun.png','rb')
file_photo4 = open('D:\Python\kar.png','rb')
file_photo5 = open('D:\Python\obl.png','rb')
file_photo6 = open('D:\Python\chebr.png','rb')
file_photo7 = open('D:\Python\chocolate.jpg','rb')
file_photo8 = open('D:\Python\green.jpg','rb')
file_photo9 = open('D:\Python\malina.jpg','rb')
file_photo10 = open('D:\Python\white.jpg','rb')
file_photo11 = open('D:\Python\capuccino.jpg','rb')
file_photo12 = open('D:\Python\omericano.jpg','rb')
file_photo13 = open('D:\Python\latte.jpg','rb')
file_photo14 = open('D:\Python\mikellanjelo.jpg','rb')
file_photo15 = open('D:\Python\glace.jpg','rb')
file_photo17 = open('D:\Python\cocktale.jpg','rb')
file_photo16 = open('D:\Python\limonade.jpg','rb')
file_photo18 = open('D:\Python\smuzi.jpg','rb')
file_photo19 = open('D:\Python\protein.png','rb')
file_photo20 = open('D:\Python\parf.jpg','rb')

@bot.message_handler(commands=['start'])
def welcome(message):


	#keyboard
	def keyboard():
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Горячее")
		item2 = types.KeyboardButton("Холодное")

		markup.add(item1, item2)
		return markup

	

	bot.send_message(message.chat.id, "Привет, я бот, созданный чтобы помочь выбрать тебе напиток!" .format(message.from_user, bot.get_me()),
			parse_mode='html')
	bot.send_message(message.chat.id, "Что вы желаете выпить?" .format(message.from_user, bot.get_me()),
			parse_mode='html', reply_markup=keyboard())

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		
		if message.text == 'Горячее': 
			def keyboard2():
				markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item3 = types.KeyboardButton("Кофе")
				item4 = types.KeyboardButton("Не кофе")
				markup2.add(item3,item4)	
				return markup2
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard2())
					
		if message.text == 'Не кофе':
			def keyboard4():
				markup4 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item10 = types.KeyboardButton("Горячий шоколад")
				item11 = types.KeyboardButton("Какао")
				item12 = types.KeyboardButton("Чай")
				markup4.add(item10,item11,item12)	
				return markup4
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard4())

		if message.text == 'Какао':
			bot.send_message(message.chat.id,"Хороший выбор! Какао является натуральным антидепрессантом, т.к. в его составе присутствует фенилэтиламин. А еще холодное какао достаточно быстро восстанавливает мышцы после спортивных занятий или тяжёлой физической работы")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Горячий шоколад':
			bot.send_message(message.chat.id,"Хороший выбор! Выпитая чашка горячего шоколада повышает настроение. Это действует природный нейромедиатор какао бобов — фенэтитиламин, поднимающий жизненный тонус. Из-за наличия в горячем шоколаде биологически активных веществ после его употребления повышается работоспособность, головной мозг получает стимул для работы, улучшается память.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo7)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())
		
		if message.text == 'Чай':
			def keyboard5():
				markup5 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item13 = types.KeyboardButton("Авторский")
				item14 = types.KeyboardButton("Пакетированый")
				markup5.add(item13,item14)	
				return markup5
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard5()) 
			
		if message.text == 'Пакетированый':
			def keyboard6():
				markup6 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item15 = types.KeyboardButton("Чёрный")
				item16 = types.KeyboardButton("Зелёный")
				markup6.add(item15,item16)	
				return markup6
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard6()) 
		
		if message.text == 'Чёрный':
			bot.send_message(message.chat.id,"Хороший выбор! Чёрный чай укрепляет иммунитет, очищает организм и повышает концентрацию.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo1)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Зелёный':
			bot.send_message(message.chat.id,"Хороший выбор! Зеленый чай придает сил, борется с вялостью и депрессией, уменьшает сонливость.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo8)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Авторский': 
			def keyboard7():
				markup7 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item17 = types.KeyboardButton("Молочный улун")
				item18 = types.KeyboardButton("Малина + мята")
				item19 = types.KeyboardButton("Каркаде")
				item20 = types.KeyboardButton("Облепиха-имбирь")
				item21 = types.KeyboardButton("С чебрецом")
				markup7.add(item17,item18,item19,item20,item21)	
				return markup7
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard7())
		
		if message.text == 'Молочный улун':
			bot.send_message(message.chat.id,"Хороший выбор! Молочный улун способствует похудению, укрепляет иммунитет, а также имеет омолаживающий эффект.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo2)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Малина + мята':
			bot.send_message(message.chat.id,"Хороший выбор! Польза чая с малиной заключается в составе. Ягоды малины содержат клетчатку, дубильные вещества, пектины, магний, селен, железо, витамины.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo9)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Каркаде':
			bot.send_message(message.chat.id,"Хороший выбор! Чай каркаде способствует похудению, тонизирует и бодрит организм, а также поднимает настроение.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo4)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Облепиха-имбирь':
			bot.send_message(message.chat.id,"Хороший выбор! В этом чае содержится большое количество витаминов. Он поднимает настрение и обладает успокаивающим дейстием.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo5)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'С чебрецом':
			bot.send_message(message.chat.id,"Хороший выбор! Чай с чебрецом укрепляет иммунитет, успокаивает и восстанавливает силы.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo6)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())
		
		if message.text == 'Кофе':
			def keyboard8():
				markup8 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item22 = types.KeyboardButton("Более молочный")
				item23 = types.KeyboardButton("Более кофейный")
				markup8.add(item22,item23)	
				return markup8
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard8()) 
		
		if message.text == 'Более кофейный':
			def keyboard9():
				markup9 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item24 = types.KeyboardButton("С молоком")
				item25 = types.KeyboardButton("Без молока")
				markup9.add(item24,item25)	
				return markup9
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard9())

		if message.text == 'С молоком':
			def keyboard14():
				markup14 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item33 = types.KeyboardButton("Менее крепкий")
				item34 = types.KeyboardButton("Более крепкий")
				markup14.add(item33,item34)	
				return markup14
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard14()) 
		if message.text == 'Более крепкий': 
			def keyboard15():
				markup15 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item35 = types.KeyboardButton("Флэт-Уайт")
				markup15.add(item35)	
				return markup15
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard15())

		if message.text == 'Флэт-Уайт':
			bot.send_message(message.chat.id,"Хороший выбор! Флэт-Уайт наиболее насыщенный по вкусу и консистенции. Употреблять его рекомендуется в первой половине дня. Его не назовешь легким, но брутальная энергичность напитка прикрыта сливочной вуалью.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo10)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Менее крепкий':
			def keyboard16():
				markup16 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item36 = types.KeyboardButton("Капучино")
				markup16.add(item36)	
				return markup16
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard16())
		
		if message.text == 'Капучино':
			bot.send_message(message.chat.id,"Хороший выбор! В состав капучино входит кофе и молоко, а также сахар. Данный кофе бодрит, тонизирует, ускоряет метаболизм, повышает артериальное давление.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo11)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Без молока': 
			def keyboard17():
				markup17 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item37 = types.KeyboardButton("Американо")
				markup17.add(item37)	
				return markup17
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard17())

		if message.text == 'Американо':
			bot.send_message(message.chat.id,"Хороший выбор! Американо – беспроигрышный вариант для тех, кто любит латте или капучино, но следит за фигурой. Преимущество напитка – большой объём при низкой калорийности. Количество кофеина такое же, как в эспрессо, но концентрация значительно ниже.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo12)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Более молочный':
			def keyboard10():
				markup10 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item27 = types.KeyboardButton("C молоком")
				item28 = types.KeyboardButton("Со сливками")
				item29 = types.KeyboardButton("С мороженным")
				markup10.add(item27,item28,item29)	
				return markup10
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard10())
		
		if message.text == 'C молоком': 
			def keyboard11():
				markup11 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item30 = types.KeyboardButton("Латте")
				markup11.add(item30)	
				return markup11
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard11())

		if message.text == 'Латте':
			bot.send_message(message.chat.id,"Хороший выбор! Латте улучшает память и внимание, а также придат телу - тонус, а духу - бодрости.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo13)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())
	
		
		if message.text == 'Со сливками': 
			def keyboard12():
				markup12 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item31 = types.KeyboardButton("Раф-кофе")
				markup12.add(item31)	
				return markup12
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard12())

		if message.text == 'Раф-кофе':
			bot.send_message(message.chat.id,"Хороший выбор! Польза раф-кофе гораздо больше, чем классического. Дело в том, что сливки, используемые при приготовлении рафа, обладают большей питательной ценностью, чем обычное молоко, и содержат больше белка, витаминов и минеральных веществ.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo14)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())
		
		if message.text == 'С мороженным': 
			def keyboard13():
				markup13 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item32 = types.KeyboardButton("Глясе")
				markup13.add(item32)	
				return markup13
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard13())

		if message.text == 'Глясе':
			bot.send_message(message.chat.id,"Хороший выбор! Глясе содержит серотонин, благодаря чему улучшается настроение и работоспособность, а также успокаивает во время стресса.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo15)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		elif message.text == 'Холодное': 
			def keyboard3():
				markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item5 = types.KeyboardButton("Лимонад")
				item6 = types.KeyboardButton("Милкшейк")
				item7 = types.KeyboardButton("Смузи")
				item8 = types.KeyboardButton("Протеиновый коктейль")
				item9 = types.KeyboardButton("Фраппучино")

				markup3.add(item5,item6,item7,item8,item9)	
				return markup3
			bot.send_message(message.chat.id,"?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard3())

		if message.text == 'Лимонад':
			bot.send_message(message.chat.id,"Хороший выбор! Американский врач Франк Липман утверждает, что тонизирующий лимонад способен вывести шлаки/токсины, восстановить кислотно-щелочный баланс и зарядить организм энергией на весь день.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo16)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())
		
		if message.text == 'Милкшейк':
			bot.send_message(message.chat.id,"Хороший выбор! Полезные свойства молочного коктейля тяжело переоценить. Богатый на витамины и минеральные вещества напиток помогает работе сердечно-сосудистой системы, способствует пищеварению, укрепляет кости и мышцы.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo17)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())
		if message.text == 'Смузи':
			bot.send_message(message.chat.id,"Хороший выбор! Одна порция смузи позволяет восполнить суточную норму витаминов в организме. Научно доказано, что ежедневное употребление фруктов и овощей благоприятно сказывается на здоровье, но что, если нет возможности брать с собой эти продукты в качестве перекуса? Их можно соединить в коктейль и насладиться приятным вкусом смузи.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo18)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Протеиновый коктейль':
			bot.send_message(message.chat.id,"Хороший выбор! В сочетании с интенсивными занятиями в спортзале, белковый коктейль способствует формированию рельефа тела. С этой целью его рекомендуется принимать до и после тренировки.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo19)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id, ".".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=keyboard18())

		if message.text == 'Фраппучино':
			bot.send_message(message.chat.id,"Хороший выбор! В фраппучино содержится большое количество каллорий. Поэтому таким напитком запросто можно утолить чувство голода.")
			bot.send_photo(chat_id=message.from_user.id, photo=file_photo20)
			def keyboard18():
				markup18 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item38 = types.KeyboardButton("В меню")
				markup18.add(item38)
				return markup18
			bot.send_message(message.chat.id,".".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard18())
		if message.text == 'В меню':
			def keyboard19():
				markup19 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
				item39 = types.KeyboardButton("Горячее")
				item40 = types.KeyboardButton("Холодное")
				markup19.add(item39, item40)
				return markup19
			bot.send_message(message.chat.id, "Привет, я бот, созданный чтобы помочь выбрать тебе напиток!".format(message.from_user, bot.get_me()), parse_mode='html')
			bot.send_message(message.chat.id, "Что вы желаете выпить?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard19())

# RUN
bot.polling(none_stop=True)