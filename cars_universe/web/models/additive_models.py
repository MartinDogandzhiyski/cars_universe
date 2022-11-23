from django.db import models
from django.contrib.auth import get_user_model

from cars_universe.web.models.models import Car

UserModel = get_user_model()


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

    photo = models.ImageField(upload_to="mediafiles/",
        validators=(
            # validate_file_max_size(5),
        )
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    address = models.CharField(max_length=40,)

    date = models.DateTimeField()


class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')



