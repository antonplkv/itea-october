import mongoengine as me
import datetime

me.connect('TEST_LESSON11')


class UserProfile(me.Document):
    login = me.StringField(required=True, unique=True, min_length=4, max_length=128)
    password = me.StringField(required=True, min_length=8)
    about_me = me.StringField()
    likes = me.IntField(default=0)


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()
    user_profile = me.ReferenceField(UserProfile, reverse_delete_rule=me.NULLIFY)

    def say_hello(self):
        return f'Hello, my name is {self.first_name}'

    def __str__(self):
        return f'{self.first_name} {self.age}'

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)


if __name__ == '__main__':
    # users = User.objects((me.Q(age__gte=20) | me.Q(first_name='John')) & me.Q(interests__in=['cars']))
    # users = User.objects()
    # print(users)
    # for u in users:
    #     print(u.say_hello())


    user_profile = UserProfile(login='Nikolai8888888', password='qwerwrtrtryryyr').save()
    user = User(first_name='Nikolai', interests=['cars'], age=23, user_profile=user_profile)
    user.save()
    print(user.age, user.first_name, user.last_name, user.id, user.created_at, user.user_profile)
    # print(user.age, user.first_name, user.last_name, user.id)

