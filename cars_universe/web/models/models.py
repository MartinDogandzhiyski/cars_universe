from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

from cars_universe.accounts.models import CarsUniverseUser

UserModel = get_user_model()


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


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

    photo = models.ImageField(upload_to="mediafiles/",
                              validators=(
                                  validate_image,
                              ),
                              blank=True,
                              null=True,
                              help_text='Maximum file size allowed is 5Mb'
                              )

    made_date = models.IntegerField(
        default=2005
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    likes = models.IntegerField(
        default=0,
    )

    hp = models.IntegerField()

    def __str__(self):
        return f"The {self.name} - {self.type}"

    class Meta:
        unique_together = ('user', 'name')


class Tool(models.Model):
    ACCESSORIES = 'ACCESSORIES'
    TOOLS = 'TOOLS'
    TYPES = [(x, x) for x in (ACCESSORIES, TOOLS)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    brand = models.CharField(
        max_length=30,
    )

    name = models.CharField(
        max_length=40,
    )

    photo = models.ImageField(upload_to="mediafiles/",
                              validators=(
                                  validate_image,
                              ),
                              blank=True,
                              null=True,
                              help_text='Maximum file size allowed is 5Mb'
                              )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.IntegerField(
        validators=[MinValueValidator(1)],
    )
    orderr = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='item_toolss',
        blank = True,
        null = True,
    )


class CarPart(models.Model):
    EnginePart = 'EnginePart'
    OTHER = 'OTHER'
    TYPES = [(x, x) for x in (EnginePart, OTHER)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    brand = models.CharField(
        max_length=30,
    )

    brand_for = models.CharField(
        max_length=30,
    )

    name = models.CharField(
        max_length=40,
    )

    photo = models.ImageField(upload_to="mediafiles/",
                              validators=(
                                  validate_image,
                              ),
                              blank=True,
                              null=True,
                              help_text='Maximum file size allowed is 5Mb'
                              )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.IntegerField(
        validators=[MinValueValidator(1)],
    )
    orderr = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='item_partss',
        blank = True,
        null = True,
    )


class Order(models.Model):
    user = models.ForeignKey(CarsUniverseUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    item_tools = models.ManyToManyField(Tool)
    item_parts = models.ManyToManyField(CarPart)
