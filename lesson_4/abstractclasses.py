from abc import ABC, abstractmethod


class Phone(ABC):

    def __init__(self, model, imei):
        self._model = model
        self._imei = imei

    @abstractmethod
    def call(self):
        pass


class Smartphone(Phone):

    def __init__(self, model, imei, os_):
        super(Smartphone, self).__init__(model, imei)
        self._os = os_

    def call(self):
        print(f'calling from {self._model}')

    def download_application(self):
        print('Downloading application')


Smartphone('Iphone', '312312312312', 'ios').call()