import factory
from faker import Factory
from csefemerideak.models import Efemeridea

faker = Factory.create()


class EfemerideaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Efemeridea

    text = faker.text()
    date = faker.date_of_birth()

