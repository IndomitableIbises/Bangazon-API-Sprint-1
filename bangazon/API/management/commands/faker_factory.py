from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from API.models import Customer, Product, Product_Type, Order, Payment_Type, Employee, Training_Prog, Emp_Training, Department, Computer, Prod_Order
##Make sure and import any new models created~

##Any new models made, need to have a seeder.add_entity()
class Command(BaseCommand):

  def handle(self, *args, **options):
    seeder.add_entity(Customer, 10)
    seeder.add_entity(Product_Type, 10)
    seeder.add_entity(Product, 10, {'title': lambda x: seeder.faker.word(), 'description': lambda x: seeder.faker.paragraph(nb_sentences=12)}) # the number argument is the total num of rows you want created
    seeder.add_entity(Payment_Type, 10, {'name': lambda x: seeder.faker.credit_card_provider(), 'account_num': lambda x: seeder.faker.credit_card_number()})
    seeder.add_entity(Order, 10, {'payment_id': None}) # the number argument is the total num of rows you want created
    seeder.add_entity(Department, 10)
    seeder.add_entity(Computer, 10)
    seeder.add_entity(Employee, 10, {'name': lambda x: seeder.faker.name()})
    seeder.add_entity(Training_Prog, 10, {'max_attendees': lambda x: random.randint(1, 500), 'name': lambda x: seeder.faker.bs()})
    seeder.add_entity(Emp_Training, 10)
    seeder.add_entity(Prod_Order, 10)

    inserted_pks = seeder.execute()

