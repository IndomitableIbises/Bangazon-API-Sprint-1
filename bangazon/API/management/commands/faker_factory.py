from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
from API.models import Customer, Product, Product_Type, Order, Payment_Type, Employee, Training_Prog, Emp_Training, Department, Computer
##Make sure and import any new models created~

##Any new models made, need to have a seeder.add_entity()
class Command(BaseCommand):

  def handle(self, *args, **options):
    seeder.add_entity(Customer, 10)
    seeder.add_entity(Product_Type, 10)
    seeder.add_entity(Product, 10) # the number argument is the total num of rows you want created
    seeder.add_entity(Payment_Type, 10)
    seeder.add_entity(Order, 10)
    seeder.add_entity(Department, 10)
    seeder.add_entity(Computer, 10)
    seeder.add_entity(Training_Prog, 10)
    seeder.add_entity(Employee, 10)
    seeder.add_entity(Emp_Training, 10)


    inserted_pks = seeder.execute()

