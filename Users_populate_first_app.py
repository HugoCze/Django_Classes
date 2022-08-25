import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

#Order does matter here - initializing django
import django
django.setup()

#FAKE POP SCRIPT
from first_app.models import User
import random
from faker import Faker
fakegen = Faker()


def populate(N=5):
    for entery in range(N):

        fake_name = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        fake_users = User.objects.get_or_create(
            FirstName=fake_name, LastName=fake_lastname, Email=fake_email)[0]


if __name__ == '__main__':
    print('users populating script')
    populate(50)
    print('users populating complete')
