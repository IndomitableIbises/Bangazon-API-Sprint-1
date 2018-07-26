from django.core.management.base import BaseCommand

from django_seed import Seed

seeder = Seed.seeder()

from API.models import Customer, Product

##Make sure and import any new models created~



##Any new models made, need to have a seeder.add_entity()

class Command(BaseCommand):



  def handle(self, *args, **options):

    seeder.add_entity(Customer, 10)

    seeder.add_entity(Product, 10) # the number argument is the total num of rows you want created

    



    inserted_pks = seeder.execute()

