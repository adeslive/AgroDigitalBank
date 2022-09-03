from django.core.management.base import BaseCommand
from faker import Faker
from bank.models import Bank, Client

class Command(BaseCommand):
    help = "Generate Data"

    def handle(self, *args, **kwargs):
        faker = Faker()
        for _ in range(15):
            bank = Bank.objects.create(bank_name = faker.bs())
            for _ in range(40):
                Client.objects.create(first_name = faker.first_name(), last_name = faker.last_name(), date_of_birth = faker.date_of_birth(minimum_age = 18), dni = faker.random_number(digits=13), bank = bank)