import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## fake data script
import random
from first_app.models import *
from faker import Faker

fakeGen = Faker()
topicList = ['Search', 'Social', 'Market', 'News', 'Games']

def addTopics(): 
    # return tuple of object that is created or got (at index 0)
    t = Topic.objects.get_or_create(top_name=random.choice(topicList))[0]
    return t

def populate(): 
    n = input('enter a integer to generate fake data: ')

    for i in range(int(n)): 
        topic = addTopics()
        fakeUrl = fakeGen.url()
        fakeDate = fakeGen.date()
        fakeName = fakeGen.company()
        webpg = Webpage.objects.get_or_create(topic=topic,name=fakeName,url=fakeUrl)[0]
        accRec = AccessRecorder.objects.get_or_create(name=webpg,date=fakeDate)[0]

def populateUser(): 
    n = input('enter a integer to generate fake User data: ')

    for i in range(int(n)): 
        fake_first_name = fakeGen.first_name()
        fake_last_name = fakeGen.last_name()
        fake_email = fakeGen.email()
        user = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)

if __name__ == '__main__': 
    print('populating fakeData...')
    res = input('which fake data you want to generate ? ')
    res = str(res).lower()
    if res == 'populate': 
        populate()
        print('fakeData complete')
    elif res == 'populateuser': 
        populateUser()
        print('fakeData complete')
    else: 
        print('unexpected function')
    