import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobproject2.settings')
import django
django.setup()

from faker import Faker
fakegen = Faker()

from random import *
def phonenumgen():
    phone = randint(6,9)
    num = str(phone)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

from job.models import Development
def populate(n):
    for i in range(n):
        fdate = fakegen.date()
        fcompany = fakegen.company()
        ftitle = fakegen.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fakegen.random_element(elements=('M.Tech','B.Tech','MCA','Phd'))
        faddress = fakegen.address()
        femail = fakegen.email()
        fphone = phonenumgen()
        dev_jobs_record = Development.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phonenumber=fphone)
n = int(input('Enter Number Of Records: '))
populate(n)
print(f'{n} numbers of record inserted successfully....')

from job.models import DebugTester
def populate(n):
    for i in range(n):
        fdate = fakegen.date()
        fcompany = fakegen.company()
        ftitle = fakegen.random_element(elements=('Unit Testing','Integration Testing','System testing','Acceptance testing','Functional Testing','Security Testing','Performance/Load Testing','Usability Testing','Compatibility testing'))
        feligibility = fakegen.random_element(elements=('M.Tech','B.Tech','MCA','Phd'))
        faddress = fakegen.address()
        femail = fakegen.email()
        fphone = phonenumgen()
        dev_jobs_record = DebugTester.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phonenumber=fphone)
n = int(input('Enter Number Of Records: '))
populate(n)
print(f'{n} numbers of record inserted successfully....')

from job.models import Hacking
def populate(n):
    for i in range(n):
        fdate = fakegen.date()
        fcompany = fakegen.company()
        ftitle = fakegen.random_element(elements=('White Hat / Ethical Hackers','Black Hat Hackers','Gray Hat Hackers','Script Kiddies','Green Hat Hackers','Blue Hat Hackers','Red Hat Hackers','State/Nation Sponsored Hackers','Hacktivist','Malicious insider or Whistleblower'))
        feligibility = fakegen.random_element(elements=('M.Tech','B.Tech','MCA','Phd'))
        faddress = fakegen.address()
        femail = fakegen.email()
        fphone = phonenumgen()
        dev_jobs_record = Hacking.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail, phonenumber=fphone)
n = int(input('Enter Number Of Records: '))
populate(n)
print(f'{n} numbers of record inserted successfully....')
