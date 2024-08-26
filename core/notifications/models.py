from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
import json


@receiver(post_save, sender=User)
def send_user_created_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        message = f'New user created: {instance.username}'
        channel_layer.group_send(
            'notifications',
            {
                'type': 'send_notification',
                'message': message
            }
        )
