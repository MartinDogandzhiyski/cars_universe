from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Car(models.Model):
    AUDI = "Audi"
    BMW = "Bmw"
    VW = "Vw"
    OPEL = "Opel"
    FORD = "Ford"
    OTHER = "Other"
    TYPES = [(x, x) for x in (AUDI, BMW, VW, OPEL, FORD, OTHER)]
    # Fields(Columns)
    name = models.CharField(
        max_length=30,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    made_date = models.IntegerField(
        default=2005
    )
    # One-to-one relations

    # One-to-many relations

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"The {self.name} - {self.type}"

    class Meta:
        unique_together = ('user', 'name')


class Photo(models.Model):
    photo = models.ImageField(
        validators=(
            #validate_file_max_size(5),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Event(models.Model):
    AUDI = "Audi"
    BMW = "Bmw"
    VW = "Vw"
    OPEL = "Opel"
    FORD = "Ford"
    OTHER = "Other"
    TYPES = [(x, x) for x in (AUDI, BMW, VW, OPEL, FORD, OTHER)]
    name = models.CharField(
        max_length=30,
    )

    cars_brand = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    address = models.CharField(max_length=40,)

    date = models.DateTimeField()

    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Tool(models.Model):
    pass