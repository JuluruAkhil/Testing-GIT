class FourWheeler(object):
	def __init__(self, _model, _clr, _size, _price, _ver, _yr):
	self.engineModel = _model
	self.color = _clr
	self.wheelSize = _size
	self.price = _price
	self.version = _ver
	self.year = _yr

	def compute_discount(self):
	if self.engineModel == 'HW':
		return self.price* 0.1
	if self.engineModel == 'LW':
		return self.price* 0.2
	return 0.0

	def get_on_road_price(self):
	if self.year == 2016:
		tax = 12.0
	elif self.year == 2017:
		tax = 13.0
	else:
		tax = 10.0

	return self.price * (1 + tax/100) - self.compute_discount()

obj = FourWheeler('HW', 'RED', 2.0, 1000000, 1.6, 2016)
obj.get_on_road_price()
