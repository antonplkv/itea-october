class News:

    def __init__(self, title, body):
        self.__title = title
        self._body = body

    def __add__(self, other):
        new_title = self.__title + other.__title
        new_body = self._body + other._body
        return News(new_title, new_body)

    def get_title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value

    def get_body(self):
        return self._body

    def set_body(self, value):
        self._body = value

    def __str__(self):
        return f'Title is {self.__title}\nBody is {self._body}'


news1 = News('Football', '............')
news2 = News('Hockey', '......')
news3 = News('Coronavirues', '.......')

r = news1 + news2
print(r.get_title())
print(news1._News__title)

#r = news1.__add__(news2)


# result_str = str(r)
# print(result_str)

