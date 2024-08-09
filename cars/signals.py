import django.db.models.deletion
from django.db.models.signals import (
  pre_save,
  post_save,
  pre_delete,
  post_delete
)
from django.dispatch import receiver
from cars.models import Car
# sender is the model that sends the signal
# instance is the instance of the model that sends the signal

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('Car pre save signal')

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('Car post save signal')

@receiver(pre_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('Car pre delete signal')

@receiver(post_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('Car post delete signal')
