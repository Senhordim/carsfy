from django.db.models import Sum
from django.db.models.signals import (
  post_save,
  post_delete,
  pre_save,
)
from django.dispatch import receiver
from cars.models import Car, CarInventory
from ai_services.google_generativeai.client import get_car_ai_bio_google
# sender is the model that sends the signal
# instance is the instance of the model that sends the signal

# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     print('Car pre save signal')

# @receiver(pre_delete, sender=Car)
# def car_post_save(sender, instance, **kwargs):
#     print('Car pre delete signal')


def update_inventory():
    cars_count = Car.objects.all().count()
    cars_Value = Car.objects.all().aggregate(
      total_value = Sum('value')
    )['total_value']

    CarInventory.objects.create(
      cars_count=cars_count,
      cars_value=cars_Value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        instance.description = get_car_ai_bio_google(instance.brand.name, instance.model, instance.model_year)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    update_inventory()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    update_inventory()

