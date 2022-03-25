from .models import Employee
from django_seed import Seed

import random


seeder = Seed.seeder()
my_position_list = [
    'Генеральный директор', 'Заместитель генерального директора', 'Менеджер по закупкам',
    'Младший менеджер', 'Продавец']

seeder.sentence()
seeder.sentence(ext_word_list=my_position_list)

seeder.add_entity(Employee, 10, {"full_name": lambda x: seeder.faker.name(),
                                 "position": lambda x: random.choice(my_position_list),
                                 "salary": lambda x: random.randint(0, 5000),
                                 "salary_paid": lambda x: random.randint(0, 5000),
                                 "level": lambda x: random.randint(0, 4),
                                 })

seeder.execute()
