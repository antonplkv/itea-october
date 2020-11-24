import mongoengine as me

me.connect('TEST_LESSON10')


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)


if __name__ == '__main__':
    users = User.objects(age__gte=18)
    for u in users:
        print(u.first_name, u.last_name, u.interests, u.age)
        print('*' * 10)

