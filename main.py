from faker import Faker
from Person import Person
import random
from datetime import datetime
import json
faker = Faker()

with open('fakers.json', '+a', encoding='utf-8', newline='') as file:
    data = []
    for i in range(1, 100001):
        person = Person(i, faker.name(), faker.last_name(), datetime.strftime(faker.date_of_birth(), '%d/%m/%Y'), random.randint(0, 1), random.randint(1, 4))
        data.append(json.dumps(person.parse_to_json()))
    file.write(','.join(data))
