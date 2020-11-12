import shelve

FILE = 'COUNTRIES'


def shelve_required(func):

    def wrapper(*args, **kwargs):
        with shelve.open(FILE) as db:
            result = func(*args, **kwargs)
            return result

    return wrapper


def add_country_and_capital(country, capital):

    with shelve.open(FILE) as db:
        db[country] = capital


def get_capital_by_by_country(country):

    with shelve.open(FILE) as db:
        return db.get(country, 'Нет такой страны в БД')


# add_country_and_capital('Ukraine', 'Kyiv')
# add_country_and_capital('Belarus', 'Minsk')

print(get_capital_by_by_country('Ukraine'))