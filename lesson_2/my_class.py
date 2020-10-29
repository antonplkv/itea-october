class Phone:

    type_ = 'Мобильный телефон'

    def __init__(self, model, imei, phone_number):
        self.model = model
        self.imei = imei
        self.phone_number = phone_number

    def call(self, to_number):
        print(f'Звоним с {self.phone_number} на {to_number}')


class SatellitePhone:

    def call(self):
        print('Делаем спутниковый звонок')


class Smartphone(Phone, SatellitePhone):

    type_ = 'Смартфон'

    def download_application(self):
        print('Downloading application from market')



phone1 = Phone('Nokia', 'eqweqweq12312', '09578888888')
print(phone1.model, phone1.phone_number, phone1.imei)
phone1.model = 'Mototorolla'
print(phone1.model, phone1.phone_number, phone1.imei)
phone1.call('04124123123')

print('-'*35)
phone2 = Phone('Siemens', 'ewqewqewqeqwe', '07777777777')
phone2.call('08888888888')
print(phone2.model, phone2.phone_number, phone2.imei)
print('-'*35)
smartphone = Smartphone('Iphone', 'qweqweqw', '0333333333')
smartphone.call()
smartphone.download_application()

print('-'*35)
print(Phone.type_)
print(Smartphone.type_)
Smartphone.type_ = 'Современный смартфон'
print(smartphone.type_)






