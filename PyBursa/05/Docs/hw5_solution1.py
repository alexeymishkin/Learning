import datetime
import dateutil.parser

class Person(object):

    def __init__(self, surname, first_name, birth_date, *args):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = dateutil.parser.parse(birth_date).date()
        if len(args) == 1:
            self.nickname = args[0]

    def get_age(self):
        now = datetime.datetime.now()
        age = now.year - self.birth_date.year
        if now.month < self.birth_date.month or (now.month == self.birth_date.month and now.day < self.birth_date.day):
            return str(age - 1)
        else:
            return str(age)

    def get_fullname(self):
        return '{} {}'.format(self.surname, self.first_name)

'''
i = Person('alexey', 'mishkin', '1988-04-07', 'hghgjhg')
print(i.get_age())
print(i.get_fullname())
print(dir(Person))
print(i.birth_date)
print(datetime.date(1988, 4, 7))'''