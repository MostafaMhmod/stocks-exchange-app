import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(
        lambda n: "user{0}.user{1}@example.com".format(n, n)
    )
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Sequence(
        lambda n: "user{0}.user{1}@example.com".format(n, n)
    )
    is_staff = False
    is_superuser = False
    password = factory.PostGenerationMethodCall("set_password", "airteam")
