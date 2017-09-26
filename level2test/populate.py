import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level2test.settings')

import django
django.setup()

import random
from app_afresh.models import user

from faker import Faker

fakegen = Faker()

def populate(n=5):

	for i in range(n):
		fakename = fakegen.name().split()
		ffirstname = fakename[0]
		flastname = fakename[1]
		femail = fakegen.email()

		fakeuser = user.objects.get_or_create(firstname=ffirstname, lastname=flastname, email=femail)[0]


if __name__ == '__main__':
	print('Populating....')
	populate(20)
	print('Populating process done!')