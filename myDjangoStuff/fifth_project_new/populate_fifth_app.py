import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fifth_project.settings')

import django
django.setup()

# Generate fake data
import random
from fifth_app.models import UserInfo
from faker import Faker

fakegen = Faker()

def generate_users(users=10):
    for user in range(users):
        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name()
        fake_email = fakegen.free_email()

        u = UserInfo.objects.get_or_create(firstName=fake_firstName,
            lastName=fake_lastName,email=fake_email)[0]

        u.save()

if __name__ == '__main__':
    print("Populating script!")
    generate_users(20)
    print("Populated!")
