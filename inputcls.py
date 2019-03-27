# Class from law
class Law:
	name = (u'Арбитражный суд г. Москвы')
	adress = (u'115191, г. Москва, ул. Б. Тульская, 17')

	# Metod from set law data
	def set(self, name, adress):
		self.name = name
		self.adress = adress

# Class from petitioners
class Plf:
	name = (u'Департамент городского имущества г. Москвы')
	adress = (u'000000, г. ******, ул. *******, 00')

	# Metod from set petitioners data
	def set(self, name, adress):
		self.name = name
		self.adress = adress

# Class from defendant
class Dft:
	name = (u'ООО «ЦЕНТР***»')
	ogrn = ('103*73*38*8*9')
	adress = (u'1*72*3,  город Москва,  Псковская улица, дом * корпус *, квартира 1**')


	# Metod from set defendant data
	def set(self, name, ogrn, adress):
		self.name = name
		self.ogrn = ogrn
		self.adress = adress

# Class from vakil
class Vkl:
	name = (u'******* Максим Александрович')
	tel = ('8977*27*19*')
	email = ('s****g*l@****e*.ru')
	adress = (u'000000,  город Москва, ***** улица, дом 5 корпус 3, квартира 15')


	# Metod from set vakil data
	def set(self, name, tel, email, adress):
		self.name = name
		self.tel = tel
		self.email = email
		self.adress = adress

# Class from lawsuit
class Lawsuit:
	number = (u'А40-*01*2*/201*')
	link = ('www.sud.ru/dela-nema')


	# Metod from set vakil data
	def set(self, number, link):
		self.number = number
		self.link = link


