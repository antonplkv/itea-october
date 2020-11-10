class SingleError(Exception):
    pass


class Singletone:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            obj = super().__new__(cls, *args, **kwargs)
            cls._instance = obj
            return obj
        return cls._instance



obj1 = Singletone()
obj2 = Singletone()
print(obj1 is obj2)